import pytest
from app.db.models import TranslationPublication, UserTranslationJob


class TestTranslationPublication:
    async def test_create_publication(self, db_session):
        pub = TranslationPublication(
            lecture_id=1,
            status="translating",
            user_id="user-123",
            display_name="Test User",
        )
        db_session.add(pub)
        await db_session.flush()

        assert pub.id is not None
        assert pub.status == "translating"
        assert pub.lecture_id == 1
        assert pub.user_id == "user-123"

    async def test_publication_status_values(self, db_session):
        for i, status in enumerate(("translating", "published", "failed"), start=1):
            pub = TranslationPublication(
                lecture_id=i,
                status=status,
            )
            db_session.add(pub)
            await db_session.flush()
            assert pub.status == status

    async def test_publication_default_status(self, db_session):
        pub = TranslationPublication(lecture_id=1)
        db_session.add(pub)
        await db_session.flush()
        assert pub.status == "translating"


class TestUserTranslationJob:
    async def test_create_job(self, db_session):
        job = UserTranslationJob(
            lecture_id=1,
            user_id="user-123",
            display_name="Test User",
            status="running",
        )
        db_session.add(job)
        await db_session.flush()

        assert job.id is not None
        assert job.status == "running"
        assert job.lecture_id == 1

    async def test_job_status_values(self, db_session):
        for status in ("pending", "running", "completed", "failed"):
            job = UserTranslationJob(
                lecture_id=1,
                status=status,
            )
            db_session.add(job)
            await db_session.flush()
            assert job.status == status

    async def test_job_default_status(self, db_session):
        job = UserTranslationJob(lecture_id=1)
        db_session.add(job)
        await db_session.flush()
        assert job.status == "pending"

    async def test_job_orphan_detection(self, db_session):
        from datetime import datetime, timedelta

        old_job = UserTranslationJob(
            lecture_id=1,
            status="running",
            created_at=datetime.utcnow() - timedelta(minutes=35),
        )
        db_session.add(old_job)
        await db_session.flush()

        from sqlalchemy import select
        threshold = datetime.utcnow() - timedelta(minutes=30)
        result = await db_session.execute(
            select(UserTranslationJob).where(
                UserTranslationJob.status == "running",
                UserTranslationJob.created_at < threshold,
            )
        )
        orphans = result.scalars().all()
        assert len(orphans) == 1
        assert orphans[0].id == old_job.id
