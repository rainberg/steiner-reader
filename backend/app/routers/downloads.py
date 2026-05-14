"""Download router — PDF download purchase and delivery."""

import os
import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User, Lecture, Book
from app.routers.auth import require_user, get_current_user
from app.services.credit_service import (
    get_credit_price, atomic_deduct_credits, grant_access, add_contribution,
    check_download_access, get_access_types, get_contributions,
)
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/lectures", tags=["downloads"])


@router.post("/{lecture_id}/purchase-download")
async def purchase_download(
    lecture_id: int,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Purchase PDF download access for a lecture."""
    # Check lecture exists and is published
    lec_result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
    lecture = lec_result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="章节不存在")
    if not lecture.is_published:
        raise HTTPException(status_code=400, detail="译文尚未公开，无法购买下载")

    # Check if user already has access
    if await check_download_access(db, user, lecture_id):
        raise HTTPException(status_code=400, detail="您已拥有下载权限")

    cost = await get_credit_price(db, "download_lecture_pdf")

    try:
        new_credits = await atomic_deduct_credits(
            db, user, cost,
            transaction_type="download_lecture",
            reference_type="lecture",
            reference_id=lecture_id,
            description=f"购买讲座 PDF 下载权限: {lecture.title_de or lecture_id}",
        )
    except ValueError:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：下载需要 {cost} 点，当前余额 {user.credits} 点"
        )

    await grant_access(db, user.id, lecture_id, "download_purchase")
    await add_contribution(db, user.id, lecture_id, "download_purchase")
    await db.commit()

    return {
        "success": True,
        "credits_remaining": new_credits,
        "message": "下载权限已开通，请及时下载文件。本网站不保证长期运行或永久提供访问。",
    }


@router.get("/{lecture_id}/download")
async def download_lecture_pdf(
    lecture_id: int,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Download lecture PDF. Requires download access."""
    # Check lecture exists and find the book's PDF
    result = await db.execute(
        select(Lecture, Book.pdf_filename, Book.title_de)
        .join(Book)
        .where(Lecture.id == lecture_id)
    )
    row = result.one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="章节不存在")

    lecture, pdf_filename, book_title = row

    if not await check_download_access(db, user, lecture_id):
        raise HTTPException(status_code=403, detail="无下载权限，请先贡献翻译或购买下载权限")

    filepath = os.path.join(settings.UPLOAD_DIR, pdf_filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="PDF文件不存在")

    download_name = f"{pdf_filename}"
    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=download_name,
    )


@router.get("/{lecture_id}/download-permission")
async def get_download_permission(
    lecture_id: int,
    user: User | None = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Check if the current user has download access for this lecture."""
    if not user:
        return {"has_permission": False, "access_types": []}

    has_perm = await check_download_access(db, user, lecture_id)
    access_types = await get_access_types(db, user, lecture_id) if has_perm else []

    return {
        "has_permission": has_perm,
        "access_types": access_types,
    }


@router.get("/{lecture_id}/contributions")
async def lecture_contributions(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get contribution records for a lecture."""
    contributions = await get_contributions(db, lecture_id)
    return {"contributions": contributions}
