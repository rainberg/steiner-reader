"""Admin router — user/credits management via Auth Service, Steiner-specific admin tools."""

import logging
from decimal import Decimal
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select, func, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.db.database import get_db
from app.db.models import (
    Book,
    Lecture,
    Sentence,
    Paragraph,
    TranslationFix,
    CreditSetting,
)
from app.routers.auth import AuthUser, require_admin
from .admin_translation_utils import admin_retranslate_lecture

router = APIRouter(prefix="/api/admin", tags=["admin"])

logger = logging.getLogger(__name__)

AUTH_BASE = settings.AUTH_SERVICE_URL


async def _proxy_auth(method: str, path: str, token: str, payload: Optional[dict] = None, params: Optional[dict] = None) -> dict:
    async with httpx.AsyncClient(timeout=15) as client:
        try:
            resp = await client.request(
                method,
                f"{AUTH_BASE}{path}",
                headers={"Authorization": f"Bearer {token}"},
                json=payload,
                params=params,
            )
            if resp.status_code == 200:
                return resp.json()
            try:
                detail = resp.json().get("detail", resp.text)
            except Exception:
                detail = resp.text
            logger.error("Auth-service %s %s returned %s: %s", method, path, resp.status_code, detail)
            raise HTTPException(status_code=resp.status_code, detail=f"Auth Service 错误: {detail}")
        except httpx.HTTPError as exc:
            logger.error("Auth-service %s %s request failed: %s", method, path, exc)
            raise HTTPException(status_code=502, detail=f"Auth Service 不可用: {exc}")


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class AddCreditsRequest(BaseModel):
    amount: Decimal
    remark: Optional[str] = None


class SetCreditsRequest(BaseModel):
    credits: Decimal
    remark: Optional[str] = None


class ToggleRoleRequest(BaseModel):
    role: str


class RetranslateRequest(BaseModel):
    clear_existing: bool = True
    force_all: bool = False


class RetranslateResponse(BaseModel):
    lecture_id: int
    total: int
    already_translated: int
    newly_translated: int
    now_translated: int
    message: str
    action_taken: str
    cleared_existing: bool


class LectureTranslationStats(BaseModel):
    lecture_id: int
    total_sentences: int
    translated_sentences: int
    untranslated_sentences: int
    translation_ratio: float


class TranslationFixCreate(BaseModel):
    pattern: str
    replacement: str
    enabled: bool = True


class TranslationFixUpdate(BaseModel):
    pattern: Optional[str] = None
    replacement: Optional[str] = None
    enabled: Optional[bool] = None


class BookTitleUpdate(BaseModel):
    title_zh: Optional[str] = None


class LectureTitleUpdate(BaseModel):
    title_zh: Optional[str] = None


class CreditSettingCreate(BaseModel):
    action: str
    price: Decimal
    description: Optional[str] = None


class CreditSettingUpdate(BaseModel):
    price: Optional[Decimal] = None
    description: Optional[str] = None


# ---------------------------------------------------------------------------
# User management — proxied to auth-service
# ---------------------------------------------------------------------------

@router.get("/users")
async def list_users(
    admin: AuthUser = Depends(require_admin),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: str = Query(""),
):
    params = {"page": page, "page_size": page_size}
    if search:
        params["search"] = search
    return await _proxy_auth("GET", "/api/admin/users", admin.raw_token, params=params)


@router.put("/users/{user_id}/credits")
async def set_user_credits(
    user_id: str,
    req: SetCreditsRequest,
    admin: AuthUser = Depends(require_admin),
):
    payload = {"credits": str(req.credits), "remark": req.remark or ""}
    return await _proxy_auth("PUT", f"/api/admin/users/{user_id}/credits", admin.raw_token, payload=payload)


@router.post("/users/{user_id}/add-credits")
async def add_user_credits(
    user_id: str,
    req: AddCreditsRequest,
    admin: AuthUser = Depends(require_admin),
):
    payload = {"amount": str(req.amount), "remark": req.remark or ""}
    return await _proxy_auth("POST", f"/api/admin/users/{user_id}/add-credits", admin.raw_token, payload=payload)


@router.put("/users/{user_id}/toggle-active")
async def toggle_user_active(
    user_id: str,
    admin: AuthUser = Depends(require_admin),
):
    return await _proxy_auth("PUT", f"/api/admin/users/{user_id}/toggle-active", admin.raw_token)


