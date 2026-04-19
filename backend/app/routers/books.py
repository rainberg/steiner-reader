"""Books API router."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Book, Lecture, Paragraph, Sentence
from app.models.schemas import BookResponse, BookDetail, LectureResponse, LectureSummary, LectureListItem

router = APIRouter(prefix="/api/books", tags=["books"])


@router.get("", response_model=list[BookResponse])
async def list_books(db: AsyncSession = Depends(get_db)):
    """Get all books with lecture summaries (lightweight — no sentence data)."""
    result = await db.execute(
        select(Book)
        .options(selectinload(Book.lectures))
        .order_by(Book.created_at.desc())
    )
    books = result.scalars().all()

    response = []
    for book in books:
        lecture_summaries = []
        for lec in sorted(book.lectures, key=lambda l: l.order_index):
            # Count sentences efficiently
            stmt = (
                select(func.count(Sentence.id))
                .select_from(Sentence)
                .join(Paragraph)
                .where(Paragraph.lecture_id == lec.id)
            )
            count_result = await db.execute(stmt)
            sentence_count = count_result.scalar() or 0

            lecture_summaries.append(LectureSummary(
                id=lec.id,
                title_de=lec.title_de,
                lecture_date=lec.lecture_date,
                location=lec.location,
                order_index=lec.order_index,
                sentence_count=sentence_count,
            ))

        response.append(BookResponse(
            id=book.id,
            ga_number=book.ga_number,
            title_de=book.title_de,
            title_zh=book.title_zh,
            pdf_filename=book.pdf_filename,
            cover_url=book.cover_url,
            created_at=book.created_at,
            lectures=lecture_summaries,
        ))

    return response


@router.get("/{book_id}", response_model=BookDetail)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """Get book detail with lectures and translation counts (no sentence data — use /lectures/{id} for reading)."""
    # Get book with lectures
    result = await db.execute(
        select(Book)
        .where(Book.id == book_id)
        .options(selectinload(Book.lectures))
    )
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Get sentence counts per lecture efficiently
    lectures_items = []
    for lec in sorted(book.lectures, key=lambda l: l.order_index):
        total_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lec.id)
        )
        total = total_result.scalar() or 0

        translated_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lec.id, Sentence.text_zh.isnot(None))
        )
        translated = translated_result.scalar() or 0

        lectures_items.append(LectureListItem(
            id=lec.id,
            book_id=book.id,
            title_de=lec.title_de,
            lecture_date=lec.lecture_date,
            location=lec.location,
            order_index=lec.order_index,
            sentence_count=total,
            translated_count=translated,
        ))

    return BookDetail(
        id=book.id,
        ga_number=book.ga_number,
        title_de=book.title_de,
        title_zh=book.title_zh,
        pdf_filename=book.pdf_filename,
        cover_url=book.cover_url,
        created_at=book.created_at,
        lectures=lectures_items,
    )


@router.get("/{book_id}/lectures/{lecture_id}", response_model=LectureResponse)
async def get_lecture(
    book_id: int,
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get a specific lecture with all paragraphs and sentences (for reader page)."""
    result = await db.execute(
        select(Lecture)
        .where(Lecture.id == lecture_id, Lecture.book_id == book_id)
        .options(
            selectinload(Lecture.paragraphs)
            .selectinload(Paragraph.sentences)
        )
    )
    lecture = result.scalar_one_or_none()

    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

    return lecture
