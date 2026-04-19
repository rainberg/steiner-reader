"""Translation service router — per-lecture sentence translation."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Lecture, Paragraph, Sentence
from app.services.translator import translate_lecture_sentences

router = APIRouter(prefix="/api", tags=["translation"])


@router.post("/lectures/{lecture_id}/translate")
async def translate_lecture(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Translate all un-translated sentences in a lecture (chapter)."""
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
        raise HTTPException(status_code=404, detail="Lecture not found")
    
    # Collect un-translated sentences
    untranslated = []
    sentence_map = {}  # index -> Sentence object
    
    for para in lecture.paragraphs:
        for sent in para.sentences:
            if not sent.text_zh:
                idx = len(untranslated)
                untranslated.append(sent.text_de)
                sentence_map[idx] = sent
    
    if not untranslated:
        return {
            "lecture_id": lecture_id,
            "message": "All sentences already translated",
            "translated": 0,
            "total": sum(len(p.sentences) for p in lecture.paragraphs),
        }
    
    # Translate in batches
    translated_texts = await translate_lecture_sentences(untranslated)
    
    # Update sentences in DB
    count = 0
    for idx, zh_text in enumerate(translated_texts):
        if idx in sentence_map:
            sentence_map[idx].text_zh = zh_text
            count += 1
    
    await db.commit()
    
    total = sum(len(p.sentences) for p in lecture.paragraphs)
    
    return {
        "lecture_id": lecture_id,
        "message": f"Translated {count} sentences",
        "translated": count,
        "total": total,
    }
