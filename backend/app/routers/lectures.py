"""Lectures API router — endpoints for reading lecture content."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Lecture, Paragraph, Sentence
from sqlalchemy import select
from app.models.schemas import ParagraphResponse, SentenceResponse

router = APIRouter(prefix="/api/lectures", tags=["lectures"])


def _build_paragraph_response(para, image_map=None, is_published: bool = True) -> ParagraphResponse:
    """Build a ParagraphResponse with all frontend fields populated.
    When is_published is False, all text_zh / content_zh are set to None.
    """
    if image_map is None:
        image_map = {}
    sentences = [
        SentenceResponse(
            id=s.id,
            text_de=s.text_de,
            text_zh=(s.text_zh if is_published else None),
            order_index=s.order_index,
            content_de=s.text_de,
            content_zh=(s.text_zh if is_published else None),
            paragraph_id=para.id,
            sentence_index=s.order_index,
            is_heading=False,
            image_url=image_map.get(s.id),
        )
        for s in para.sentences
    ]
    content_de = " ".join(s.text_de for s in para.sentences) if para.sentences else ""
    content_zh = (
        " ".join(s.text_zh for s in para.sentences if s.text_zh)
        if para.sentences and is_published else None
    )
    return ParagraphResponse(
        id=para.id,
        order_index=para.order_index,
        content_de=content_de,
        content_zh=content_zh,
        lecture_id=para.lecture_id,
        paragraph_index=para.order_index,
        sentences=sentences,
    )


@router.get("/{lecture_id}/paragraphs")
async def get_lecture_paragraphs(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get all paragraphs for a lecture, ordered by order_index, with sentences eager loaded."""
    # Check publication status
    lec_result = await db.execute(
        select(Lecture.is_published).where(Lecture.id == lecture_id)
    )
    is_published = lec_result.scalar() or False

    result = await db.execute(
        select(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
        .options(selectinload(Paragraph.sentences))
        .order_by(Paragraph.order_index)
    )
    paragraphs = result.scalars().all()

    # 查询图片映射，动态获取 ga_number
    from sqlalchemy import text as sa_text
    img_sql = "SELECT li.after_sentence_id, li.filename, b.ga_number "
    img_sql += "FROM lecture_images li "
    img_sql += "JOIN lectures l ON li.lecture_id = l.id "
    img_sql += "JOIN books b ON l.book_id = b.id "
    img_sql += "WHERE li.lecture_id = :lid"
    img_result = await db.execute(
        sa_text(img_sql),
        {"lid": lecture_id}
    )
    image_map = {}
    for row in img_result:
        if row[0]:
            ga = row[2] if row[2] else "GA279"
            image_map[row[0]] = f"/api/images/{ga}/{row[1]}"

    return [_build_paragraph_response(p, image_map, is_published) for p in paragraphs]


@router.get("/{lecture_id}", response_model=dict)
async def get_lecture_simple(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get basic lecture info without paragraphs."""
    result = await db.execute(
        select(Lecture).where(Lecture.id == lecture_id)
    )
    lecture = result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return {
        "id": lecture.id,
        "book_id": lecture.book_id,
        "order_index": lecture.order_index,
        "title_de": lecture.title_de,
        "title_zh": lecture.title_zh,
        "lecture_date": str(lecture.lecture_date) if lecture.lecture_date else None,
        "location": lecture.location,
        "is_published": lecture.is_published,
    }
