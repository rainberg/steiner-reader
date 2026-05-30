"""Credit service — local price computation + auth-service credit operations.

Price computation uses the local CreditSetting table.
All credit balance mutations (reserve / settle / refund / topup) are delegated
to the auth-service via HTTP API.
Contribution and LectureAccess records are stored in the local database.
"""

import logging
from decimal import Decimal
from typing import Optional

import httpx
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.db.models import CreditSetting, Contribution, LectureAccess

logger = logging.getLogger(__name__)

AUTH_BASE = settings.AUTH_SERVICE_URL


# ---------------------------------------------------------------------------
# Local price computation
# ---------------------------------------------------------------------------

async def compute_price(db: AsyncSession, action: str, **kwargs) -> Decimal:
    """Compute the credit price for *action* from the CreditSetting table.

    Supported actions include e.g. ``translate_per_lecture``,
    ``download_per_lecture``, etc.  Raises ``ValueError`` when no row matches.
    """
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.action == action)
    )
    setting = result.scalar_one_or_none()
    if not setting:
        raise ValueError(f"No credit setting found for action: {action}")
    return Decimal(str(setting.price))


DEFAULT_CREDIT_SETTINGS = [
    {"action": "translate_per_lecture", "price": Decimal("10.00"), "description": "翻译单个讲座"},
    {"action": "download_per_lecture", "price": Decimal("5.00"), "description": "下载单个讲座"},
]


async def seed_default_settings(db: AsyncSession) -> None:
    """Insert default credit settings if they do not exist yet."""
    for item in DEFAULT_CREDIT_SETTINGS:
        result = await db.execute(
            select(CreditSetting).where(CreditSetting.action == item["action"])
        )
        if result.scalar_one_or_none() is None:
            db.add(CreditSetting(**item))
    await db.flush()


# ---------------------------------------------------------------------------
# Auth-service credit operations (httpx)
# ---------------------------------------------------------------------------

async def _call_auth(
    method: str,
    path: str,
    token: str,
    payload: Optional[dict] = None,
) -> dict:
    """Low-level helper: call auth-service and return parsed JSON or error dict."""
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.request(
                method,
                f"{AUTH_BASE}{path}",
                headers={"Authorization": f"Bearer {token}"},
                json=payload,
            )
            if resp.status_code == 200:
                return resp.json()
            try:
                detail = resp.json().get("detail", resp.text)
            except Exception:
                detail = resp.text
            logger.error("Auth-service %s %s returned %s: %s", method, path, resp.status_code, detail)
            return {"error": detail, "status_code": resp.status_code}
        except httpx.HTTPError as exc:
            logger.error("Auth-service %s %s request failed: %s", method, path, exc)
            return {"error": str(exc)}


async def get_balance(token: str) -> dict:
    """Query credit balance from auth-service.

    Returns ``{"user_id": ..., "credits": "100.00", "credits_reserved": "10.00"}``
    on success, or ``{"error": ...}`` on failure.
    """
    return await _call_auth("GET", "/api/credits/balance", token)


