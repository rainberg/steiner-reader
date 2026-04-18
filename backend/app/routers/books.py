"""Books API router."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Book, Lecture, Paragraph, Sentence
from app.models.schemas import BookResponse, BookDetail, LectureResponse, LectureSummary

router = APIRouter(prefix="/api/books", tags=["books"])


@router.get("", response_model=list[BookResponse])
async def list_books(db: AsyncSession = Depends(get_db)):
    """Get all books with lecture summaries."""
    result = await db.execute(
        select(Book)
        .options(selectinload(Book.lectures))
        .order_by(Book.created_at.desc())
    )
    books = result.scalars().all()
    
    response = []
    for book in books:
        # Count sentences per lecture
        lecture_summaries = []
        for lec in sorted(book.lectures, key=lambda l: l.order_index):
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
    """Get book detail with all lectures, paragraphs, sentences."""
    result = await db.execute(
        select(Book)
        .where(Book.id == book_id)
        .options(
            selectinload(Book.lectures)
            .selectinload(Lecture.paragraphs)
            .selectinload(Paragraph.sentences)
        )
    )
    book = result.scalar_one_or_none()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


@router.get("/{book_id}/lectures/{lecture_id}", response_model=LectureResponse)
async def get_lecture(
    book_id: int,
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get a specific lecture with all paragraphs and sentences."""
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
