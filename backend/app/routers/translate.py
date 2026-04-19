"""Translation service router — per-lecture sentence translation."""

import asyncio
import logging
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import selectinload

from app.db.database import async_session as AsyncSessionLocal, get_db
from app.db.models import Lecture, Paragraph, Sentence
from app.services.translator import translate_lecture_sentences

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["translation"])


async def _do_translate_lecture(lecture_id: int):
    """Background task: translate all un-translated sentences in a lecture."""
    async with AsyncSessionLocal() as db:
        # Fetch lecture with paragraphs and sentences
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

        # Collect un-translated sentences
        untranslated = []
        sentence_map = {}

        for para in lecture.paragraphs:
            for sent in para.sentences:
                if not sent.text_zh:
                    idx = len(untranslated)
                    untranslated.append(sent.text_de)
                    sentence_map[idx] = sent

        if not untranslated:
            logger.info(f"Lecture {lecture_id}: already fully translated")
            return

        logger.info(f"Lecture {lecture_id}: translating {len(untranslated)} sentences...")

        # Translate in batches
        translated_texts = await translate_lecture_sentences(untranslated)

        # Update sentences in DB
        count = 0
        for idx, zh_text in enumerate(translated_texts):
            if idx in sentence_map:
                sentence_map[idx].text_zh = zh_text
                count += 1

        await db.commit()
        logger.info(f"Lecture {lecture_id}: done, {count} sentences translated")


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    """Start translating a lecture (runs in background)."""
    # Verify lecture exists
    result = await db.execute(
        select(Lecture).where(Lecture.id == lecture_id)
    )
    lecture = result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

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
        }

    # Start background translation
    background_tasks.add_task(_do_translate_lecture, lecture_id)

    return {
        "lecture_id": lecture_id,
        "status": "started",
        "message": f"Translation started: {remaining} sentences to translate",
        "translated": translated,
        "total": total,
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
