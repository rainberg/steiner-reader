"""Translation service router — per-lecture sentence translation.

Uses Auth Service for credits management:
- Reserve credits before translation starts
- Settle (actual deduction) after translation completes
- Refund on failure
"""

import asyncio
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import async_session as AsyncSessionLocal, get_db
from app.db.models import Lecture, Paragraph, Sentence
from app.routers.auth import AuthUser, require_user, get_current_user
from app.services.auth_client import (
    reserve_credits,
    settle_credits,
    refund_credits,
    get_credits_balance,
)
from app.services.translator import translate_lecture_sentences

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["translation"])

COST_PER_LECTURE = 10


_running_tasks: set[int] = set()

_running_task_tokens: dict[int, str] = {}


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Start translating a lecture (costs credits via auth-service, runs in background)."""
    if lecture_id in _running_tasks:
        raise HTTPException(status_code=409, detail="该章节正在翻译中，请等待完成")

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
    if remaining == 0:
        return {
            "lecture_id": lecture_id,
            "status": "already_translated",
            "message": "All sentences already translated",
            "translated": translated,
            "total": total,
        }

    balance = await get_credits_balance(user.raw_token)
    available = float(balance.get("credits", 0)) - float(balance.get("credits_reserved", 0)) if balance else user.credits
    if available < COST_PER_LECTURE:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：翻译需要 {COST_PER_LECTURE} 点，当前可用 {available:.0f} 点"
        )

    reserve_result = await reserve_credits(
        user.raw_token,
        amount=COST_PER_LECTURE,
        reference_id=f"translate-lecture-{lecture_id}",
        description=f"翻译讲座 {lecture_id}",
    )
    if not reserve_result or "error" in reserve_result:
        error_msg = reserve_result.get("error", "积分预扣失败") if reserve_result else "积分预扣失败"
        raise HTTPException(status_code=402, detail=f"积分预扣失败: {error_msg}")

    _running_task_tokens[lecture_id] = user.raw_token
    asyncio.create_task(_do_translate_lecture(lecture_id))

    balance = await get_credits_balance(user.raw_token)
    new_credits = balance.get("credits", user.credits) if balance else user.credits

    return {
        "lecture_id": lecture_id,
        "status": "started",
        "message": f"Translation started (预扣 {COST_PER_LECTURE} 点)",
        "translated": translated,
        "total": total,
        "credits": new_credits,
        "cost": COST_PER_LECTURE,
    }


@router.get("/lectures/{lecture_id}/translation-cost")
async def get_translation_cost(
    lecture_id: int,
    user: AuthUser | None = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get the cost to translate a lecture."""
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

    user_credits = None
    can_afford = None
    if user:
        balance = await get_credits_balance(user.raw_token)
        if balance:
            user_credits = float(balance.get("credits", 0)) - float(balance.get("credits_reserved", 0))
            can_afford = user_credits >= COST_PER_LECTURE

    return {
        "lecture_id": lecture_id,
        "total": total,
        "translated": translated,
        "remaining": total - translated,
        "cost": COST_PER_LECTURE if total > translated else 0,
        "already_translated": total > 0 and translated == total,
        "user_credits": user_credits,
        "can_afford": can_afford,
    }


@router.get("/lectures/{lecture_id}/translation-status")
async def lecture_translation_status(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get translation progress for a single lecture."""
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
    }


async def _do_translate_lecture(lecture_id: int):
    """Background task: translate all un-translated sentences in a lecture.

    Credits flow:
    1. Credits were already reserved before this task started
    2. On success: settle (confirm actual deduction)
    3. On failure: refund the reserved credits
    """
    _running_tasks.add(lecture_id)
    token = _running_task_tokens.pop(lecture_id, None)
    success = False

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

            for para in lecture.paragraphs:
                for sent in para.sentences:
                    if not sent.text_zh:
                        idx = len(untranslated)
                        untranslated.append(sent.text_de)
                        sentence_map[idx] = sent

            if not untranslated:
                success = True
                return

            logger.info(f"Lecture {lecture_id}: translating {len(untranslated)} sentences...")
            total = len(untranslated)

            BATCH_SIZE = 20
            for batch_start in range(0, total, BATCH_SIZE):
                batch_sentences = untranslated[batch_start:batch_start + BATCH_SIZE]
                translated_batch = await translate_lecture_sentences(batch_sentences)

                for local_idx, zh_text in enumerate(translated_batch):
                    global_idx = batch_start + local_idx
                    if global_idx in sentence_map:
                        sentence_map[global_idx].text_zh = zh_text

                await db.commit()
                logger.info(f"Lecture {lecture_id}: committed batch {batch_start}-{batch_start+len(batch_sentences)}")

            logger.info(f"Lecture {lecture_id}: done, {total} sentences translated")
            success = True

    except Exception as e:
        logger.error(f"Lecture {lecture_id}: translation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
    finally:
        _running_tasks.discard(lecture_id)

        if token:
            if success:
                settle_result = await settle_credits(
                    token,
                    reserved_amount=COST_PER_LECTURE,
                    actual_amount=COST_PER_LECTURE,
                    reference_id=f"translate-lecture-{lecture_id}",
                    description=f"翻译讲座 {lecture_id} 完成",
                )
                if not settle_result or "error" in settle_result:
                    logger.error(f"Lecture {lecture_id}: settle credits failed: {settle_result}")
            else:
                refund_result = await refund_credits(
                    token,
                    amount=COST_PER_LECTURE,
                    reference_id=f"translate-lecture-{lecture_id}",
                    description=f"翻译讲座 {lecture_id} 失败，退还积分",
                )
                if not refund_result or "error" in refund_result:
                    logger.error(f"Lecture {lecture_id}: refund credits failed: {refund_result}")
