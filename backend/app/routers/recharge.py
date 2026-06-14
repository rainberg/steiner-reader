"""Recharge router — user submits application, admin reviews and approves."""

import hashlib
import os
import secrets
import uuid
import logging
from datetime import datetime
import httpx
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import RechargeCode, RechargeRequest, CreditSetting
from app.models.schemas import (
    GenerateCodesRequest,
    GenerateCodesResponse,
    RechargeCodeResponse,
    RechargeCodeList,
    RedeemCodeRequest,
    RedeemCodeResponse,
)
from app.routers.auth import AuthUser, require_user, require_admin
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/recharge", tags=["recharge"])

AUTH_BASE = settings.AUTH_SERVICE_URL

RECHARGE_DIR = "/opt/steiner-reader/images/recharge"
PAYMENT_QR_PATH = "/opt/steiner-reader/images/recharge/payment_qr.png"

try:
    os.makedirs(RECHARGE_DIR, exist_ok=True)
except PermissionError:
    pass


async def _add_credits_via_auth(user_id: str, amount: int, token: str) -> dict:
    async with httpx.AsyncClient(timeout=15) as client:
        try:
            resp = await client.post(
                f"{AUTH_BASE}/api/credits/topup",
                headers={"Authorization": f"Bearer {token}"},
                json={"amount": amount, "description": "充值码兑换"},
            )
            if resp.status_code == 200:
                return resp.json()
            try:
                detail = resp.json().get("detail", resp.text)
            except Exception:
                detail = resp.text
            logger.error("Auth-service add-credits failed for %s: %s", user_id, detail)
            raise HTTPException(status_code=resp.status_code, detail=f"Auth Service 错误: {detail}")
        except httpx.HTTPError as exc:
            logger.error("Auth-service add-credits request failed: %s", exc)
            raise HTTPException(status_code=502, detail=f"Auth Service 不可用: {exc}")


def _generate_code() -> str:
    """Generate a random recharge code in format XXXX-XXXX-XXXX."""
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    raw = "".join(secrets.choice(chars) for _ in range(12))
    return f"{raw[:4]}-{raw[4:8]}-{raw[8:]}"


class RechargeSubmitRequest(BaseModel):
    amount: int


class RechargeReviewRequest(BaseModel):
    status: str
    admin_note: str | None = None


@router.get("/info")
async def recharge_info(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.action == "recharge_coefficient")
    )
    row = result.scalar_one_or_none()
    coefficient = int(row.price) if row else 10
    return {
        "coefficient": coefficient,
        "description": f"1元 = {coefficient}积分",
        "examples": [
            {"yuan": 1, "credits": 1 * coefficient},
            {"yuan": 10, "credits": 10 * coefficient},
            {"yuan": 50, "credits": 50 * coefficient},
        ],
    }


@router.post("/submit")
async def submit_recharge(
    amount: int = Form(...),
    payment_image: UploadFile = File(...),
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="充值金额必须大于0元")

    if not payment_image.content_type or not payment_image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="请上传图片文件")

    coeff_result = await db.execute(
        select(CreditSetting).where(CreditSetting.action == "recharge_coefficient")
    )
    coeff_row = coeff_result.scalar_one_or_none()
    coefficient = int(coeff_row.price) if coeff_row else 10

    ext = os.path.splitext(payment_image.filename or "proof.png")[1] or ".png"
    filename = f"recharge_{user.id}_{uuid.uuid4().hex[:8]}{ext}"
    filepath = os.path.join(RECHARGE_DIR, filename)

    content = await payment_image.read()
    file_hash = hashlib.sha256(content).hexdigest()

    dup_result = await db.execute(
        select(RechargeRequest).where(
            RechargeRequest.user_id == user.id,
            RechargeRequest.image_hash == file_hash,
            RechargeRequest.status == "pending",
        ).order_by(RechargeRequest.created_at.desc()).limit(1)
    )
    dup_req = dup_result.scalar_one_or_none()
    if dup_req:
        raise HTTPException(
            status_code=409,
            detail="请勿重复提交，该凭证已有待审核的申请"
        )

    with open(filepath, "wb") as f:
        f.write(content)

    req = RechargeRequest(
        user_id=user.id,
        amount=amount,
        coefficient=coefficient,
        payment_image=filename,
        image_hash=file_hash,
        status="pending",
    )
    db.add(req)
    await db.commit()
    await db.refresh(req)

    credits = amount * coefficient
    return {
        "success": True,
        "message": f"充值申请已提交，审核通过后将获得 {credits} 积分",
        "id": req.id,
        "amount": req.amount,
        "coefficient": coefficient,
        "credits": credits,
        "status": req.status,
    }


