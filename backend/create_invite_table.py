from app.db.database import engine
from app.db.models import Base
import asyncio

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())
print('Tables created')
