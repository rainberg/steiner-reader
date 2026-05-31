"""Translation service router — per-lecture sentence translation.

Uses Auth Service for credits management:
- Reserve credits before translation starts
- Settle (actual deduction) after translation completes
- Refund on failure

Uses database-backed job tracking (UserTranslationJob) instead of
in-memory sets, so translation state survives server restarts.
"""

import asyncio
import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import async_session as AsyncSessionLocal, get_db
from app.db.models import Contribution, Lecture, Paragraph, Sentence
from app.routers.auth import AuthUser, require_user, get_current_user
from app.services.auth_client import (
    reserve_credits,
    settle_credits,
    refund_credits,
    get_credits_balance,
)
from app.services.credit_service import add_contribution, atomic_deduct_credits
from app.services.translation_service import (
    is_lecture_running,
    start_translation_job,
    complete_translation_job,
    fail_translation_job,
    detect_orphan_jobs,
    set_publication_status,
    get_publication_status,
)
from app.services.translator import translate_lecture_sentences

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["translation"])

COST_PER_LECTURE = 10


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Start translating a lecture (costs credits via auth-service, runs in background)."""
    await detect_orphan_jobs(db)

    if await is_lecture_running(db, lecture_id):
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

    lec_result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
    lecture = lec_result.scalar_one_or_none()
    book_id = lecture.book_id if lecture else None

    remaining = total - translated
    if remaining == 0:
        if lecture and not lecture.is_published:
            existing = await db.execute(
                select(Contribution).where(
                    Contribution.user_id == user.id,
                    Contribution.lecture_id == lecture_id,
                    Contribution.contribution_type == "translate",
                )
            )
            if existing.scalar_one_or_none():
                lecture.is_published = True
                await set_publication_status(db, lecture_id, book_id, "published", user.id)
                await db.commit()
                return {
                    "lecture_id": lecture_id,
                    "status": "already_translated",
                    "message": "All sentences already translated",
                    "translated": translated,
                    "total": total,
                }

            balance = await get_credits_balance(user.raw_token)
            available = float(balance.get("credits", 0)) - float(balance.get("credits_reserved", 0)) if balance and "error" not in balance else user.credits
            if available < COST_PER_LECTURE:
                raise HTTPException(
                    status_code=402,
                    detail=f"点数不足：翻译需要 {COST_PER_LECTURE} 点，当前可用 {available:.0f} 点"
                )
            ref_id = f"translate-lecture-{lecture_id}-{uuid.uuid4().hex[:8]}"
            deduct_result = await atomic_deduct_credits(
                user.raw_token, COST_PER_LECTURE,
                reference_id=ref_id,
                description=f"翻译讲座 {lecture_id}",
            )
            if "error" in deduct_result:
                error_detail = deduct_result.get("error", "未知错误")
                logger.error(f"Lecture {lecture_id}: deduct credits failed: {deduct_result}")
                raise HTTPException(status_code=402, detail=f"积分扣费失败: {error_detail}")
            lecture.is_published = True
            await set_publication_status(db, lecture_id, book_id, "published", user.id)
            await add_contribution(
                db, user.id, lecture_id,
                access_type="translate",
                display_name=user.display_name,
                book_id=lecture.book_id,
                cost=COST_PER_LECTURE,
                grants_download=True,
            )
            await db.commit()
        return {
            "lecture_id": lecture_id,
            "status": "already_translated",
            "message": "All sentences already translated",
            "translated": translated,
            "total": total,
        }

    balance = await get_credits_balance(user.raw_token)
    available = float(balance.get("credits", 0)) - float(balance.get("credits_reserved", 0)) if balance and "error" not in balance else user.credits
    if available < COST_PER_LECTURE:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：翻译需要 {COST_PER_LECTURE} 点，当前可用 {available:.0f} 点"
        )

    ref_id = f"translate-lecture-{lecture_id}-{uuid.uuid4().hex[:8]}"
    reserve_result = await reserve_credits(
        user.raw_token,
        amount=COST_PER_LECTURE,
        reference_id=ref_id,
        description=f"翻译讲座 {lecture_id}",
    )
    if not reserve_result or "error" in reserve_result:
        error_msg = reserve_result.get("error", "积分预扣失败") if reserve_result else "积分预扣失败"
        raise HTTPException(status_code=402, detail=f"积分预扣失败: {error_msg}")

    await start_translation_job(db, lecture_id, user.id, book_id)
    await set_publication_status(db, lecture_id, book_id, "translating", user.id)
    await db.commit()

    asyncio.create_task(_do_translate_lecture(lecture_id, book_id, user.raw_token, user.id, user.display_name, ref_id))

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
        if balance and "error" not in balance:
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

    is_running = await is_lecture_running(db, lecture_id)

    result_data = {
        "lecture_id": lecture_id,
        "total": total,
        "translated": translated,
        "completed": translated == total and total > 0,
        "is_running": is_running,
    }
    return JSONResponse(
        content=result_data,
        headers={"Cache-Control": "no-store"},
    )


async def _do_translate_lecture(lecture_id: int, book_id: int, token: str, user_id: str, display_name: str, reference_id: str):
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
                if not lecture.is_published:
                    lecture.is_published = True
                    await db.commit()
                await complete_translation_job(db, lecture_id)
                await set_publication_status(db, lecture_id, book_id, "published", user_id)
                await db.commit()
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

            if not lecture.is_published:
                lecture.is_published = True
                await db.commit()

            await complete_translation_job(db, lecture_id)
            await set_publication_status(db, lecture_id, book_id, "published", user_id)
            await db.commit()

            if user_id:
                await add_contribution(
                    db, user_id, lecture_id,
                    access_type="translate",
                    display_name=display_name,
                    book_id=lecture.book_id,
                    cost=COST_PER_LECTURE,
                    grants_download=True,
                )
                await db.commit()

            logger.info(f"Lecture {lecture_id}: done, {total} sentences translated")
            success = True

    except Exception as e:
        logger.error(f"Lecture {lecture_id}: translation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())

        try:
            async with AsyncSessionLocal() as db:
                await fail_translation_job(db, lecture_id, error=str(e))
                lec_result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
                lecture = lec_result.scalar_one_or_none()
                bid = lecture.book_id if lecture else 0
                await set_publication_status(db, lecture_id, bid, "failed")
                await db.commit()
        except Exception as db_err:
            logger.error(f"Lecture {lecture_id}: failed to update job status: {db_err}")

    finally:
        if token:
            if success:
                settle_result = await settle_credits(
                    token,
                    reserved_amount=COST_PER_LECTURE,
                    actual_amount=COST_PER_LECTURE,
                    reference_id=reference_id,
                    description=f"翻译讲座 {lecture_id} 完成",
                )
                if not settle_result or "error" in settle_result:
                    logger.error(f"Lecture {lecture_id}: settle credits failed: {settle_result}")
            else:
                refund_result = await refund_credits(
                    token,
                    amount=COST_PER_LECTURE,
                    reference_id=reference_id,
                    description=f"翻译讲座 {lecture_id} 失败，退还积分",
                )
                if not refund_result or "error" in refund_result:
                    logger.error(f"Lecture {lecture_id}: refund credits failed: {refund_result}")
