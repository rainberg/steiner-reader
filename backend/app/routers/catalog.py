"""Catalog API router for lecture catalog queries and statistics."""

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import LectureCatalog, LocationAbbreviation
from app.models.schemas import (
    CatalogLectureResponse,
    CatalogLectureList,
    CatalogStatsResponse,
    CatalogLocationResponse,
)

router = APIRouter(prefix="/api/catalog", tags=["catalog"])


@router.get("/lectures", response_model=CatalogLectureList)
async def list_catalog_lectures(
    year: int | None = Query(None),
    year_from: int | None = Query(None),
    year_to: int | None = Query(None),
    location_code: str | None = Query(None),
    ga_number: str | None = Query(None),
    is_collected: bool | None = Query(None),
    is_lecture_matched: bool | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
):
    """Paginated query of lecture catalog entries with optional filters."""
    # Base query
    query = select(LectureCatalog)
    count_query = select(func.count()).select_from(LectureCatalog)

    # Apply filters
    if year is not None:
        query = query.where(LectureCatalog.year == year)
        count_query = count_query.where(LectureCatalog.year == year)
    if year_from is not None:
        query = query.where(LectureCatalog.year >= year_from)
        count_query = count_query.where(LectureCatalog.year >= year_from)
    if year_to is not None:
        query = query.where(LectureCatalog.year <= year_to)
        count_query = count_query.where(LectureCatalog.year <= year_to)
    if location_code is not None:
        query = query.where(LectureCatalog.location_code == location_code)
        count_query = count_query.where(LectureCatalog.location_code == location_code)
    if ga_number is not None:
        query = query.where(LectureCatalog.ga_number == ga_number)
        count_query = count_query.where(LectureCatalog.ga_number == ga_number)
    if is_collected is not None:
        query = query.where(LectureCatalog.is_collected == is_collected)
        count_query = count_query.where(LectureCatalog.is_collected == is_collected)
    if is_lecture_matched is not None:
        query = query.where(LectureCatalog.is_lecture_matched == is_lecture_matched)
        count_query = count_query.where(LectureCatalog.is_lecture_matched == is_lecture_matched)

    # Total count
    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0

    # Pagination
    offset = (page - 1) * page_size
    query = query.order_by(LectureCatalog.id).offset(offset).limit(page_size)

    result = await db.execute(query)
    items = [CatalogLectureResponse.model_validate(row) for row in result.scalars().all()]

    return CatalogLectureList(
        total=total,
        page=page,
        page_size=page_size,
        items=items,
    )


@router.get("/stats", response_model=CatalogStatsResponse)
async def catalog_stats(db: AsyncSession = Depends(get_db)):
    """Get aggregate statistics for the lecture catalog."""
    # Total, collected, lecture_matched
    total_result = await db.execute(select(func.count()).select_from(LectureCatalog))
    total = total_result.scalar() or 0

    collected_result = await db.execute(
        select(func.count()).select_from(LectureCatalog).where(LectureCatalog.is_collected == True)
    )
    collected = collected_result.scalar() or 0

    matched_result = await db.execute(
        select(func.count()).select_from(LectureCatalog).where(LectureCatalog.is_lecture_matched == True)
    )
    lecture_matched = matched_result.scalar() or 0

    # Year range
    year_min_result = await db.execute(select(func.min(LectureCatalog.year)))
    year_min = year_min_result.scalar()
    year_max_result = await db.execute(select(func.max(LectureCatalog.year)))
    year_max = year_max_result.scalar()
    year_range = list(range(year_min, year_max + 1)) if year_min and year_max else []

    # Group by year
    by_year_result = await db.execute(
        select(LectureCatalog.year, func.count())
        .group_by(LectureCatalog.year)
        .order_by(LectureCatalog.year)
    )
    by_year = {str(row[0]): row[1] for row in by_year_result.all() if row[0] is not None}

    # Group by location_code with full_name from location_abbreviations
    by_location_result = await db.execute(
        select(LectureCatalog.location_code, LocationAbbreviation.full_name, func.count(LectureCatalog.id))
        .outerjoin(LocationAbbreviation, LectureCatalog.location_code == LocationAbbreviation.code)
        .group_by(LectureCatalog.location_code, LocationAbbreviation.full_name)
        .order_by(func.count(LectureCatalog.id).desc())
    )
    by_location = [
        {"code": row[0] or "", "name": row[1] or "", "count": row[2]}
        for row in by_location_result.all()
    ]

    # Group by decade
    by_decade_result = await db.execute(
        text("""
            SELECT FLOOR(year / 10) * 10 AS decade, COUNT(*) AS cnt
            FROM lecture_catalog
            WHERE year IS NOT NULL
            GROUP BY decade
            ORDER BY decade
        """)
    )
    by_decade = {f"{int(row[0])}s": row[1] for row in by_decade_result.all()}

    return CatalogStatsResponse(
        total=total,
        collected=collected,
        lecture_matched=lecture_matched,
        year_range=year_range,
        by_year=by_year,
        by_location=by_location,
        by_decade=by_decade,
    )


@router.get("/locations", response_model=list[CatalogLocationResponse])
async def list_locations(db: AsyncSession = Depends(get_db)):
    """Get all locations with lecture counts, sorted by count descending."""
    result = await db.execute(
        select(
            LocationAbbreviation.code,
            LocationAbbreviation.full_name,
            func.count(LectureCatalog.id),
        )
        .outerjoin(LectureCatalog, LocationAbbreviation.code == LectureCatalog.location_code)
        .group_by(LocationAbbreviation.code, LocationAbbreviation.full_name)
        .order_by(func.count(LectureCatalog.id).desc())
    )
    return [
        CatalogLocationResponse(code=row[0], full_name=row[1], lecture_count=row[2])
        for row in result.all()
    ]
