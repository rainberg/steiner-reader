"""FastAPI application entry point."""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, func

from app.config import settings
from contextlib import asynccontextmanager

from app.routers import books, translate, images, auth, admin, lectures, paragraphs
from app.routers import downloads, edits, upload, recharge, search
from app.db.database import async_session, get_db
from app.db.models import CreditTransaction
from app.routers.auth import require_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: seed default credit settings, clear stale translation flags."""
    async with async_session() as db:
        from app.services.credit_service import seed_default_settings
        await seed_default_settings(db)
        # Reset translation flags stuck from server restart/crash
        from sqlalchemy import update
        from app.db.models import Lecture
        await db.execute(
            update(Lecture).where(Lecture.is_translating == True)
            .values(is_translating=False, translate_progress=0, translate_total=0)
        )
        await db.commit()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description="Platform for reading and translating Rudolf Steiner's works (GA series)",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS — allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(books.router)
app.include_router(translate.router)
app.include_router(images.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(lectures.router)
app.include_router(paragraphs.router)
app.include_router(downloads.router)
app.include_router(edits.router)
app.include_router(upload.router)
app.include_router(recharge.router)
app.include_router(search.router)


@app.get("/")
async def root():
    return {"app": settings.APP_NAME, "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# User credit transaction history
@app.get("/api/users/{user_id}/transactions")
async def user_transactions(
    user_id: int,
    page: int = 1,
    limit: int = 50,
    db=Depends(get_db),
    current_user=Depends(require_user),
):
    """Get credit transaction history for a user. Must be the user or admin."""
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="无权查看他人交易记录")

    offset = (page - 1) * limit
    result = await db.execute(
        select(CreditTransaction)
        .where(CreditTransaction.user_id == user_id)
        .order_by(CreditTransaction.created_at.desc())
        .offset(offset)
        .limit(min(limit, 100))
    )
    rows = result.scalars().all()
    total_result = await db.execute(
        select(func.count(CreditTransaction.id))
        .where(CreditTransaction.user_id == user_id)
    )
    total = total_result.scalar() or 0
    return {
        "transactions": [
            {
                "id": r.id, "user_id": r.user_id, "amount": r.amount,
                "balance_after": r.balance_after, "transaction_type": r.transaction_type,
                "reference_type": r.reference_type, "reference_id": r.reference_id,
                "description": r.description, "created_at": str(r.created_at),
            }
            for r in rows
        ],
        "total": total,
    }
