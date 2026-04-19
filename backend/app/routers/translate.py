"""Translation service router — per-lecture sentence translation."""

import asyncio
import logging
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import selectinload

from app.db.database import async_session as AsyncSessionLocal, get_db
from app.db.models import Lecture, Paragraph, Sentence, User
from app.routers.auth import require_user, get_current_user
from app.services.translator import translate_lecture_sentences

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["translation"])

COST_PER_LECTURE = 10  # Credits per lecture translation


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    background_tasks: BackgroundTasks,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Start translating a lecture (costs credits, runs in background)."""
    # Get current counts
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
            "credits": user.credits,
        }

    # Check if user has enough credits
    if user.credits < COST_PER_LECTURE:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：翻译需要 {COST_PER_LECTURE} 点，当前余额 {user.credits} 点"
        )

    # Deduct credits
    user.credits -= COST_PER_LECTURE
    await db.commit()

    # Start background translation
    background_tasks.add_task(_do_translate_lecture, lecture_id)

    return {
        "lecture_id": lecture_id,
        "status": "started",
        "message": f"Translation started (消耗 {COST_PER_LECTURE} 点)",
        "translated": translated,
        "total": total,
        "credits": user.credits,
        "cost": COST_PER_LECTURE,
    }


@router.get("/lectures/{lecture_id}/translation-cost")
async def get_translation_cost(
    lecture_id: int,
    user: User | None = Depends(get_current_user),
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

    return {
        "lecture_id": lecture_id,
        "total": total,
        "translated": translated,
        "remaining": total - translated,
        "cost": COST_PER_LECTURE if total > translated else 0,
        "already_translated": total > 0 and translated == total,
        "user_credits": user.credits if user else None,
        "can_afford": user.credits >= COST_PER_LECTURE if user else None,
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
    """Background task: translate all un-translated sentences in a lecture."""
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
            return

        logger.info(f"Lecture {lecture_id}: translating {len(untranslated)} sentences...")
        translated_texts = await translate_lecture_sentences(untranslated)

        count = 0
        for idx, zh_text in enumerate(translated_texts):
            if idx in sentence_map:
                sentence_map[idx].text_zh = zh_text
                count += 1

        await db.commit()
        logger.info(f"Lecture {lecture_id}: done, {count} sentences translated")
