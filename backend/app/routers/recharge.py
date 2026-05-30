"""Recharge router — user submits application, admin reviews and approves."""

import hashlib
import os
import uuid
import logging
from datetime import datetime
import httpx
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import RechargeRequest, CreditSetting
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
                f"{AUTH_BASE}/api/admin/users/{user_id}/add-credits",
                headers={"Authorization": f"Bearer {token}"},
                json={"credits": amount, "remark": "充值审核通过"},
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
            "created_at": r.created_at,
            "updated_at": r.updated_at,
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


@router.get("/payment-proof/{filename}")
async def get_payment_proof(filename: str):
    filepath = os.path.join(RECHARGE_DIR, filename)
    if not os.path.exists(filepath) or ".." in filename:
        raise HTTPException(status_code=404, detail="文件不存在")
    return FileResponse(filepath)
