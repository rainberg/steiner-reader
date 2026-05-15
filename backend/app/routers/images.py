"""Images router — serve lecture images from disk."""
import os
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db

router = APIRouter(prefix="/api", tags=["images"])
IMAGES_DIR = "/opt/steiner-reader/images"


def _resolve_image_path(ga_dir: str, filename: str) -> str:
    """Resolve actual image file path, handling filename mismatches."""
    direct_path = os.path.join(IMAGES_DIR, ga_dir, filename)
    if os.path.exists(direct_path):
        return direct_path
    dir_path = os.path.join(IMAGES_DIR, ga_dir)
    if os.path.isdir(dir_path):
        name_only, ext = os.path.splitext(filename)
        for f in os.listdir(dir_path):
            if f.startswith(name_only) or name_only in f:
                return os.path.join(dir_path, f)
    return direct_path


@router.get("/books/{book_id}/images")
async def get_book_images(
    book_id: int,
    lecture_id: int = Query(None),
    db: AsyncSession = Depends(get_db),
):
    if lecture_id:
        query = text("""
            SELECT li.id, li.filename, li.order_index, b.ga_number
            FROM lecture_images li
            JOIN lectures l ON li.lecture_id = l.id
            JOIN books b ON l.book_id = b.id
            WHERE b.id = :book_id AND li.lecture_id = :lecture_id
            ORDER BY li.order_index
        """)
        result = await db.execute(query, {"book_id": book_id, "lecture_id": lecture_id})
    else:
        query = text("""
            SELECT li.id, li.filename, li.lecture_id, li.order_index, b.ga_number
            FROM lecture_images li
            JOIN lectures l ON li.lecture_id = l.id
            JOIN books b ON l.book_id = b.id
            WHERE b.id = :book_id
            ORDER BY li.lecture_id, li.order_index
        """)
        result = await db.execute(query, {"book_id": book_id})

    images = result.fetchall()
    return [{
        "id": img[0],
        "filename": img[1],
        "url": f"/api/images/{img[3]}/{img[1]}" if len(img) <= 4 else f"/api/images/{img[4]}/{img[1]}",
        "lecture_id": img[2] if len(img) > 4 else None,
        **({"lecture_id": img[2]} if len(img) > 4 else {}),
    } for img in images]


@router.get("/lectures/{lecture_id}/images")
async def get_lecture_images(lecture_id: int, db: AsyncSession = Depends(get_db)):
    query = text("""
        SELECT li.id, li.filename, li.order_index, b.ga_number
        FROM lecture_images li
        JOIN lectures l ON li.lecture_id = l.id
        JOIN books b ON l.book_id = b.id
        WHERE li.lecture_id = :lecture_id
        ORDER BY li.order_index
    """)
    result = await db.execute(query, {"lecture_id": lecture_id})
    images = result.fetchall()
    return [{
        "id": img[0],
        "filename": img[1],
        "url": f"/api/images/{img[3]}/{img[1]}",
        "order_index": img[2],
    } for img in images]


@router.get("/images/{ga_dir}/{filename}")
async def serve_image(ga_dir: str, filename: str):
    filepath = _resolve_image_path(ga_dir, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail=f"Image not found")
    media_type = "image/png"
    if filename.endswith((".jpg", ".jpeg")):
        media_type = "image/jpeg"
    return FileResponse(filepath, media_type=media_type)
