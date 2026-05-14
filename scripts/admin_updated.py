"""Admin router — user management, credit administration, and admin tools."""

from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import User
from app.routers.auth import require_admin
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