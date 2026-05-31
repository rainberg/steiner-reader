"""Download router — PDF download purchase and bilingual lecture delivery."""

import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Lecture, Book, Paragraph, Sentence
from app.routers.auth import AuthUser, require_user, get_current_user
from app.services.credit_service import (
    compute_price, atomic_deduct_credits, grant_access, add_contribution,
    check_download_access, get_access_types, get_contributions,
)
from app.services.pdf_generator import generate_bilingual_pdf
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/lectures", tags=["downloads"])


@router.post("/{lecture_id}/purchase-download")
async def purchase_download(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
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
    if await check_download_access(db, user.id, lecture_id):
        raise HTTPException(status_code=400, detail="您已拥有下载权限")

    cost = await compute_price(db, "download_lecture_price", 0)

    deduct_result = await atomic_deduct_credits(
        user.raw_token, cost,
        reference_id=f"download-lecture-{lecture_id}-{uuid.uuid4().hex[:8]}",
        description=f"购买讲座 PDF 下载权限: {lecture.title_de or lecture_id}",
    )
    if "error" in deduct_result:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：下载需要 {cost} 点"
        )

    await grant_access(db, user.id, lecture_id, "download_purchase")
    await add_contribution(
        db, user.id, lecture_id,
        access_type="download_purchase",
        display_name=user.display_name,
        book_id=lecture.book_id,
        cost=int(cost),
        grants_download=True,
    )
    await db.commit()

    return {
        "success": True,
        "credits_remaining": deduct_result.get("credits", 0),
        "message": "下载权限已开通，请及时下载文件。本网站不保证长期运行或永久提供访问。",
    }


@router.get("/{lecture_id}/download")
async def download_lecture_bilingual(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Download bilingual (DE+ZH) lecture content as HTML. Requires download access."""
    # Check lecture exists and load with paragraphs+sentences
    result = await db.execute(
        select(Lecture)
        .where(Lecture.id == lecture_id)
        .options(
            selectinload(Lecture.paragraphs)
            .selectinload(Paragraph.sentences)
        )
    )
    lecture = result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="章节不存在")

    if not await check_download_access(db, user.id, lecture_id):
        raise HTTPException(status_code=403, detail="无下载权限，请先贡献翻译或购买下载权限")

    # Build bilingual HTML
    title = lecture.title_de or f"Lecture {lecture_id}"
    title_zh = lecture.title_zh or ""

    sentences_html = ""
    for pi, para in enumerate(lecture.paragraphs):
        for si, sent in enumerate(sorted(para.sentences, key=lambda s: s.order_index)):
            de = (sent.text_de or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            zh = (sent.text_zh or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            zh_display = zh if zh else '<span class="untranslated">（未翻译）</span>'
            sentences_html += f"""
            <div class="sentence">
              <div class="de">{pi+1}.{si+1} {de}</div>
              <div class="zh">{zh_display}</div>
            </div>"""

    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>{title} — 中德双语</title>
<style>
  body {{ font-family: "Noto Serif", "Noto Serif SC", Georgia, serif; max-width: 800px; margin: 0 auto; padding: 2em 1.5em; background: #fff; color: #1a1a1a; }}
  h1 {{ font-size: 1.4em; color: #1e3a5f; border-bottom: 2px solid #1e3a5f; padding-bottom: 0.4em; margin-bottom: 0.2em; }}
  h2 {{ font-size: 1em; color: #666; font-weight: normal; margin-top: 0; margin-bottom: 1.5em; }}
  .sentence {{ margin-bottom: 0.8em; border-left: 3px solid #e5e7eb; padding-left: 1em; }}
  .de {{ font-size: 0.95em; line-height: 1.7; color: #1e293b; }}
  .zh {{ font-size: 0.9em; line-height: 1.7; color: #64748b; margin-top: 0.15em; }}
  .untranslated {{ font-style: italic; color: #94a3b8; }}
  .meta {{ font-size: 0.75em; color: #94a3b8; margin-bottom: 2em; }}
  .notice {{ font-size: 0.7em; color: #cbd5e1; text-align: center; margin-top: 3em; }}
</style>
</head>
<body>
<h1>{title}</h1>
<h2>{title_zh}</h2>
<div class="meta">
  {lecture.location or ""}{" — " if lecture.location and lecture.lecture_date else ""}{str(lecture.lecture_date) if lecture.lecture_date else ""}
  &nbsp;·&nbsp; {sum(1 for p in lecture.paragraphs for _ in p.sentences)} 句
</div>
{sentences_html}
<div class="notice">Generated by Steiner Reader — 仅供个人学习使用</div>
</body>
</html>"""

    safe_title = "".join(c for c in title[:40] if c.isalnum() or c in " _-").strip()
    return HTMLResponse(
        content=html,
        status_code=200,
        media_type="text/html; charset=utf-8",
        headers={
            "Content-Disposition": f"attachment; filename*=UTF-8''{safe_title}.html",
        },
    )


@router.get("/{lecture_id}/download-pdf")
async def download_lecture_pdf(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Download bilingual (DE+ZH) lecture content as PDF. Requires download access."""
    result = await db.execute(
        select(Lecture)
        .where(Lecture.id == lecture_id)
        .options(
            selectinload(Lecture.paragraphs)
            .selectinload(Paragraph.sentences)
        )
    )
    lecture = result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(status_code=404, detail="章节不存在")

    if not await check_download_access(db, user.id, lecture_id):
        raise HTTPException(status_code=403, detail="无下载权限，请先贡献翻译或购买下载权限")

    lecture_data = {
        "title_de": lecture.title_de or f"Lecture {lecture_id}",
        "title_zh": lecture.title_zh or "",
        "location": lecture.location or "",
        "lecture_date": str(lecture.lecture_date) if lecture.lecture_date else "",
        "paragraphs": [],
    }
    for para in lecture.paragraphs:
        para_data = {
            "sentences": [
                {
                    "text_de": sent.text_de or "",
                    "text_zh": sent.text_zh,
                }
                for sent in sorted(para.sentences, key=lambda s: s.order_index)
            ]
        }
        lecture_data["paragraphs"].append(para_data)

    pdf_bytes = generate_bilingual_pdf(lecture_data)

    safe_title = "".join(
        c for c in lecture_data["title_de"][:40] if c.isalnum() or c in " _-"
    ).strip()

    import io
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename*=UTF-8''{safe_title}.pdf",
        },
    )


@router.get("/{lecture_id}/download-permission")
async def get_download_permission(
    lecture_id: int,
    user: AuthUser | None = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Check if the current user has download access for this lecture."""
    if not user:
        return {"has_permission": False, "access_types": []}

    has_perm = await check_download_access(db, user.id, lecture_id)
    access_types = await get_access_types(db, user.id, lecture_id) if has_perm else []

    return {
        "has_permission": has_perm,
        "access_types": access_types,
    }


@router.get("/{lecture_id}/contributions")
async def lecture_contributions(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    contributions = await get_contributions(db, lecture_id)
    return {"contributions": contributions}