async def reserve_credits(
    token: str,
    amount: Decimal,
    reference_id: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Reserve (freeze) credits via auth-service.

    Returns ``{"success": true, "credits": ..., "credits_reserved": ..., "log_id": ...}``
    on success.  ``status_code`` 400 means insufficient balance; 409 means
    *reference_id* already exists.
    """
    payload: dict = {"amount": str(amount)}
    if reference_id is not None:
        payload["reference_id"] = reference_id
    if description is not None:
        payload["description"] = description
    return await _call_auth("POST", "/api/credits/reserve", token, payload)


async def settle_credits(
    token: str,
    reserved_amount: Decimal,
    actual_amount: Decimal,
    reference_id: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Settle previously reserved credits via auth-service.

    If *actual_amount* < *reserved_amount* the difference is refunded.
    Returns ``{"success": true, "credits": ..., "credits_reserved": ..., "refund": ..., "log_id": ...}``.
    """
    payload: dict = {
        "reserved_amount": str(reserved_amount),
        "actual_amount": str(actual_amount),
    }
    if reference_id is not None:
        payload["reference_id"] = reference_id
    if description is not None:
        payload["description"] = description
    return await _call_auth("POST", "/api/credits/settle", token, payload)


async def refund_credits(
    token: str,
    amount: Decimal,
    reference_id: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Refund credits via auth-service.

    Returns ``{"success": true, "credits": ..., "credits_reserved": ..., "log_id": ...}``.
    """
    payload: dict = {"amount": str(amount)}
    if reference_id is not None:
        payload["reference_id"] = reference_id
    if description is not None:
        payload["description"] = description
    return await _call_auth("POST", "/api/credits/refund", token, payload)


async def topup_credits(
    token: str,
    amount: Decimal,
    description: Optional[str] = None,
) -> dict:
    """Top-up (add) credits via auth-service.

    Returns ``{"success": true, "credits": ..., "credits_reserved": ..., "log_id": ...}``.
    """
    payload: dict = {"amount": str(amount)}
    if description is not None:
        payload["description"] = description
    return await _call_auth("POST", "/api/credits/topup", token, payload)


# ---------------------------------------------------------------------------
# Composite operations
# ---------------------------------------------------------------------------

async def atomic_deduct_credits(
    token: str,
    amount: Decimal,
    reference_id: Optional[str] = None,
    description: Optional[str] = None,
) -> dict:
    """Deduct credits atomically: reserve then immediately settle.

    This is the equivalent of the old local ``atomic_deduct_credits`` but
    delegates to auth-service reserve + settle.  If reserve succeeds but
    settle fails, the reserved credits remain frozen (not lost) and can be
    settled or refunded later.
    """
    reserve_result = await reserve_credits(token, amount, reference_id, description)
    if "error" in reserve_result:
        return reserve_result

    settle_result = await settle_credits(
        token,
        reserved_amount=amount,
        actual_amount=amount,
        reference_id=reference_id,
        description=description,
    )
    if "error" in settle_result:
        logger.warning(
            "Reserve succeeded but settle failed for ref=%s — credits remain reserved",
            reference_id,
        )
        return settle_result

    return settle_result


async def atomic_add_credits(
    token: str,
    amount: Decimal,
    description: Optional[str] = None,
) -> dict:
    """Add credits via auth-service topup.

    Replaces the old local ``atomic_add_credits``.
    """
    return await topup_credits(token, amount, description)


# ---------------------------------------------------------------------------
# Local DB: Contribution & LectureAccess
# ---------------------------------------------------------------------------

async def add_contribution(
    db: AsyncSession,
    user_id: str,
    lecture_id: int,
    amount: Decimal,
    access_type: str = "translate",
    display_name: str = "",
    book_id: int | None = None,
    cost: int = 0,
    grants_download: bool = False,
) -> Contribution:
    """Record a credit contribution for a user on a lecture."""
    entry = Contribution(
        user_id=user_id,
        lecture_id=lecture_id,
        contribution_type=access_type,
        display_name=display_name or None,
        book_id=book_id,
        cost=cost,
        grants_download=grants_download,
    )
    db.add(entry)
    await db.flush()
    return entry


async def grant_access(
    db: AsyncSession,
    user_id: str,
    lecture_id: int,
    access_type: str = "translate",
) -> LectureAccess:
    """Grant a user access to a lecture.  If access already exists, return it."""
    result = await db.execute(
        select(LectureAccess).where(
            LectureAccess.user_id == user_id,
            LectureAccess.lecture_id == lecture_id,
            LectureAccess.access_type == access_type,
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        return existing

    entry = LectureAccess(
        user_id=user_id,
        lecture_id=lecture_id,
        access_type=access_type,
    )
    db.add(entry)
    await db.flush()
    return entry


async def check_download_access(
    db: AsyncSession,
    user_id: str,
    lecture_id: int,
) -> bool:
    """Return True if the user has download access to the lecture."""
    result = await db.execute(
        select(LectureAccess).where(
            LectureAccess.user_id == user_id,
            LectureAccess.lecture_id == lecture_id,
            LectureAccess.access_type == "download",
        )
    )
    return result.scalar_one_or_none() is not None


async def get_access_types(
    db: AsyncSession,
    user_id: str,
    lecture_id: int,
) -> list[str]:
    """Return all access types the user has for a lecture."""
    result = await db.execute(
        select(LectureAccess.access_type).where(
            LectureAccess.user_id == user_id,
            LectureAccess.lecture_id == lecture_id,
        )
    )
    return [row[0] for row in result.all()]


async def get_contributions(
    db: AsyncSession,
    lecture_id: int,
) -> list[dict]:
    """Return all contributions for a lecture, newest first."""
    result = await db.execute(
        select(Contribution)
        .where(Contribution.lecture_id == lecture_id)
        .order_by(Contribution.created_at.desc())
    )
    rows = result.scalars().all()
    return [
        {
            "user_id": str(r.user_id),
            "display_name": r.display_name or "",
            "contribution_type": r.contribution_type,
            "cost": r.cost,
            "grants_download": r.grants_download,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
