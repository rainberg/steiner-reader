"""Translation service router — per-lecture sentence translation with contribution tracking."""

import asyncio
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import async_session as AsyncSessionLocal, get_db
from app.db.models import Lecture, Paragraph, Sentence, User
from app.routers.auth import require_user, get_current_user
from app.services.translator import translate_lecture_sentences
from app.services.credit_service import (
    compute_price, atomic_deduct_credits, add_contribution, grant_access,
    get_contributions, check_download_access, get_access_types,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["translation"])

# Track running tasks to prevent duplication
_running_tasks: set[int] = set()


def _build_extra_fields(user, db, lecture):
    """Return the extra fields added to lecture content responses.

    Extracted as a module-level helper so books.py and lectures.py can reuse it
    without circular imports.
    """
    # contributions will be filled by caller via get_contributions
    pass


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Start translating a lecture (costs credits, runs in background).

    If all sentences already have text_zh, simulates translation progress then publishes.
    Otherwise triggers real network translation for missing sentences.
    """
    if lecture_id in _running_tasks:
        raise HTTPException(status_code=409, detail="该章节正在翻译中，请等待完成")

    # Fetch lecture to check current state
    lecture_result = await db.execute(
        select(Lecture).where(Lecture.id == lecture_id)
    )
    lecture = lecture_result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="章节不存在")

    if lecture.is_published:
        raise HTTPException(status_code=400, detail="该讲译文已公开，无需再次翻译")

    # Get sentence counts
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0

    translated_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
    )
    translated = translated_result.scalar() or 0

    # Determine cost by sentence count × coefficient (or manual override)
    remaining = total - translated
    cost = await compute_price(db, "translate_lecture", remaining if remaining > 0 else total)

    # Atomic deduction
    try:
        new_credits = await atomic_deduct_credits(
            db, user, cost,
            transaction_type="translate_lecture",
            reference_type="lecture",
            reference_id=lecture_id,
            description=f"翻译讲座 {lecture.title_de or lecture_id}",
        )
    except ValueError:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：翻译需要 {cost} 点，当前余额 {user.credits} 点"
        )

    await db.commit()

    # Decide: simulate or real translation
    if remaining == 0:
        # All sentences already have text_zh — simulate progress then publish
        lecture.is_translating = True
        lecture.translate_progress = 0
        lecture.translate_total = total
        await db.commit()
        asyncio.create_task(_do_simulate_translate_lecture(lecture_id, user.id))
        status = "simulating"
        message = f"数据库中已有译文，正在模拟翻译进度 (消耗 {cost} 点)"
    else:
        # Real translation needed
        lecture.is_translating = True
        lecture.translate_progress = translated
        lecture.translate_total = total
        await db.commit()
        asyncio.create_task(_do_translate_lecture(lecture_id, user.id))
        status = "started"
        message = f"翻译已启动 (消耗 {cost} 点)"

    return {
        "lecture_id": lecture_id,
        "status": status,
        "message": message,
        "translated": translated,
        "total": total,
        "credits": new_credits,
        "cost": cost,
    }


@router.get("/lectures/{lecture_id}/translation-cost")
async def get_translation_cost(
    lecture_id: int,
    user: User | None = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get the cost to translate a lecture, including publication status."""
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0

    translated_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
    )
    translated = translated_result.scalar() or 0

    remaining = total - translated
    cost = await compute_price(db, "translate_lecture", remaining) if remaining > 0 else 0

    # Check publication status
    lecture_result = await db.execute(
        select(Lecture.is_published).where(Lecture.id == lecture_id)
    )
    is_published = lecture_result.scalar() or False

    return {
        "lecture_id": lecture_id,
        "total": total,
        "translated": translated,
        "remaining": remaining,
        "cost": 0 if (total > 0 and translated == total and is_published) else cost,
        "already_translated": total > 0 and translated == total,
        "is_published": is_published,
        "user_credits": user.credits if user else None,
        "can_afford": user.credits >= cost if user else None,
    }


