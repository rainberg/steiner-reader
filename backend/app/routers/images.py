"""Lecture images router."""

import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import LectureImage

router = APIRouter(prefix="/api", tags=["images"])

IMAGES_DIR = "/opt/steiner-reader/uploads/images"


@router.get("/lectures/{lecture_id}/images")
async def get_lecture_images(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get all images for a lecture with paragraph positions."""
    result = await db.execute(
        select(LectureImage)
        .where(LectureImage.lecture_id == lecture_id)
        .order_by(LectureImage.order_index)
    )
    images = result.scalars().all()

    return [
        {
            "id": img.id,
            "lecture_id": img.lecture_id,
            "filename": img.filename,
            "url": f"/api/images/{img.filename}",
            "page_number": img.page_number,
            "width": img.width,
            "height": img.height,
            "after_paragraph_id": img.after_paragraph_id,
        }
        for img in images
    ]


@router.get("/images/{filename}")
async def serve_image(filename: str):
    """Serve an uploaded image file."""
    filepath = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(filepath, media_type="image/png")
