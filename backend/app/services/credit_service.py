"""Credit operations: atomic deduction, transaction logging, access checks."""

import logging
from sqlalchemy import select, update, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import (
    CreditSetting, CreditTransaction, Contribution,
    LectureAccess, User
)
from app.config import settings

logger = logging.getLogger(__name__)

DEFAULT_PRICES = {
    "translate_lecture": settings.CREDIT_TRANSLATE_LECTURE,
    "translate_book": settings.CREDIT_TRANSLATE_BOOK,
    "edit_translation_sentence": settings.CREDIT_EDIT_TRANSLATION_SENTENCE,
    "edit_source_sentence": settings.CREDIT_EDIT_SOURCE_SENTENCE,
    "download_lecture_pdf": settings.CREDIT_DOWNLOAD_LECTURE_PDF,
    "download_book_pdf": settings.CREDIT_DOWNLOAD_BOOK_PDF,
}

DEFAULT_DESCRIPTIONS = {
    "translate_lecture": "翻译单章 (每次)",
    "translate_book": "翻译全书 (每次)",
    "edit_translation_sentence": "编辑译文 (每次)",
    "edit_source_sentence": "编辑原文 (每次)",
    "download_lecture_pdf": "单章PDF下载权限",
    "download_book_pdf": "全书PDF下载权限",
}


async def get_credit_price(db: AsyncSession, key: str) -> int:
    """Read price from credit_settings table, or fall back to config default."""
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == key)
    )
    row = result.scalar_one_or_none()
    if row:
        return row.value
    return DEFAULT_PRICES.get(key, 10)


async def atomic_deduct_credits(
    db: AsyncSession,
    user: User,
    amount: int,
    transaction_type: str,
    reference_type: str = None,
    reference_id: int = None,
    description: str = None,
) -> int:
    """Atomically deduct credits. Returns new balance. Raises ValueError if insufficient."""
    if amount <= 0:
        raise ValueError("Deduction amount must be positive")

    result = await db.execute(
        text(
            "UPDATE users SET credits = credits - :amount "
            "WHERE id = :uid AND credits >= :amount "
            "RETURNING credits"
        ),
        {"amount": amount, "uid": user.id},
    )
    row = result.fetchone()
    if row is None:
        raise ValueError("点数不足")

    new_credits = row[0]
    user.credits = new_credits  # sync the ORM object

    # Log transaction
    txn = CreditTransaction(
        user_id=user.id,
        amount=-amount,
        balance_after=new_credits,
        transaction_type=transaction_type,
        reference_type=reference_type,
        reference_id=reference_id,
        description=description,
    )
    db.add(txn)
    return new_credits


async def atomic_add_credits(
    db: AsyncSession,
    user_id: int,
    amount: int,
    transaction_type: str,
    reference_type: str = None,
    reference_id: int = None,
    description: str = None,
) -> int:
    """Atomically add credits. Returns new balance."""
    if amount <= 0:
        raise ValueError("Add amount must be positive")

    result = await db.execute(
        text(
            "UPDATE users SET credits = credits + :amount "
            "WHERE id = :uid "
            "RETURNING credits"
        ),
        {"amount": amount, "uid": user_id},
    )
    row = result.fetchone()
    if row is None:
        raise ValueError("User not found")

    new_credits = row[0]

    txn = CreditTransaction(
        user_id=user_id,
        amount=amount,
        balance_after=new_credits,
        transaction_type=transaction_type,
        reference_type=reference_type,
        reference_id=reference_id,
        description=description,
    )
    db.add(txn)
    return new_credits


async def check_download_access(db: AsyncSession, user: User, lecture_id: int) -> bool:
    """True if user is admin or has a lecture_access row for this lecture."""
    if user.is_admin:
        return True
    result = await db.execute(
        select(LectureAccess).where(
            LectureAccess.user_id == user.id,
            LectureAccess.lecture_id == lecture_id,
        )
    )
    return result.scalar_one_or_none() is not None


async def get_access_types(db: AsyncSession, user: User, lecture_id: int) -> list[str]:
    """Return list of access_type strings for the given user and lecture."""
    if user.is_admin:
        return ["admin"]
    result = await db.execute(
        select(LectureAccess.access_type).where(
            LectureAccess.user_id == user.id,
            LectureAccess.lecture_id == lecture_id,
        )
    )
    return [row[0] for row in result.all()]


async def grant_access(db: AsyncSession, user_id: int, lecture_id: int, access_type: str):
    """Grant download access. Idempotent — ignores duplicates."""
    existing = await db.execute(
        select(LectureAccess).where(
            LectureAccess.user_id == user_id,
            LectureAccess.lecture_id == lecture_id,
            LectureAccess.access_type == access_type,
        )
    )
    if existing.scalar_one_or_none():
        return
    db.add(LectureAccess(user_id=user_id, lecture_id=lecture_id, access_type=access_type))


async def add_contribution(db: AsyncSession, user_id: int, lecture_id: int, contribution_type: str):
    """Record a contribution record."""
    db.add(Contribution(
        user_id=user_id,
        lecture_id=lecture_id,
        contribution_type=contribution_type,
    ))


async def get_contributions(db: AsyncSession, lecture_id: int) -> list[dict]:
    """Return list of {username, contribution_type, created_at} for a lecture."""
    result = await db.execute(
        select(Contribution, User.username)
        .join(User, Contribution.user_id == User.id)
        .where(Contribution.lecture_id == lecture_id)
        .order_by(Contribution.created_at)
    )
    rows = result.all()
    return [
        {
            "username": username,
            "contribution_type": row.contribution_type,
            "created_at": row.created_at,
        }
        for row, username in rows
    ]


async def seed_default_settings(db: AsyncSession):
    """Insert default credit settings if the table is empty."""
    result = await db.execute(select(CreditSetting).limit(1))
    if result.scalar_one_or_none():
        return  # already seeded

    for key, value in DEFAULT_PRICES.items():
        db.add(CreditSetting(
            key=key,
            value=value,
            description=DEFAULT_DESCRIPTIONS.get(key, ""),
        ))
    await db.commit()
    logger.info("Seeded default credit settings")
