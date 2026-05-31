import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, patch, MagicMock
from sqlalchemy import select

from app.db.models import UserTranslationJob, TranslationPublication
from app.services.translation_service import (
    is_lecture_running,
    start_translation_job,
    complete_translation_job,
    fail_translation_job,
    detect_orphan_jobs,
    get_publication_status,
    set_publication_status,
)


class TestIsLectureRunning:
    async def test_returns_false_when_no_running_job(self, db_session):
        result = await is_lecture_running(db_session, lecture_id=1)
        assert result is False

    async def test_returns_true_when_running_job_exists(self, db_session):
        job = UserTranslationJob(lecture_id=1, book_id=1, user_id="user-1", status="running")
        db_session.add(job)
        await db_session.flush()

        result = await is_lecture_running(db_session, lecture_id=1)
        assert result is True

    async def test_returns_false_when_job_completed(self, db_session):
        job = UserTranslationJob(lecture_id=1, book_id=1, user_id="user-1", status="completed")
        db_session.add(job)
        await db_session.flush()

        result = await is_lecture_running(db_session, lecture_id=1)
        assert result is False


class TestStartTranslationJob:
    async def test_creates_running_job(self, db_session):
        job = await start_translation_job(
            db_session, lecture_id=1, user_id="user-123", book_id=42
        )
        assert job.status == "running"
        assert job.lecture_id == 1
        assert job.user_id == "user-123"
        assert job.book_id == 42

    async def test_raises_if_already_running(self, db_session):
        await start_translation_job(db_session, lecture_id=1, user_id="user-1", book_id=1)
        with pytest.raises(ValueError, match="already has a running"):
            await start_translation_job(db_session, lecture_id=1, user_id="user-2", book_id=1)


class TestCompleteTranslationJob:
    async def test_marks_job_completed(self, db_session):
        await start_translation_job(db_session, lecture_id=1, user_id="user-1", book_id=1)
        completed = await complete_translation_job(db_session, lecture_id=1)
        assert completed.status == "completed"

    async def test_raises_if_no_running_job(self, db_session):
        with pytest.raises(ValueError, match="No running job"):
            await complete_translation_job(db_session, lecture_id=999)


class TestFailTranslationJob:
    async def test_marks_job_failed_with_error(self, db_session):
        await start_translation_job(db_session, lecture_id=1, user_id="user-1", book_id=1)
        failed = await fail_translation_job(db_session, lecture_id=1, error="API timeout")
        assert failed.status == "failed"
        assert failed.error_message == "API timeout"


class TestDetectOrphanJobs:
    async def test_marks_old_running_jobs_as_failed(self, db_session):
        old_job = UserTranslationJob(
            lecture_id=1,
            book_id=1,
            user_id="user-1",
            status="running",
            created_at=datetime.utcnow() - timedelta(minutes=35),
        )
        db_session.add(old_job)
        await db_session.flush()

        count = await detect_orphan_jobs(db_session, timeout_minutes=30)
        assert count == 1

        await db_session.refresh(old_job)
        assert old_job.status == "failed"
        assert "orphan" in old_job.error_message.lower()

    async def test_does_not_mark_recent_jobs(self, db_session):
        recent_job = UserTranslationJob(
            lecture_id=1,
            book_id=1,
            user_id="user-1",
            status="running",
            created_at=datetime.utcnow() - timedelta(minutes=10),
        )
        db_session.add(recent_job)
        await db_session.flush()

        count = await detect_orphan_jobs(db_session, timeout_minutes=30)
        assert count == 0

        await db_session.refresh(recent_job)
        assert recent_job.status == "running"


class TestPublicationStatus:
    async def test_returns_none_when_no_publication(self, db_session):
        status = await get_publication_status(db_session, lecture_id=1)
        assert status is None

    async def test_set_and_get_publication(self, db_session):
        pub = await set_publication_status(
            db_session, lecture_id=1, book_id=1, status="published", user_id="user-123"
        )
        assert pub.status == "published"
        assert pub.published_at is not None

        status = await get_publication_status(db_session, lecture_id=1)
        assert status == "published"

    async def test_update_existing_publication(self, db_session):
        await set_publication_status(db_session, lecture_id=1, book_id=1, status="translating")
        pub = await set_publication_status(db_session, lecture_id=1, book_id=1, status="published")
        assert pub.status == "published"

        from sqlalchemy import select
        result = await db_session.execute(
            select(TranslationPublication).where(TranslationPublication.lecture_id == 1)
        )
        pubs = result.scalars().all()
        assert len(pubs) == 1
