import asyncio, sys
sys.path.insert(0, '/opt/steiner-reader/backend')
from app.db.database import async_session
from sqlalchemy import text

async def check():
    async with async_session() as db:
        r = await db.execute(text("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905 AND s.text_zh IS NOT NULL"))
        print(f"translated (NOT NULL): {r.scalar()}")

        r = await db.execute(text("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905 AND s.text_zh IS NOT NULL AND s.text_zh != ''"))
        print(f"translated (NOT NULL AND != ''): {r.scalar()}")

        r = await db.execute(text("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905"))
        print(f"total: {r.scalar()}")

        r = await db.execute(text("SELECT s.id, s.text_zh FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = 6905 AND (s.text_zh IS NULL OR s.text_zh = '') LIMIT 10"))
        rows = r.fetchall()
        print(f"Untranslated/empty rows: {len(rows)}")
        for row in rows:
            print(f"  id={row[0]}, text_zh={repr(row[1])}")

asyncio.run(check())
