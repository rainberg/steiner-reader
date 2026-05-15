#!/usr/bin/env python3
"""Re-translate untranslated sentences in GA312."""
import asyncio, sys, os
os.chdir('/opt/steiner-reader/backend')
sys.path.insert(0, '/opt/steiner-reader/backend')

from app.db.models import Lecture, Paragraph, Sentence
from app.db.database import async_session
from app.services.translator import translate_lecture_sentences
from sqlalchemy import select
from sqlalchemy.orm import selectinload

async def main():
    async with async_session() as db:
        result = await db.execute(
            select(Lecture).where(Lecture.book_id == 258)
            .options(selectinload(Lecture.paragraphs).selectinload(Paragraph.sentences))
        )
        lectures = result.scalars().all()
        total_done = 0
        total_sents = 0

        for lec in lectures:
            untranslated = []
            sent_map = {}
            for p in lec.paragraphs:
                for s in p.sentences:
                    total_sents += 1
                    if not s.text_zh:
                        untranslated.append(s.text_de)
                        sent_map[len(untranslated) - 1] = s
                    else:
                        total_done += 1

            if not untranslated:
                print(f'Lect {lec.id}: OK ({total_sents} sents)')
                continue

            print(f'Lect {lec.id}: {len(untranslated)} to translate...')
            BATCH = 20
            for i in range(0, len(untranslated), BATCH):
                batch = untranslated[i:i + BATCH]
                try:
                    translated = await translate_lecture_sentences(batch)
                    for j, zh in enumerate(translated):
                        idx = i + j
                        if idx in sent_map:
                            sent_map[idx].text_zh = zh
                    await db.commit()
                    print(f'  Batch {i}-{i+len(batch)}', flush=True)
                except Exception as e:
                    print(f'  Batch {i} ERROR: {e}', flush=True)

            lec.is_published = True
            await db.commit()
            total_done += len(untranslated)
            print(f'Lect {lec.id}: DONE', flush=True)

        print(f'\nTotal: {total_done}/{total_sents} translated', flush=True)

if __name__ == '__main__':
    asyncio.run(main())
