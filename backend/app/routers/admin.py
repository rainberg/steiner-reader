"""Admin router — user management, credit administration, and admin tools."""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User
from app.routers.auth import require_admin, pwd_context
from .admin_translation_utils import admin_retranslate_lecture

router = APIRouter(prefix="/api/admin", tags=["admin"])


# --- Schemas ---

class UserListItem(BaseModel):
    id: int
    username: str
    email: str
    credits: int
    is_admin: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class UpdateCreditsRequest(BaseModel):
    credits: int


class UserListResponse(BaseModel):
    users: list[UserListItem]
    total: int


class RetranslateRequest(BaseModel):
    """Request model for admin re-translation."""
    clear_existing: bool = True
    """If True, clear existing translations before translating"""
    force_all: bool = False
    """If True, translate all sentences (even those already translated)"""


class RetranslateResponse(BaseModel):
    """Response model for admin re-translation."""
    lecture_id: int
    total: int
    already_translated: int
    newly_translated: int
    now_translated: int
    message: str
    action_taken: str
    cleared_existing: bool


class LectureTranslationStats(BaseModel):
    """Statistics about lecture translation."""
    lecture_id: int
    total_sentences: int
    translated_sentences: int
    untranslated_sentences: int
    translation_ratio: float


# --- User Management Endpoints ---

@router.get("/users", response_model=UserListResponse)
async def list_users(
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """List all users with their credit balances."""
    result = await db.execute(
        select(User).order_by(User.created_at.desc())
    )
    users = result.scalars().all()
    
    return UserListResponse(
        users=[UserListItem.model_validate(u) for u in users],
        total=len(users),
    )


@router.put("/users/{user_id}/credits")
async def update_user_credits(
    user_id: int,
    req: UpdateCreditsRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Set a user's credit balance."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(404, "用户不存在")
    
    if req.credits < 0:
        raise HTTPException(400, "点数不能为负数")
    
    old_credits = user.credits
    user.credits = req.credits
    await db.commit()
    await db.refresh(user)
    
    return {
        "success": True,
        "user_id": user.id,
        "username": user.username,
        "old_credits": old_credits,
        "new_credits": user.credits,
    }


@router.post("/users/{user_id}/add-credits")
async def add_user_credits(
    user_id: int,
    req: UpdateCreditsRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Add credits to a user's balance."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(404, "用户不存在")
    
    user.credits += req.credits
    await db.commit()
    await db.refresh(user)
    
    return {
        "success": True,
        "user_id": user.id,
        "username": user.username,
        "added": req.credits,
        "new_credits": user.credits,
    }


class AddCreditsRequest(BaseModel):
    amount: int


@router.post("/users/{user_id}/credits/add")
async def add_user_credits_v2(
    user_id: int,
    req: AddCreditsRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Add credits to a user's balance (累加积分)."""
    if req.amount <= 0:
        raise HTTPException(400, "充值数量必须大于 0")

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, "用户不存在")

    user.credits += req.amount
    await db.commit()
    await db.refresh(user)

    return {
        "success": True,
        "user_id": user.id,
        "username": user.username,
        "added": req.amount,
        "new_credits": user.credits,
    }


class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


@router.put("/users/{user_id}")
async def update_user(
    user_id: int,
    req: UpdateUserRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Update a user's username and/or email."""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, "用户不存在")

    if req.username is not None:
        if len(req.username) < 2 or len(req.username) > 50:
            raise HTTPException(400, "用户名需要 2-50 个字符")
        existing = await db.execute(
            select(User).where(User.username == req.username, User.id != user_id)
        )
        if existing.scalar_one_or_none():
            raise HTTPException(400, "用户名已被使用")
        user.username = req.username

    if req.email is not None:
        if "@" not in req.email:
            raise HTTPException(400, "请输入有效邮箱")
        existing = await db.execute(
            select(User).where(User.email == req.email, User.id != user_id)
        )
        if existing.scalar_one_or_none():
            raise HTTPException(400, "该邮箱已被其他用户使用")
        user.email = req.email

    await db.commit()
    await db.refresh(user)

    return {
        "success": True,
        "user_id": user.id,
        "username": user.username,
        "email": user.email,
    }


class ResetPasswordRequest(BaseModel):
    new_password: str


@router.post("/users/{user_id}/reset-password")
async def reset_user_password(
    user_id: int,
    req: ResetPasswordRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Reset a user's password."""
    if len(req.new_password) < 6:
        raise HTTPException(400, "密码至少 6 个字符")

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, "用户不存在")

    user.password_hash = pwd_context.hash(req.new_password)
    await db.commit()

    return {"success": True, "message": f"用户 {user.username} 的密码已重置"}


# --- Translation Management Endpoints ---

@router.post("/lectures/{lecture_id}/retranslate", response_model=RetranslateResponse)
async def admin_retranslate(
    lecture_id: int,
    request: RetranslateRequest,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Admin-only endpoint to re-translate a lecture.
    
    This allows administrators to fix translation errors without cost.
    """
    try:
        result = await admin_retranslate_lecture(
            db=db,
            lecture_id=lecture_id,
            clear_existing=request.clear_existing,
            force_all=request.force_all
        )
        
        return RetranslateResponse(**result)
        
    except ValueError as e:
        raise HTTPException(404, str(e))
    except Exception as e:
        logger.error(f"Error in admin retranslation: {e}")
        raise HTTPException(500, f"Translation failed: {str(e)}")


@router.get("/lectures/{lecture_id}/translation-stats", response_model=LectureTranslationStats)
async def get_lecture_translation_stats(
    lecture_id: int,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Get detailed translation statistics for a lecture."""
    # Total sentences
    total_result = await db.execute(
        select(func.count(Sentence.id))
        .select_from(Sentence)
        .join(Paragraph)
        .where(Paragraph.lecture_id == lecture_id)
    )
    total = total_result.scalar() or 0
    
    # Translated sentences
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
        translation_ratio=ratio
    )


# Import needed for stats endpoint
from app.db.models import Sentence, Paragraph

# Set up logger
import logging
logger = logging.getLogger(__name__)

# --- Admin User Management Endpoints ---

class ToggleAdminResponse(BaseModel):
    success: bool
    user_id: int
    username: str
    is_admin: int
    message: str


@router.put("/users/{user_id}/toggle-admin", response_model=ToggleAdminResponse)
async def toggle_user_admin(
    user_id: int,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """切换用户的管理员权限"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, "用户不存在")

    if user.id == admin.id:
        raise HTTPException(400, "不能修改自己的管理员权限")

    user.is_admin = 1 if user.is_admin == 0 else 0
    await db.commit()
    await db.refresh(user)

    return ToggleAdminResponse(
        success=True,
        user_id=user.id,
        username=user.username,
        is_admin=user.is_admin,
        message=f"{user.username} 的管理员权限已{'开启' if user.is_admin else '关闭'}",
    )


class DeleteUserResponse(BaseModel):
    success: bool
    deleted_user_id: int
    username: str
    message: str


@router.delete("/users/{user_id}", response_model=DeleteUserResponse)
async def delete_user(
    user_id: int,
    admin: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """删除指定用户（不能删除自己）"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(404, "用户不存在")

    if user.id == admin.id:
        raise HTTPException(400, "不能删除自己的账号")

    username = user.username
    await db.delete(user)
    await db.commit()

    return DeleteUserResponse(
        success=True,
        deleted_user_id=user_id,
        username=username,
        message=f"用户 {username} 已删除",
    )
