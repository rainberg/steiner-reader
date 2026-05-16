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

COEFFICIENTS = {
    "translate_coefficient": settings.CREDIT_TRANSLATE_COEFFICIENT,
    "edit_translation_coefficient": settings.CREDIT_EDIT_TRANSLATION_COEFFICIENT,
    "edit_source_coefficient": settings.CREDIT_EDIT_SOURCE_COEFFICIENT,
    "download_lecture_price": settings.CREDIT_DOWNLOAD_LECTURE_PRICE,
    "download_book_price": settings.CREDIT_DOWNLOAD_BOOK_PRICE,
}

DEFAULT_DESCRIPTIONS = {
    "translate_coefficient": "翻译系数 (每句点数)",
    "edit_translation_coefficient": "编辑译文系数 (每句点数)",
    "edit_source_coefficient": "编辑原文系数 (每句点数)",
    "download_lecture_price": "单章下载",
    "download_book_price": "全书下载",
}


async def get_credit_price(db: AsyncSession, key: str) -> int:
    """Read manual price override from credit_settings. Returns 0 if not set
    (meaning use coefficient calculation instead)."""
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == key)
    )
    row = result.scalar_one_or_none()
    if row and row.value is not None:
        return row.value
    return 0  # 0 means "not manually set, use coefficient"


async def get_coefficient(db: AsyncSession, key: str) -> float:
    """Get pricing coefficient from credit_settings or config default."""
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == key)
    )
    row = result.scalar_one_or_none()
    if row and row.value is not None:
        return float(row.value)
    return COEFFICIENTS.get(key, 1.0)


async def compute_price(db: AsyncSession, key: str, sentence_count: int = 1) -> int:
    """Compute price: manual override if set, otherwise coefficient × sentence_count.
    For download keys, return the manual price or 0 directly.
    """
    # Check manual override
    manual = await get_credit_price(db, key)
    if manual > 0:
        return manual

    # Coefficient-based calculation
    if key in ("translate_lecture", "translate_book", "translate_coefficient"):
        coeff = await get_coefficient(db, "translate_coefficient")
        return max(1, int(sentence_count * coeff))
    elif key in ("edit_translation_sentence", "edit_translation_coefficient"):
        coeff = await get_coefficient(db, "edit_translation_coefficient")
        return max(0, int(coeff))
    elif key in ("edit_source_sentence", "edit_source_coefficient"):
        coeff = await get_coefficient(db, "edit_source_coefficient")
        return max(0, int(coeff))
    elif key in ("download_lecture_pdf", "download_lecture_price"):
        return manual  # 0 = free
    elif key in ("download_book_pdf", "download_book_price"):
        return manual  # 0 = free

    # Fallback: try as coefficient
    coeff = await get_coefficient(db, key)
    return max(1, int(sentence_count * coeff))


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
    """Return deduplicated list of {username, contribution_type, credits, created_at}."""
    from sqlalchemy import func as sa_func
    result = await db.execute(
        select(
            Contribution.user_id,
            User.username,
            Contribution.contribution_type,
            sa_func.count(Contribution.id).label("count"),
            sa_func.min(Contribution.created_at).label("first_at"),
        )
        .join(User, Contribution.user_id == User.id)
        .where(Contribution.lecture_id == lecture_id)
        .group_by(Contribution.user_id, User.username, Contribution.contribution_type)
        .order_by(sa_func.min(Contribution.created_at))
    )
    rows = result.all()
    return [
        {
            "username": username,
            "contribution_type": cont_type,
            "count": count,
            "created_at": first_at,
        }
        for uid, username, cont_type, count, first_at in rows
    ]


async def seed_default_settings(db: AsyncSession):
    """Insert default credit coefficients if the table is empty."""
    result = await db.execute(select(CreditSetting).limit(1))
    if result.scalar_one_or_none():
        return  # already seeded

    for key, value in COEFFICIENTS.items():
        db.add(CreditSetting(
            key=key,
            value=int(value) if isinstance(value, float) and value == int(value) else value,
            description=DEFAULT_DESCRIPTIONS.get(key, ""),
        ))
    await db.commit()
    logger.info("Seeded default credit coefficients")


async def apply_translation_fixes(text: str, db: AsyncSession = None) -> str:
    """Apply all enabled translation fixes to text. If no db, returns unchanged."""
    if not text or not db:
        return text
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == "translation_fixes_loaded")
    )
    if not result.scalar_one_or_none():
        return text
    from app.db.models import TranslationFix
    fixes_result = await db.execute(
        select(TranslationFix).where(TranslationFix.enabled == True).order_by(TranslationFix.id)
    )
    for fix in fixes_result.scalars().all():
        text = text.replace(fix.pattern, fix.replacement)
    return text
