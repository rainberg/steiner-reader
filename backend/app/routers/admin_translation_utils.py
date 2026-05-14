"""Translation utilities for admin re-translation."""

import logging
from typing import Optional, List, Dict
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.models import Lecture, Paragraph, Sentence
from app.services.translator import translate_lecture_sentences

logger = logging.getLogger(__name__)


async def get_lecture_sentences(
    db: AsyncSession, 
    lecture_id: int, 
    clear_existing: bool = False
) -> tuple[List[Sentence], List[str]]:
    """Get sentences for translation, optionally clearing existing translations.
    
    Returns:
        tuple: (list_of_sentence_objects, list_of_german_texts)
    """
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
        raise ValueError(f"Lecture {lecture_id} not found")
    
    sentences = []
    german_texts = []
    
    for para in lecture.paragraphs:
        for sent in para.sentences:
            # If clear_existing is True, clear the existing translation
            if clear_existing:
                sent.text_zh = None
            
            # Only include if no translation exists
            if not sent.text_zh:
                sentences.append(sent)
                german_texts.append(sent.text_de)
    
    return sentences, german_texts


async def translate_sentences_batch(
    sentences: List[Sentence],
    german_texts: List[str]
) -> int:
    """Translate a batch of sentences and update the database."""
    if not german_texts:
        return 0
    
    logger.info(f"Translating {len(german_texts)} sentences...")
    translated_texts = await translate_lecture_sentences(german_texts)
    
    count = 0
    for i, sentence in enumerate(sentences):
        if i < len(translated_texts):
            sentence.text_zh = translated_texts[i]
            count += 1
        else:
            # If translation returns fewer items than input (shouldn't happen with individual translation)
            logger.warning(f"Translation result missing for sentence {sentence.id}")
    
    logger.info(f"Translated {count} sentences")
    return count


async def admin_retranslate_lecture(
    db: AsyncSession,
    lecture_id: int,
    clear_existing: bool = True,
    force_all: bool = False
) -> Dict:
    """Admin-only function to re-translate a lecture.
    
    Args:
        db: Database session
        lecture_id: ID of lecture to translate
        clear_existing: If True, clear existing translations before translating
        force_all: If True, translate all sentences (even those already translated)
    
    Returns:
        Dict with translation results
    """
    # Get sentence counts
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0
    
    if force_all or clear_existing:
        # If forcing all, we want to translate everything
        sentences, german_texts = await get_lecture_sentences(db, lecture_id, clear_existing=True)
        untranslated_count = total
    else:
        # Only translate untranslated sentences
        sentences, german_texts = await get_lecture_sentences(db, lecture_id, clear_existing=False)
        untranslated_count = len(german_texts)
    
    # Get count of already translated sentences
    already_translated = total - untranslated_count
    
    if untranslated_count == 0:
        return {
            "lecture_id": lecture_id,
            "total": total,
            "translated": already_translated,
            "newly_translated": 0,
            "message": "No sentences need translation",
            "action_taken": "none"
        }
    
    # Do the translation
    newly_translated = await translate_sentences_batch(sentences, german_texts)
    
    # Commit changes
    await db.commit()
    
    return {
        "lecture_id": lecture_id,
        "total": total,
        "already_translated": already_translated,
        "newly_translated": newly_translated,
        "now_translated": already_translated + newly_translated,
        "message": f"Translated {newly_translated} sentences",
        "action_taken": "retranslate_all" if force_all else "translate_untranslated",
        "cleared_existing": clear_existing
    }