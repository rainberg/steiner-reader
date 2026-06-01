"""Books API router."""

import re
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import Book, Lecture, Paragraph, Sentence
from app.models.schemas import BookResponse, BookDetail, BookSummary, LectureResponse, LectureSummary, LectureListItem
from app.routers.auth import get_current_user, AuthUser

router = APIRouter(prefix="/api/books", tags=["books"])


@router.get("/summary", response_model=list[BookSummary])
async def list_book_summaries(
    page: int = Query(1, ge=1),
    page_size: int = Query(24, ge=1, le=200),
    search: str = Query("", max_length=200),
    sort_by: str = Query("created_at", pattern="^(created_at|ga_number|title_de|lecture_count)$"),
    sort_dir: str = Query("desc", pattern="^(asc|desc)$"),
    db: AsyncSession = Depends(get_db),
):
    """Get compact book rows for the homepage. Supports pagination, search, and sorting."""
    base_cte = """
        WITH lecture_counts AS (
            SELECT book_id, COUNT(*) AS lecture_count
            FROM lectures GROUP BY book_id
        ),
        sentence_counts AS (
            SELECT l.book_id, COUNT(s.id) AS sentence_count
            FROM lectures l
            JOIN paragraphs p ON p.lecture_id = l.id
            JOIN sentences s ON s.paragraph_id = p.id
            GROUP BY l.book_id
        ),
        translated_counts AS (
            SELECT l.book_id, COUNT(s.id) AS translated_count
            FROM lectures l
            JOIN paragraphs p ON p.lecture_id = l.id
            JOIN sentences s ON s.paragraph_id = p.id
            WHERE s.text_zh IS NOT NULL AND s.text_zh != '' AND l.is_published = true
            GROUP BY l.book_id
        ),
        image_counts AS (
            SELECT l.book_id, COUNT(li.id) AS image_count
            FROM lectures l
            JOIN lecture_images li ON li.lecture_id = l.id
            GROUP BY l.book_id
        )
    """
    select_clause = """
        SELECT
            b.id, b.ga_number, b.title_de, b.title_zh, b.pdf_filename,
            b.cover_url, b.created_at,
            COALESCE(lc.lecture_count, 0) AS lecture_count,
            COALESCE(sc.sentence_count, 0) AS sentence_count,
            COALESCE(ic.image_count, 0) AS image_count,
            COALESCE(tc.translated_count, 0) AS translated_count
        FROM books b
        LEFT JOIN lecture_counts lc ON lc.book_id = b.id
        LEFT JOIN sentence_counts sc ON sc.book_id = b.id
        LEFT JOIN image_counts ic ON ic.book_id = b.id
        LEFT JOIN translated_counts tc ON tc.book_id = b.id
    """
    where = ""
    params: dict = {}
    if search:
        where = " WHERE b.ga_number ILIKE :q OR b.title_de ILIKE :q OR b.title_zh ILIKE :q"
        params["q"] = f"%{search}%"

    sort_col_map = {
        "created_at": "b.created_at",
        "ga_number": "b.ga_number",
        "title_de": "b.title_de",
        "lecture_count": "lecture_count",
    }
    sort_col = sort_col_map.get(sort_by, "b.created_at")
    direction = "ASC" if sort_dir == "asc" else "DESC"

    offset = (page - 1) * page_size
    query = f"{base_cte}{select_clause}{where} ORDER BY {sort_col} {direction} LIMIT :limit OFFSET :offset"
    params["limit"] = page_size
    params["offset"] = offset

    result = await db.execute(text(query), params)
    return [BookSummary(**dict(row._mapping)) for row in result]


@router.get("/summary/count")
async def book_count(
    search: str = Query("", max_length=200),
    db: AsyncSession = Depends(get_db),
):
    """Get total book count (with optional search filter) for pagination."""
    if search:
        result = await db.execute(
            text("SELECT COUNT(*) FROM books WHERE ga_number ILIKE :q OR title_de ILIKE :q OR title_zh ILIKE :q"),
            {"q": f"%{search}%"},
        )
    else:
        result = await db.execute(text("SELECT COUNT(*) FROM books"))
    return {"count": result.scalar() or 0}