@router.get("/my-requests")
async def my_recharge_requests(
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(RechargeRequest)
        .where(RechargeRequest.user_id == user.id)
        .order_by(RechargeRequest.created_at.desc())
        .limit(50)
    )
    requests = result.scalars().all()
    return [
        {
            "id": r.id,
            "amount": r.amount,
            "coefficient": r.coefficient or 10,
            "credits": r.amount * (r.coefficient or 10),
            "status": r.status,
            "admin_note": r.admin_note,
            "created_at": r.created_at.isoformat() if r.created_at else None,
            "updated_at": r.updated_at.isoformat() if r.updated_at else None,
        }
        for r in requests
    ]


@router.post("/admin/upload-qr")
async def upload_payment_qr(
    qr_image: UploadFile = File(...),
    admin: AuthUser = Depends(require_admin),
):
    content = await qr_image.read()
    with open(PAYMENT_QR_PATH, "wb") as f:
        f.write(content)
    return {"success": True, "message": "收款码已更新"}


@router.get("/admin/pending-requests")
async def admin_pending_requests(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(RechargeRequest)
        .order_by(
            RechargeRequest.status == "pending",
            RechargeRequest.created_at.desc()
        )
        .limit(200)
    )
    rows = result.scalars().all()

    user_ids = list(set(r.user_id for r in rows))
    user_map: dict[str, str] = {}
    if user_ids:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                for uid in user_ids:
                    try:
                        resp = await client.get(
                            f"{AUTH_BASE}/api/admin/users",
                            headers={"Authorization": f"Bearer {admin.raw_token}"},
                            params={"search": uid},
                        )
                        if resp.status_code == 200:
                            data = resp.json()
                            u_list = data if isinstance(data, list) else data.get("users", data.get("items", []))
                            for u in u_list:
                                if str(u.get("id")) == str(uid):
                                    user_map[uid] = u.get("display_name") or u.get("username") or u.get("email", "")
                                    break
                    except Exception:
                        pass
        except Exception:
            pass

    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "username": user_map.get(r.user_id, ""),
            "amount": r.amount,
            "coefficient": r.coefficient,
            "credits": r.amount * (r.coefficient or 10),
            "payment_image": r.payment_image,
            "status": r.status,
            "admin_note": r.admin_note,
            "created_at": r.created_at.isoformat() if r.created_at else None,
            "updated_at": r.updated_at.isoformat() if r.updated_at else None,
        }
        for r in rows
    ]


@router.post("/admin/review/{request_id}")
async def admin_review_request(
    request_id: int,
    review: RechargeReviewRequest,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(RechargeRequest)
        .where(RechargeRequest.id == request_id)
    )
    req = result.scalar_one_or_none()
    if not req:
        raise HTTPException(status_code=404, detail="申请不存在")

    if req.status != "pending":
        raise HTTPException(status_code=400, detail="该申请已处理过")

    if review.status not in ("approved", "rejected"):
        raise HTTPException(status_code=400, detail="状态值无效，应为 approved 或 rejected")

    req.status = review.status
    req.admin_note = review.admin_note

    if review.status == "approved":
        credits = req.amount * (req.coefficient or 10)
        try:
            auth_result = await _add_credits_via_auth(req.user_id, credits, admin.raw_token)
        except HTTPException:
            req.status = "pending"
            req.admin_note = None
            await db.commit()
            raise

        await db.commit()
        return {
            "success": True,
            "message": f"已批准，用户充值 {req.amount} 元获得 {credits} 积分",
            "amount_yuan": req.amount,
            "coefficient": req.coefficient,
            "credits_added": credits,
            "auth_result": auth_result,
        }
    else:
        await db.commit()
        return {
            "success": True,
            "message": f"已拒绝充值申请 #{req.id}",
        }


