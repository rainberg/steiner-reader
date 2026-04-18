"""Translation service router — triggers async sentence translation."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import Book, TranslationJob
from app.models.schemas import TranslationJobResponse

router = APIRouter(prefix="/api", tags=["translation"])


@router.post("/books/{book_id}/translate", response_model=TranslationJobResponse)
async def trigger_translation(
    book_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Create a translation job for a book. Actual translation runs in background."""
    # Check book exists
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Check for existing pending/running job
    result = await db.execute(
        select(TranslationJob)
        .where(
            TranslationJob.book_id == book_id,
            TranslationJob.status.in_(["pending", "running"]),
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Translation job already {existing.status} (job #{existing.id})"
        )
    
    # Create job (actual work done by background worker)
    job = TranslationJob(
        book_id=book_id,
        status="pending",
    )
    db.add(job)
    await db.commit()
    await db.refresh(job)
    
    return job


@router.get("/jobs/{job_id}", response_model=TranslationJobResponse)
async def get_job_status(
    job_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Check translation job progress."""
    result = await db.execute(select(TranslationJob).where(TranslationJob.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
