"""Paragraphs API router."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Paragraph, Sentence
from app.models.schemas import SentenceResponse

router = APIRouter(prefix="/api/paragraphs", tags=["paragraphs"])


@router.get("/{paragraph_id}/sentences")
async def get_paragraph_sentences(
    paragraph_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get all sentences for a paragraph, ordered by order_index."""
    result = await db.execute(
        select(Sentence)
        .where(Sentence.paragraph_id == paragraph_id)
        .order_by(Sentence.order_index)
    )
    sentences = result.scalars().all()
    return [
        SentenceResponse(
            id=s.id,
            text_de=s.text_de,
            text_zh=s.text_zh,
            order_index=s.order_index,
            content_de=s.text_de,
            content_zh=s.text_zh,
            paragraph_id=paragraph_id,
            sentence_index=s.order_index,
            is_heading=False,
        )
        for s in sentences
    ]
