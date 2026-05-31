import asyncio, sys
sys.path.insert(0, '/opt/steiner-reader/backend')
from app.db.database import async_session
from sqlalchemy import select, func, text
from app.db.models import Sentence, Paragraph

async def check():
    async with async_session() as db:
        r = await db.execute(text("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905 AND s.text_zh IS NOT NULL"))
        print(f"Direct SQL translated: {r.scalar()}")
        r2 = await db.execute(text("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905"))
        print(f"Direct SQL total: {r2.scalar()}")
        r3 = await db.execute(text("SELECT id, text_de, text_zh FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905 AND s.text_zh IS NULL"))
        rows = r3.fetchall()
        print(f"Untranslated rows: {len(rows)}")
        for row in rows:
            print(f"  id={row[0]}, de={row[1][:60] if row[1] else 'N/A'}, zh={row[2]}")

asyncio.run(check())
