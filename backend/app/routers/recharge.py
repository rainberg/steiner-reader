"""Recharge router — user submits application, admin reviews and approves."""

import hashlib
import os
import uuid
import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User, RechargeRequest, CreditTransaction, CreditSetting
from app.routers.auth import require_user, require_admin
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/recharge", tags=["recharge"])

# Payment proof upload directory
RECHARGE_DIR = "/opt/steiner-reader/images/recharge"
PAYMENT_QR_PATH = "/opt/steiner-reader/images/recharge/payment_qr.png"

# Ensure directory exists (ignore error outside production)
try:
    os.makedirs(RECHARGE_DIR, exist_ok=True)
except PermissionError:
    pass


# ── Schemas ────────────────────────────────────────────────────

class RechargeSubmitRequest(BaseModel):
    amount: int


class RechargeRequestResponse(BaseModel):
    id: int
    user_id: int
    username: str = ""
    amount: int
    payment_image: str | None = None
    status: str
    admin_note: str | None = None
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class RechargeReviewRequest(BaseModel):
    status: str  # "approved" or "rejected"
    admin_note: str | None = None


# ── User Endpoints ─────────────────────────────────────────────

@router.get("/info")
async def recharge_info(db: AsyncSession = Depends(get_db)):
    """Get recharge coefficient and conversion info."""
    result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == "recharge_coefficient")
    )
    row = result.scalar_one_or_none()
    coefficient = row.value if row else 10
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
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Submit a recharge application. amount is in RMB yuan. Credits = amount × coefficient."""
    if amount <= 0:
        raise HTTPException(status_code=400, detail="充值金额必须大于0元")

    if not payment_image.content_type or not payment_image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="请上传图片文件")

    # Get current coefficient
    coeff_result = await db.execute(
        select(CreditSetting).where(CreditSetting.key == "recharge_coefficient")
    )
    coeff_row = coeff_result.scalar_one_or_none()
    coefficient = coeff_row.value if coeff_row else 10

    # Save payment proof
    ext = os.path.splitext(payment_image.filename or "proof.png")[1] or ".png"
    filename = f"recharge_{user.id}_{uuid.uuid4().hex[:8]}{ext}"
    filepath = os.path.join(RECHARGE_DIR, filename)

    content = await payment_image.read()
    file_hash = hashlib.sha256(content).hexdigest()

    # Check for duplicate submission by same user
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
            detail=f"该凭证已于 {dup_req.created_at.strftime('%m月%d日 %H:%M')} 提交（{dup_req.amount}元），请修改已有申请或等待审核"
        )

    with open(filepath, "wb") as f:
        f.write(content)

    # Create request with coefficient snapshot
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
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Get current user's recharge request history."""
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
            "status": r.status,
            "admin_note": r.admin_note,
            "created_at": r.created_at,
            "updated_at": r.updated_at,
        }
        for r in requests
    ]


# ── Admin Endpoints ────────────────────────────────────────────

@router.post("/admin/upload-qr")
async def upload_payment_qr(
    qr_image: UploadFile = File(...),
    admin: User = Depends(require_admin),
):
    """Admin uploads payment QR code for users to scan."""
    content = await qr_image.read()
    with open(PAYMENT_QR_PATH, "wb") as f:
        f.write(content)
    return {"success": True, "message": "收款码已更新"}


@router.get("/admin/pending-requests")
async def admin_pending_requests(
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Get all recharge requests for admin review. Optional status filter."""
    result = await db.execute(
        select(RechargeRequest, User.username)
        .join(User, RechargeRequest.user_id == User.id)
        .order_by(
            RechargeRequest.status == "pending",
            RechargeRequest.created_at.desc()
        )
        .limit(200)
    )
    rows = result.all()
    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "username": username,
            "amount": r.amount,
            "coefficient": r.coefficient,
            "credits": r.amount * (r.coefficient or 10),
            "payment_image": r.payment_image,
            "status": r.status,
            "admin_note": r.admin_note,
            "created_at": r.created_at,
            "updated_at": r.updated_at,
        }
        for r, username in rows
    ]


@router.post("/admin/review/{request_id}")
async def admin_review_request(
    request_id: int,
    review: RechargeReviewRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Admin approves or rejects a recharge request. Adds credits on approval."""
    result = await db.execute(
        select(RechargeRequest, User)
        .join(User, RechargeRequest.user_id == User.id)
        .where(RechargeRequest.id == request_id)
    )
    row = result.one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="申请不存在")

    req, user = row
    if req.status != "pending":
        raise HTTPException(status_code=400, detail="该申请已处理过")

    if review.status not in ("approved", "rejected"):
        raise HTTPException(status_code=400, detail="状态值无效，应为 approved 或 rejected")

    req.status = review.status
    req.admin_note = review.admin_note

    if review.status == "approved":
        credits = req.amount * (req.coefficient or 10)
        old_credits = user.credits
        user.credits += credits

        # Log transaction
        db.add(CreditTransaction(
            user_id=user.id,
            amount=credits,
            balance_after=user.credits,
            transaction_type="recharge_approved",
            reference_type="recharge_request",
            reference_id=req.id,
            description=f"充值申请 #{req.id} 审核通过，{req.amount}元×{req.coefficient or 10}={credits}积分",
        ))

        await db.commit()
        return {
            "success": True,
            "message": f"已批准，用户 {user.username} 充值 {req.amount} 元获得 {credits} 积分 (余额 {user.credits})",
            "old_credits": old_credits,
            "new_credits": user.credits,
            "amount_yuan": req.amount,
            "coefficient": req.coefficient,
            "credits_added": credits,
        }
    else:
        await db.commit()
        return {
            "success": True,
            "message": f"已拒绝充值申请 #{req.id}",
        }


# ── Image Serving ──────────────────────────────────────────────

@router.get("/payment-qr")
async def get_payment_qr():
    """Serve the admin-uploaded payment QR code."""
    if not os.path.exists(PAYMENT_QR_PATH):
        raise HTTPException(status_code=404, detail="收款码未设置")
    return FileResponse(PAYMENT_QR_PATH, media_type="image/png")


@router.get("/payment-proof/{filename}")
async def get_payment_proof(
    filename: str,
    admin: User = Depends(require_admin),
):
    """Serve a payment proof image (admin only)."""
    filepath = os.path.join(RECHARGE_DIR, filename)
    if not os.path.exists(filepath) or ".." in filename:
        raise HTTPException(status_code=404, detail="文件不存在")
    return FileResponse(filepath)