@router.put("/users/{user_id}/role")
async def set_user_role(
    user_id: str,
    req: ToggleRoleRequest,
    admin: AuthUser = Depends(require_admin),
):
    payload = {"role": req.role}
    return await _proxy_auth("PUT", f"/api/admin/users/{user_id}/role", admin.raw_token, payload=payload)


@router.get("/users/{user_id}/credit-logs")
async def get_user_credit_logs(
    user_id: str,
    admin: AuthUser = Depends(require_admin),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    params = {"page": page, "page_size": page_size}
    return await _proxy_auth("GET", f"/api/admin/users/{user_id}/credit-logs", admin.raw_token, params=params)


@router.get("/credit-logs")
async def get_all_credit_logs(
    admin: AuthUser = Depends(require_admin),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    params = {"page": page, "page_size": page_size}
    return await _proxy_auth("GET", "/api/admin/credit-logs", admin.raw_token, params=params)


# ---------------------------------------------------------------------------
# Translation Fix management — local DB
# ---------------------------------------------------------------------------

@router.get("/translation-fixes")
async def list_translation_fixes(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(TranslationFix).order_by(TranslationFix.id.desc())
    )
    fixes = result.scalars().all()
    return [
        {
            "id": f.id,
            "pattern": f.pattern,
            "replacement": f.replacement,
            "enabled": f.enabled,
            "created_at": f.created_at.isoformat() if f.created_at else None,
        }
        for f in fixes
    ]


@router.post("/translation-fixes")
async def create_translation_fix(
    req: TranslationFixCreate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    fix = TranslationFix(pattern=req.pattern, replacement=req.replacement, enabled=req.enabled)
    db.add(fix)
    await db.commit()
    await db.refresh(fix)
    return {
        "id": fix.id,
        "pattern": fix.pattern,
        "replacement": fix.replacement,
        "enabled": fix.enabled,
        "created_at": fix.created_at.isoformat() if fix.created_at else None,
    }


@router.put("/translation-fixes/{fix_id}")
async def update_translation_fix(
    fix_id: int,
    req: TranslationFixUpdate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(TranslationFix).where(TranslationFix.id == fix_id))
    fix = result.scalar_one_or_none()
    if not fix:
        raise HTTPException(404, "翻译修正规则不存在")
    if req.pattern is not None:
        fix.pattern = req.pattern
    if req.replacement is not None:
        fix.replacement = req.replacement
    if req.enabled is not None:
        fix.enabled = req.enabled
    await db.commit()
    await db.refresh(fix)
    return {
        "id": fix.id,
        "pattern": fix.pattern,
        "replacement": fix.replacement,
        "enabled": fix.enabled,
        "created_at": fix.created_at.isoformat() if fix.created_at else None,
    }


@router.delete("/translation-fixes/{fix_id}")
async def delete_translation_fix(
    fix_id: int,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(TranslationFix).where(TranslationFix.id == fix_id))
    fix = result.scalar_one_or_none()
    if not fix:
        raise HTTPException(404, "翻译修正规则不存在")
    await db.delete(fix)
    await db.commit()
    return {"success": True}


@router.post("/translation-fixes/apply-all")
async def apply_all_translation_fixes(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(TranslationFix).where(TranslationFix.enabled == True)
    )
    fixes = result.scalars().all()
    if not fixes:
        return {"success": True, "updated_count": 0, "message": "没有启用的修正规则"}

    sentence_result = await db.execute(
        select(Sentence).where(Sentence.text_zh.isnot(None))
    )
    sentences = sentence_result.scalars().all()

    updated_count = 0
    for sentence in sentences:
        original = sentence.text_zh
        modified = original
        for fix in fixes:
            modified = modified.replace(fix.pattern, fix.replacement)
        if modified != original:
            sentence.text_zh = modified
            updated_count += 1

    await db.commit()
    return {
        "success": True,
        "updated_count": updated_count,
        "fixes_applied": len(fixes),
        "message": f"已应用 {len(fixes)} 条规则，更新了 {updated_count} 个句子",
    }


# ---------------------------------------------------------------------------
# Book / Lecture title editing — local DB
# ---------------------------------------------------------------------------

@router.put("/books/{book_id}/title")
async def update_book_title(
    book_id: int,
    req: BookTitleUpdate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(404, "书籍不存在")
    if req.title_zh is not None:
        book.title_zh = req.title_zh
    await db.commit()
    return {"id": book.id, "title_zh": book.title_zh}


@router.put("/lectures/{lecture_id}/title")
async def update_lecture_title(
    lecture_id: int,
    req: LectureTitleUpdate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Lecture).where(Lecture.id == lecture_id))
    lecture = result.scalar_one_or_none()
    if not lecture:
        raise HTTPException(404, "讲座不存在")
    if req.title_zh is not None:
        lecture.title_zh = req.title_zh
    await db.commit()
    return {"id": lecture.id, "title_zh": lecture.title_zh}


# ---------------------------------------------------------------------------
# Lecture retranslation — local DB + translation service
# ---------------------------------------------------------------------------

@router.post("/lectures/{lecture_id}/retranslate", response_model=RetranslateResponse)
async def admin_retranslate(
    lecture_id: int,
    request: RetranslateRequest,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await admin_retranslate_lecture(
            db=db,
            lecture_id=lecture_id,
            clear_existing=request.clear_existing,
            force_all=request.force_all,
        )
        return RetranslateResponse(**result)
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        logger.error("Error in admin retranslation: %s", e)
        raise HTTPException(500, f"Translation failed: {str(e)}")


# ---------------------------------------------------------------------------
# Translation statistics — local DB
# ---------------------------------------------------------------------------

@router.get("/lectures/{lecture_id}/translation-stats", response_model=LectureTranslationStats)
async def get_lecture_translation_stats(
    lecture_id: int,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0

    translated_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id, Sentence.text_zh.isnot(None))
    )
    translated = translated_result.scalar() or 0

    untranslated = total - translated
    ratio = translated / total if total > 0 else 0

    return LectureTranslationStats(
        lecture_id=lecture_id,
        total_sentences=total,
        translated_sentences=translated,
        untranslated_sentences=untranslated,
        translation_ratio=ratio,
    )


@router.get("/translation-stats")
async def get_overall_translation_stats(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    total_result = await db.execute(select(func.count(Sentence.id)))
    total = total_result.scalar() or 0

    translated_result = await db.execute(
        select(func.count(Sentence.id)).where(Sentence.text_zh.isnot(None))
    )
    translated = translated_result.scalar() or 0

    books_result = await db.execute(select(func.count(Book.id)))
    book_count = books_result.scalar() or 0

    lectures_result = await db.execute(select(func.count(Lecture.id)))
    lecture_count = lectures_result.scalar() or 0

    return {
        "total_sentences": total,
        "translated_sentences": translated,
        "untranslated_sentences": total - translated,
        "translation_ratio": translated / total if total > 0 else 0,
        "book_count": book_count,
        "lecture_count": lecture_count,
    }


# ---------------------------------------------------------------------------
# CreditSetting management — local DB (price configuration)
# ---------------------------------------------------------------------------

@router.get("/credit-settings")
async def list_credit_settings(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(CreditSetting).order_by(CreditSetting.id))
    settings_list = result.scalars().all()
    return [
        {
            "id": s.id,
            "action": s.action,
            "price": float(s.price) if s.price else 0,
            "description": s.description,
            "updated_at": s.updated_at.isoformat() if s.updated_at else None,
        }
        for s in settings_list
    ]


@router.post("/credit-settings")
async def create_credit_setting(
    req: CreditSettingCreate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    existing = await db.execute(
        select(CreditSetting).where(CreditSetting.action == req.action)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(409, f"Credit setting '{req.action}' already exists")
    setting = CreditSetting(action=req.action, price=req.price, description=req.description)
    db.add(setting)
    await db.commit()
    await db.refresh(setting)
    return {
        "id": setting.id,
        "action": setting.action,
        "price": float(setting.price) if setting.price else 0,
        "description": setting.description,
    }


@router.put("/credit-settings/{setting_id}")
async def update_credit_setting(
    setting_id: int,
    req: CreditSettingUpdate,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(CreditSetting).where(CreditSetting.id == setting_id))
    setting = result.scalar_one_or_none()
    if not setting:
        raise HTTPException(404, "积分设置不存在")
    if req.price is not None:
        setting.price = req.price
    if req.description is not None:
        setting.description = req.description
    await db.commit()
    await db.refresh(setting)
    return {
        "id": setting.id,
        "action": setting.action,
        "price": float(setting.price) if setting.price else 0,
        "description": setting.description,
    }


@router.delete("/credit-settings/{setting_id}")
async def delete_credit_setting(
    setting_id: int,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(CreditSetting).where(CreditSetting.id == setting_id))
    setting = result.scalar_one_or_none()
    if not setting:
        raise HTTPException(404, "积分设置不存在")
    await db.delete(setting)
    await db.commit()
    return {"success": True}
