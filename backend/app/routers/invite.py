import secrets
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import InviteCode, CreditSetting
from app.models.schemas import (
    InviteCodeResponse,
    MyInviteCodesResponse,
    GenerateInviteCodeResponse,
    RedeemInviteCodeRequest,
    RedeemInviteCodeResponse,
)
from app.routers.auth import AuthUser, require_user, require_admin
from app.routers.recharge import _add_credits_via_auth

router = APIRouter(prefix="/api/invite", tags=["invite"])


def _generate_invite_code() -> str:
    """Generate a random invite code in format INV-XXXX-XXXX."""
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    raw = "".join(secrets.choice(chars) for _ in range(8))
    return f"INV-{raw[:4]}-{raw[4:]}"


async def _get_invite_setting(db: AsyncSession, action: str, default: int) -> int:
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.action == action)
    )
    row = result.scalar_one_or_none()
    return int(row.price) if row else default


@router.post("/generate", response_model=GenerateInviteCodeResponse)
async def generate_invite_code(
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    quota = await _get_invite_setting(db, "invite_codes_per_user", 3)
    credits = await _get_invite_setting(db, "invite_credits", 50)

    count_result = await db.execute(
        select(func.count()).select_from(InviteCode).where(InviteCode.owner_id == user.id)
    )
    used_quota = count_result.scalar() or 0

    if used_quota >= quota:
        raise HTTPException(status_code=400, detail="邀请码配额已用完")

    for _attempt in range(10):
        code = _generate_invite_code()
        exists = await db.execute(
            select(InviteCode).where(InviteCode.code == code)
        )
        if exists.scalar_one_or_none() is None:
            break
    else:
        raise HTTPException(status_code=500, detail="生成唯一邀请码失败，请重试")

    db.add(InviteCode(
        code=code,
        owner_id=user.id,
        credits=credits,
        status="active",
    ))
    await db.commit()

    return GenerateInviteCodeResponse(
        code=code,
        credits=credits,
        remaining_quota=quota - used_quota - 1,
    )


@router.get("/my-codes", response_model=MyInviteCodesResponse)
async def my_invite_codes(
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    quota = await _get_invite_setting(db, "invite_codes_per_user", 3)

    count_result = await db.execute(
        select(func.count()).select_from(InviteCode).where(InviteCode.owner_id == user.id)
    )
    used_quota = count_result.scalar() or 0

    result = await db.execute(
        select(InviteCode)
        .where(InviteCode.owner_id == user.id)
        .order_by(InviteCode.id.desc())
    )
    codes = [InviteCodeResponse.model_validate(row) for row in result.scalars().all()]

    return MyInviteCodesResponse(
        quota=quota,
        used=used_quota,
        remaining=quota - used_quota,
        codes=codes,
    )


@router.post("/redeem", response_model=RedeemInviteCodeResponse)
async def redeem_invite_code(
    req: RedeemInviteCodeRequest,
    user: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Redeem an invite code for a new user. Called by auth-service after registration."""
    code = req.invite_code.strip().upper()

    result = await db.execute(
        select(InviteCode).where(InviteCode.code == code).with_for_update()
    )
    invite_code = result.scalar_one_or_none()

    if not invite_code:
        raise HTTPException(status_code=404, detail="邀请码不存在")

    if invite_code.status == "used":
        raise HTTPException(status_code=400, detail="邀请码已被使用")

    invite_code.status = "used"
    invite_code.used_by = req.new_user_id
    invite_code.used_at = datetime.utcnow()

    try:
        await _add_credits_via_auth(req.new_user_id, invite_code.credits, user.raw_token)
    except HTTPException:
        invite_code.status = "active"
        invite_code.used_by = None
        invite_code.used_at = None
        await db.commit()
        raise

    await db.commit()

    return RedeemInviteCodeResponse(
        success=True,
        credits_added=invite_code.credits,
        message=f"邀请码兑换成功，获得 {invite_code.credits} 积分",
    )


@router.get("/admin/codes")
async def list_invite_codes(
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    query = select(InviteCode)
    count_query = select(func.count()).select_from(InviteCode)

    if status and status != "all":
        query = query.where(InviteCode.status == status)
        count_query = count_query.where(InviteCode.status == status)

    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0

    offset = (page - 1) * page_size
    query = query.order_by(InviteCode.id.desc()).offset(offset).limit(page_size)

    result = await db.execute(query)
    items = [InviteCodeResponse.model_validate(row) for row in result.scalars().all()]

    return {"total": total, "page": page, "page_size": page_size, "items": items}
