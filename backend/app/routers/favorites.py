"""Favorites API router — user lecture favorites."""

import logging
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import UserFavorite, Lecture, Book
from app.routers.auth import require_user, AuthUser

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/favorites", tags=["favorites"])


@router.post("/{lecture_id}")
async def add_favorite(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """收藏讲座（幂等：已收藏则返回成功）"""
    lecture = await db.get(Lecture, lecture_id)
    if not lecture or lecture.level != "lecture":
        raise HTTPException(status_code=404, detail="讲座不存在")

    existing = await db.execute(
        select(UserFavorite).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    if existing.scalar_one_or_none():
        return {"favorited": True, "lecture_id": lecture_id}

    favorite = UserFavorite(
        user_id=user.id,
        lecture_id=lecture_id,
    )
    db.add(favorite)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
    return {"favorited": True, "lecture_id": lecture_id}


@router.delete("/{lecture_id}")
async def remove_favorite(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """取消收藏（幂等：未收藏则返回成功）"""
    await db.execute(
        delete(UserFavorite).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    await db.commit()
    return {"favorited": False, "lecture_id": lecture_id}


@router.get("")
async def list_favorites(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=50),
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """获取收藏列表（按收藏时间倒序）"""
    count_query = select(func.count()).select_from(UserFavorite).where(
        UserFavorite.user_id == user.id
    )
    total = (await db.execute(count_query)).scalar() or 0

    offset = (page - 1) * page_size
    query = (
        select(
            UserFavorite.lecture_id,
            UserFavorite.created_at.label("favorited_at"),
            Lecture.id,
            Lecture.title_de,
            Lecture.title_zh,
            Lecture.lecture_date,
            Lecture.book_id,
            Book.title_de.label("book_title_de"),
            Book.ga_number.label("book_ga_number"),
        )
        .join(Lecture, UserFavorite.lecture_id == Lecture.id)
        .join(Book, Lecture.book_id == Book.id)
        .where(UserFavorite.user_id == user.id)
        .order_by(UserFavorite.created_at.desc())
        .offset(offset)
        .limit(page_size)
    )
    result = await db.execute(query)
    rows = result.all()

    items = [
        {
            "lecture_id": row.lecture_id,
            "title_de": row.title_de,
            "title_zh": row.title_zh,
            "book_id": row.book_id,
            "book_title_de": row.book_title_de,
            "book_ga_number": row.book_ga_number,
            "lecture_date": row.lecture_date.isoformat() if row.lecture_date else None,
            "favorited_at": row.favorited_at.isoformat() if row.favorited_at else None,
        }
        for row in rows
    ]

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/{lecture_id}/status")
async def get_favorite_status(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """查询单个讲座的收藏状态"""
    result = await db.execute(
        select(UserFavorite.id).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    return {"favorited": result.scalar_one_or_none() is not None}
