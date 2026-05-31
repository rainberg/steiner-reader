"""Fix orphan translation: translate remaining 4 sentences for lecture 6905."""
import asyncio
import sys
sys.path.insert(0, '/opt/steiner-reader/backend')

from app.db.database import async_session
from sqlalchemy import select
from app.db.models import Sentence, Paragraph
from app.services.translator import translate_lecture_sentences


async def fix_lecture(lecture_id: int):
    async with async_session() as db:
        result = await db.execute(
            select(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.is_(None))
        )
        untranslated = result.scalars().all()

        if not untranslated:
            print("No untranslated sentences found!")
            return

        print(f"Found {len(untranslated)} untranslated sentences")

        texts_de = [s.text_de for s in untranslated]
        print("Translating...")
        translations = await translate_lecture_sentences(texts_de)

        for sent, zh in zip(untranslated, translations):
            sent.text_zh = zh
            print(f"  {sent.text_de[:60]} -> {zh[:60]}")

        await db.commit()
        print("Done! All sentences translated.")

        # Verify
        from sqlalchemy import func
        total_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id)
        )
        translated_result = await db.execute(
            select(func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
        )
        total = total_result.scalar()
        translated = translated_result.scalar()
        print(f"Final status: translated={translated}, total={total}, completed={translated == total}")


if __name__ == '__main__':
    asyncio.run(fix_lecture(6905))
