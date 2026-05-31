"""Resume orphan translation tasks after backend restart."""
import asyncio
import sys
sys.path.insert(0, '/opt/steiner-reader/backend')

from app.db.database import async_session
from sqlalchemy import select, func
from app.db.models import Sentence, Paragraph


async def check_lecture(lecture_id: int):
    async with async_session() as db:
        total_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id)
        )
        total = total_result.scalar() or 0

        translated_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
        )
        translated = translated_result.scalar() or 0

        print(f"Lecture {lecture_id}: translated={translated}, total={total}, completed={translated == total and total > 0}")

        # Find untranslated sentences
        result = await db.execute(
            select(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.is_(None))
            .limit(10)
        )
        untranslated = result.scalars().all()
        for s in untranslated:
            print(f"  Untranslated sentence {s.id}: {s.text_de[:80] if s.text_de else 'N/A'}...")


if __name__ == '__main__':
    asyncio.run(check_lecture(6905))