@router.get("/payment-qr")
async def get_payment_qr():
    if not os.path.exists(PAYMENT_QR_PATH):
        raise HTTPException(status_code=404, detail="收款码未设置")
    return FileResponse(PAYMENT_QR_PATH, media_type="image/png")


@router.post("/admin/generate-codes", response_model=GenerateCodesResponse)
async def generate_recharge_codes(
    req: GenerateCodesRequest,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    if req.credits <= 0:
        raise HTTPException(status_code=400, detail="积分值必须大于0")
    if req.count < 1 or req.count > 100:
        raise HTTPException(status_code=400, detail="生成数量需在1-100之间")

    batch_id = uuid.uuid4().hex
    codes = []

    for _ in range(req.count):
        for _attempt in range(10):
            code = _generate_code()
            exists = await db.execute(
                select(RechargeCode).where(RechargeCode.code == code)
            )
            if exists.scalar_one_or_none() is None:
                break
        else:
            raise HTTPException(status_code=500, detail="生成唯一充值码失败，请重试")

        db.add(RechargeCode(
            code=code,
            credits=req.credits,
            expires_at=req.expires_at,
            created_by=admin.id,
            status="active",
            batch_id=batch_id,
        ))
        codes.append(code)

    await db.commit()
    return GenerateCodesResponse(
        batch_id=batch_id,
        codes=codes,
        count=len(codes),
        credits_per_code=req.credits,
    )


@router.get("/admin/codes", response_model=RechargeCodeList)
async def list_recharge_codes(
    status: str | None = Query(None),
    batch_id: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    query = select(RechargeCode)
    count_query = select(func.count()).select_from(RechargeCode)

    if status and status != "all":
        query = query.where(RechargeCode.status == status)
        count_query = count_query.where(RechargeCode.status == status)
    if batch_id:
        query = query.where(RechargeCode.batch_id == batch_id)
        count_query = count_query.where(RechargeCode.batch_id == batch_id)

    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0

    offset = (page - 1) * page_size
    query = query.order_by(RechargeCode.id.desc()).offset(offset).limit(page_size)

    result = await db.execute(query)
    items = [RechargeCodeResponse.model_validate(row) for row in result.scalars().all()]

    return RechargeCodeList(total=total, page=page, page_size=page_size, items=items)


@router.post("/redeem", response_model=RedeemCodeResponse)
async def redeem_recharge_code(
    req: RedeemCodeRequest,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    code = req.code.strip().upper()

    result = await db.execute(
        select(RechargeCode)
        .where(RechargeCode.code == code)
        .with_for_update()
    )
    recharge_code = result.scalar_one_or_none()

    if not recharge_code:
        raise HTTPException(status_code=404, detail="充值码不存在")

    if recharge_code.status == "used":
        raise HTTPException(status_code=400, detail="充值码已被使用")

    if recharge_code.status == "expired":
        raise HTTPException(status_code=400, detail="充值码已过期")

    if recharge_code.expires_at and recharge_code.expires_at < datetime.utcnow():
        recharge_code.status = "expired"
        await db.commit()
        raise HTTPException(status_code=400, detail="充值码已过期")

    recharge_code.status = "used"
    recharge_code.used_by = user.id
    recharge_code.used_at = datetime.utcnow()

    try:
        await _add_credits_via_auth(user.id, recharge_code.credits, user.raw_token)
    except HTTPException:
        recharge_code.status = "active"
        recharge_code.used_by = None
        recharge_code.used_at = None
        await db.commit()
        raise

    await db.commit()

    return RedeemCodeResponse(
        success=True,
        credits_added=recharge_code.credits,
        message=f"充值码兑换成功，获得 {recharge_code.credits} 积分",
    )


@router.get("/payment-proof/{filename}")
async def get_payment_proof(filename: str):
    filepath = os.path.join(RECHARGE_DIR, filename)
    if not os.path.exists(filepath) or ".." in filename:
        raise HTTPException(status_code=404, detail="文件不存在")
    return FileResponse(filepath)
