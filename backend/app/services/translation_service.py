from datetime import datetime, timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import UserTranslationJob, TranslationPublication


async def is_lecture_running(db: AsyncSession, lecture_id: int) -> bool:
    result = await db.execute(
        select(UserTranslationJob)
        .where(UserTranslationJob.lecture_id == lecture_id)
        .where(UserTranslationJob.status == "running")
    )
    return result.scalar_one_or_none() is not None


async def start_translation_job(
    db: AsyncSession,
    lecture_id: int,
    user_id: str,
    book_id: int,
    mode: str = "simulate",
) -> UserTranslationJob:
    if await is_lecture_running(db, lecture_id):
        raise ValueError(f"Lecture {lecture_id} already has a running job")

    job = UserTranslationJob(
        lecture_id=lecture_id,
        user_id=user_id,
        book_id=book_id,
        mode=mode,
        status="running",
    )
    db.add(job)
    await db.flush()
    return job


async def complete_translation_job(db: AsyncSession, lecture_id: int) -> UserTranslationJob:
    result = await db.execute(
        select(UserTranslationJob)
        .where(UserTranslationJob.lecture_id == lecture_id)
        .where(UserTranslationJob.status == "running")
    )
    job = result.scalar_one_or_none()
    if not job:
        raise ValueError(f"No running job for lecture {lecture_id}")
    job.status = "completed"
    await db.flush()
    return job


async def fail_translation_job(
    db: AsyncSession, lecture_id: int, error: str = ""
) -> UserTranslationJob:
    result = await db.execute(
        select(UserTranslationJob)
        .where(UserTranslationJob.lecture_id == lecture_id)
        .where(UserTranslationJob.status == "running")
    )
    job = result.scalar_one_or_none()
    if not job:
        raise ValueError(f"No running job for lecture {lecture_id}")
    job.status = "failed"
    job.error_message = error
    await db.flush()
    return job


async def detect_orphan_jobs(db: AsyncSession, timeout_minutes: int = 30) -> int:
    threshold = datetime.utcnow() - timedelta(minutes=timeout_minutes)
    result = await db.execute(
        select(UserTranslationJob)
        .where(UserTranslationJob.status == "running")
        .where(UserTranslationJob.created_at < threshold)
    )
    orphans = result.scalars().all()
    count = 0
    for job in orphans:
        job.status = "failed"
        job.error_message = f"Orphan job: running for over {timeout_minutes} minutes"
        count += 1
    if count:
        await db.flush()
    return count


async def get_publication_status(db: AsyncSession, lecture_id: int) -> str | None:
    result = await db.execute(
        select(TranslationPublication)
        .where(TranslationPublication.lecture_id == lecture_id)
    )
    pub = result.scalar_one_or_none()
    return pub.status if pub else None


async def set_publication_status(
    db: AsyncSession,
    lecture_id: int,
    book_id: int,
    status: str,
    user_id: str | None = None,
) -> TranslationPublication:
    result = await db.execute(
        select(TranslationPublication)
        .where(TranslationPublication.lecture_id == lecture_id)
    )
    pub = result.scalar_one_or_none()
    if pub:
        pub.status = status
        if status == "published":
            pub.published_at = datetime.utcnow()
        if user_id and not pub.first_contributor_user_id:
            pub.first_contributor_user_id = user_id
    else:
        pub = TranslationPublication(
            lecture_id=lecture_id,
            book_id=book_id,
            status=status,
            first_contributor_user_id=user_id,
            published_at=datetime.utcnow() if status == "published" else None,
        )
        db.add(pub)
    await db.flush()
    return pub