@router.get("/groups")
async def list_book_groups(db: AsyncSession = Depends(get_db)):
    """Get books grouped by GA number prefix (e.g. GA010, GA020, ...)."""
    result = await db.execute(
        text(
            """
            WITH lecture_counts AS (
                SELECT book_id, COUNT(*) AS lecture_count
                FROM lectures GROUP BY book_id
            ),
            sentence_counts AS (
                SELECT l.book_id, COUNT(s.id) AS sentence_count
                FROM lectures l
                JOIN paragraphs p ON p.lecture_id = l.id
                JOIN sentences s ON s.paragraph_id = p.id
                GROUP BY l.book_id
            )
            SELECT
                b.id, b.ga_number, b.title_de, b.title_zh, b.pdf_filename,
                b.cover_url, b.created_at,
                COALESCE(lc.lecture_count, 0) AS lecture_count,
                COALESCE(sc.sentence_count, 0) AS sentence_count,
                0 AS image_count,
                0 AS translated_count
            FROM books b
            LEFT JOIN lecture_counts lc ON lc.book_id = b.id
            LEFT JOIN sentence_counts sc ON sc.book_id = b.id
            ORDER BY b.ga_number NULLS LAST, b.title_de
            """
        )
    )
    all_books = [BookSummary(**dict(row._mapping)) for row in result]

    groups: dict[str, list[BookSummary]] = {}
    for book in all_books:
        ga = (book.ga_number or "").strip()
        # Group by tens: GA001-GA009 → "GA00x", GA010-GA019 → "GA01x", etc.
        if ga.startswith("GA") and len(ga) >= 4 and ga[2:].isdigit():
            num = int(ga[2:])
            decade = (num // 10) * 10
            prefix = f"GA{decade:03d}-{decade+9:03d}"
        elif ga.startswith("GA"):
            prefix = ga[:4] + "x"
        else:
            prefix = "未分类"
        groups.setdefault(prefix, []).append(book)

    result_list = []
    for prefix in sorted(groups.keys()):
        books_in_group = groups[prefix]
        result_list.append({
            "group": prefix,
            "book_count": len(books_in_group),
            "lecture_count": sum(b.lecture_count for b in books_in_group),
            "sentence_count": sum(b.sentence_count for b in books_in_group),
            "books": books_in_group,
        })
    return result_list


@router.get("", response_model=list[BookResponse])
async def list_books(db: AsyncSession = Depends(get_db)):
    """Get all books with lecture summaries (lightweight — no sentence data)."""
    books_result = await db.execute(
        select(Book).order_by(Book.created_at.desc())
    )
    books = books_result.scalars().all()
    if not books:
        return []

    book_ids = [b.id for b in books]

    lectures_result = await db.execute(
        select(Lecture).where(Lecture.book_id.in_(book_ids)).order_by(Lecture.order_index)
    )
    lectures = lectures_result.scalars().all()

    lecture_ids = [l.id for l in lectures]

    sentence_counts = {}
    if lecture_ids:
        sc_result = await db.execute(
            select(Paragraph.lecture_id, func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id.in_(lecture_ids))
            .group_by(Paragraph.lecture_id)
        )
        sentence_counts = dict(sc_result.all())

    image_counts = {}
    if lecture_ids:
        ic_result = await db.execute(
            text("SELECT lecture_id, COUNT(*) FROM lecture_images WHERE lecture_id = ANY(:ids) GROUP BY lecture_id"),
            {"ids": lecture_ids},
        )
        image_counts = {row[0]: row[1] for row in ic_result.all()}

    translated_counts = {}
    if lecture_ids:
        tc_result = await db.execute(
            select(Paragraph.lecture_id, func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(
                Paragraph.lecture_id.in_(lecture_ids),
                Sentence.text_zh.isnot(None),
                Sentence.text_zh != "",
            )
            .group_by(Paragraph.lecture_id)
        )
        translated_counts = dict(tc_result.all())

    published_lecture_ids = {l.id for l in lectures if l.is_published}

    lectures_by_book: dict[int, list[Lecture]] = {}
    for lec in lectures:
        lectures_by_book.setdefault(lec.book_id, []).append(lec)

    book_image_counts = {}
    bi_result = await db.execute(
        text("SELECT l.book_id, COUNT(li.id) FROM lecture_images li JOIN lectures l ON li.lecture_id = l.id WHERE l.book_id = ANY(:bids) GROUP BY l.book_id"),
        {"bids": book_ids},
    )
    book_image_counts = {row[0]: row[1] for row in bi_result.all()}

    response = []
    for book in books:
        book_lectures = lectures_by_book.get(book.id, [])
        lecture_summaries = []
        for lec in book_lectures:
            sc = sentence_counts.get(lec.id, 0)
            ic = image_counts.get(lec.id, 0)
            tc = translated_counts.get(lec.id, 0) if lec.id in published_lecture_ids else 0
            lecture_summaries.append(LectureSummary(
                id=lec.id,
                title_de=lec.title_de,
                title_zh=lec.title_zh,
                lecture_date=lec.lecture_date,
                location=lec.location,
                order_index=lec.order_index,
                sentence_count=sc,
                image_count=ic,
                translated_count=tc,
                level=lec.level,
                parent_id=lec.parent_id,
            ))

        response.append(BookResponse(
            id=book.id,
            ga_number=book.ga_number,
            title_de=book.title_de,
            title_zh=book.title_zh,
            pdf_filename=book.pdf_filename,
            cover_url=book.cover_url,
            created_at=book.created_at,
            lectures=lecture_summaries,
            image_count=book_image_counts.get(book.id, 0),
        ))

    return response


@router.get("/{book_id}", response_model=BookDetail)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """Get book detail with lectures and translation counts (no sentence data — use /lectures/{id} for reading)."""
    result = await db.execute(
        select(Book).where(Book.id == book_id)
    )
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    lectures_result = await db.execute(
        select(Lecture).where(Lecture.book_id == book_id).order_by(Lecture.order_index)
    )
    lectures = lectures_result.scalars().all()

    lecture_ids = [l.id for l in lectures]

    sentence_counts = {}
    translated_counts = {}
    image_counts = {}

    if lecture_ids:
        sc_result = await db.execute(
            select(Paragraph.lecture_id, func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(Paragraph.lecture_id.in_(lecture_ids))
            .group_by(Paragraph.lecture_id)
        )
        sentence_counts = dict(sc_result.all())

        tc_result = await db.execute(
            select(Paragraph.lecture_id, func.count(Sentence.id))
            .select_from(Sentence)
            .join(Paragraph)
            .where(
                Paragraph.lecture_id.in_(lecture_ids),
                Sentence.text_zh.isnot(None),
            )
            .group_by(Paragraph.lecture_id)
        )
        translated_counts = dict(tc_result.all())

        ic_result = await db.execute(
            text("SELECT lecture_id, COUNT(*) FROM lecture_images WHERE lecture_id = ANY(:ids) GROUP BY lecture_id"),
            {"ids": lecture_ids},
        )
        image_counts = {row[0]: row[1] for row in ic_result.all()}

    published_ids = {l.id for l in lectures if l.is_published}

    lectures_items = []
    for lec in lectures:
        lectures_items.append(LectureListItem(
            id=lec.id,
            book_id=book.id,
            title_de=lec.title_de,
            title_zh=lec.title_zh,
            lecture_date=lec.lecture_date,
            location=lec.location,
            order_index=lec.order_index,
            sentence_count=sentence_counts.get(lec.id, 0),
            image_count=image_counts.get(lec.id, 0),
            translated_count=translated_counts.get(lec.id, 0) if lec.id in published_ids else 0,
            level=lec.level,
            parent_id=lec.parent_id,
        ))

    return BookDetail(
        id=book.id,
        ga_number=book.ga_number,
        title_de=book.title_de,
        title_zh=book.title_zh,
        pdf_filename=book.pdf_filename,
        cover_url=book.cover_url,
        created_at=book.created_at,
        lectures=lectures_items,
        image_count=sum(li.image_count for li in lectures_items),
    )


@router.get("/{book_id}/lectures/{lecture_id}")
async def get_lecture(
    book_id: int,
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
    user: AuthUser | None = Depends(get_current_user),
):
    """Get a specific lecture with all paragraphs and sentences (for reader page)."""
    result = await db.execute(
        select(Lecture)
        .where(Lecture.id == lecture_id, Lecture.book_id == book_id)
        .options(
            selectinload(Lecture.paragraphs)
            .selectinload(Paragraph.sentences)
        )
    )
    lecture = result.scalar_one_or_none()

    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

    from app.routers.lectures import _build_paragraph_response
    from app.services.credit_service import (
        get_contributions, check_download_access, get_access_types, compute_price,
    )
    from sqlalchemy import text as sa_text
    from app.db.models import SentenceRevision

    is_published = lecture.is_published or False

    # Fetch winning revisions: hash match first, then anchor fallback
    import hashlib
    win_map = {}

    # Build hash+anchor for each sentence
    sent_hashes = {}
    for para in lecture.paragraphs:
        for sent in para.sentences:
            n = re.sub(r'\s+', ' ', (sent.text_de or '')).strip()
            sent_hashes[sent.id] = (hashlib.sha256(n.encode()).hexdigest(), (n[:60] + "|" + n[-60:])[:200])

    # Get all active revisions for this lecture
    all_rev_result = await db.execute(sa_text("""
        SELECT r.sentence_id, r.field, r.new_value, r.text_hash, r.text_anchor,
               r.vote_count, r.created_at
        FROM sentence_revisions r
        WHERE r.sentence_id IN (
            SELECT s.id FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = :lid
        )
        AND r.status = 'active'
        ORDER BY r.vote_count DESC, r.created_at DESC
    """), {"lid": lecture_id})
    all_revs = all_rev_result.fetchall()

    # Match: for each sentence, pick the best revision by hash or anchor
    for sid, (href, ha) in sent_hashes.items():
        for row in all_revs:
            rsid, field, val, rhash, ranch, _, _ = row
            if sid != rsid: continue
            if rhash == href or (ranch and ranch[:30] in ha):
                if sid not in win_map: win_map[sid] = {}
                if field not in win_map[sid]: win_map[sid][field] = val

    # Apply winning revisions
    for para in lecture.paragraphs:
        for sent in para.sentences:
            if sent.id in win_map:
                revs = win_map[sent.id]
                if "text_de" in revs:
                    sent.text_de = revs["text_de"]
                    if "text_zh" not in revs:
                        sent.text_zh = None
                if "text_zh" in revs:
                    sent.text_zh = revs["text_zh"]

    # 查询该讲座的图片 -> sentence_id 映射（动态获取 GA 号）
    img_result = await db.execute(
        sa_text("SELECT li.after_sentence_id, li.filename, b.ga_number FROM lecture_images li " +
                "JOIN lectures l ON li.lecture_id = l.id " +
                "JOIN books b ON l.book_id = b.id " +
                "WHERE li.lecture_id = :lid"),
        {"lid": lecture_id}
    )
    image_map = {}
    unlinked_images = []
    for row in img_result:
        ga = row[2] if row[2] else "GA279"
        url = f"/api/images/{ga}/{row[1]}"
        if row[0]:
            image_map[row[0]] = url
        else:
            unlinked_images.append(url)

    # Contributions (for display)
    contributions = await get_contributions(db, lecture_id)

    # Download permission
    can_download_pdf = False
    if user:
        can_download_pdf = await check_download_access(db, user.id, lecture_id)

    # Edit costs
    edit_translation_cost = await compute_price(db, "edit_translation_coefficient", 1)
    edit_source_cost = await compute_price(db, "edit_source_coefficient", 1)
    download_lecture_cost = await compute_price(db, "download_lecture_pdf", 0)

    return {
        "id": lecture.id,
        "book_id": lecture.book_id,
        "order_index": lecture.order_index,
        "title_de": lecture.title_de,
        "title_zh": lecture.title_zh,
        "lecture_date": str(lecture.lecture_date) if lecture.lecture_date else None,
        "location": lecture.location,
        "is_published": is_published,
        "contributors": contributions,
        "can_download_pdf": can_download_pdf,
        "can_edit": is_published and user is not None,
        "download_notice": "请及时下载已解锁内容。本网站不保证长期运行或永久提供访问。",
        "download_lecture_cost": download_lecture_cost,
        "edit_translation_cost": edit_translation_cost,
        "edit_source_cost": edit_source_cost,
        "paragraphs": [_build_paragraph_response(p, image_map, is_published) for p in lecture.paragraphs],
        "unlinked_images": unlinked_images,
    }