@router.get("/lectures/{lecture_id}/translation-status")
async def lecture_translation_status(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get translation progress. Checks lecture.is_translating for running jobs first."""
    lecture_result = await db.execute(
        select(Lecture).where(Lecture.id == lecture_id)
    )
    lecture = lecture_result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="章节不存在")

    if lecture.is_translating:
        return {
            "lecture_id": lecture_id,
            "total": lecture.translate_total,
            "translated": lecture.translate_progress,
            "completed": False,
            "is_translating": True,
        }

    # Fall back to counting
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0

    translated_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
    )
    translated = translated_result.scalar() or 0

    return {
        "lecture_id": lecture_id,
        "total": total,
        "translated": translated,
        "completed": translated == total and total > 0,
        "is_translating": False,
    }


async def _do_translate_lecture(lecture_id: int, user_id: int):
    """Background task: translate untranslated sentences, update progress, publish on completion."""
    _running_tasks.add(lecture_id)
    try:
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Lecture)
                .where(Lecture.id == lecture_id)
                .options(
                    selectinload(Lecture.paragraphs)
                    .selectinload(Paragraph.sentences)
                )
            )
            lecture = result.scalar_one_or_none()
            if not lecture:
                logger.error(f"Lecture {lecture_id} not found")
                return

            untranslated = []
            sentence_map = {}
            global_idx = 0

            for para in lecture.paragraphs:
                for sent in para.sentences:
                    if not sent.text_zh:
                        untranslated.append(sent.text_de)
                        sentence_map[global_idx] = sent
                        global_idx += 1

            if not untranslated:
                # All done — just publish
                lecture.is_published = True
                lecture.is_translating = False
                await _record_first_contribution(db, user_id, lecture)
                await db.commit()
                return

            logger.info(f"Lecture {lecture_id}: translating {len(untranslated)} sentences...")
            total = len(untranslated)

            BATCH_SIZE = 20
            for batch_start in range(0, total, BATCH_SIZE):
                batch_sentences = untranslated[batch_start:batch_start + BATCH_SIZE]
                translated_batch = await translate_lecture_sentences(batch_sentences)

                for local_idx, zh_text in enumerate(translated_batch):
                    gidx = batch_start + local_idx
                    if gidx in sentence_map:
                        sentence_map[gidx].text_zh = zh_text

                # Update lecture progress
                lecture.translate_progress = min(batch_start + len(batch_sentences), total)
                await db.commit()
                logger.info(f"Lecture {lecture_id}: committed batch {batch_start}-{batch_start+len(batch_sentences)}")

            # All done — publish
            lecture.is_published = True
            lecture.is_translating = False
            lecture.translate_progress = 0
            lecture.translate_total = 0
            await _record_first_contribution(db, user_id, lecture)
            await db.commit()
            logger.info(f"Lecture {lecture_id}: done, {total} sentences translated and published")

    except Exception as e:
        logger.error(f"Lecture {lecture_id}: translation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        # Reset translating flag on failure so user can retry
        try:
            async with AsyncSessionLocal() as db:
                result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
                lecture = result.scalar_one_or_none()
                if lecture:
                    lecture.is_translating = False
                    await db.commit()
        except Exception:
            pass
    finally:
        _running_tasks.discard(lecture_id)


async def _do_simulate_translate_lecture(lecture_id: int, user_id: int):
    """Background task: simulate translation progress for lectures with existing text_zh,
    then publish. No actual translation API calls — just progress bar + publication."""
    _running_tasks.add(lecture_id)
    try:
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(Lecture)
                .where(Lecture.id == lecture_id)
                .options(
                    selectinload(Lecture.paragraphs)
                    .selectinload(Paragraph.sentences)
                )
            )
            lecture = result.scalar_one_or_none()
            if not lecture:
                logger.error(f"Lecture {lecture_id} not found")
                return

            total = lecture.translate_total
            logger.info(f"Lecture {lecture_id}: simulating translation of {total} sentences...")

            BATCH_SIZE = 20
            for batch_start in range(0, total, BATCH_SIZE):
                await asyncio.sleep(0.3)
                lecture.translate_progress = min(batch_start + BATCH_SIZE, total)
                await db.commit()

            # Done — publish
            lecture.is_published = True
            lecture.is_translating = False
            lecture.translate_progress = 0
            lecture.translate_total = 0
            await _record_first_contribution(db, user_id, lecture)
            await db.commit()
            logger.info(f"Lecture {lecture_id}: simulation done, published")

    except Exception as e:
        logger.error(f"Lecture {lecture_id}: simulation failed: {e}")
        try:
            async with AsyncSessionLocal() as db:
                result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
                lecture = result.scalar_one_or_none()
                if lecture:
                    lecture.is_translating = False
                    await db.commit()
        except Exception:
            pass
    finally:
        _running_tasks.discard(lecture_id)


async def _record_first_contribution(db: AsyncSession, user_id: int, lecture):
    """Record first-translation contribution and grant download access."""
    await add_contribution(db, user_id, lecture.id, "first_translation")
    await grant_access(db, user_id, lecture.id, "translator")
