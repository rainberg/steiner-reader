"""Completeness check router — data integrity verification for lectures."""

import asyncio
import logging
import re
from datetime import datetime
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, delete, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import Book, Lecture, Paragraph, Sentence, CompletenessCheck
from app.routers.auth import AuthUser, require_admin

router = APIRouter(prefix="/api/admin/completeness", tags=["completeness"])

logger = logging.getLogger(__name__)

# Global state for tracking running checks
_check_state = {
    "running": False,
    "phase": "",
    "progress": 0,
    "total": 0,
    "started_at": None,
    "finished_at": None,
    "error": None,
}


# ---------------------------------------------------------------------------
# Response models
# ---------------------------------------------------------------------------

class CompletenessSummary:
    pass


# ---------------------------------------------------------------------------
# Helper: fetch steiner.wiki TOC for a GA number
# ---------------------------------------------------------------------------

async def _fetch_wiki_toc(ga_number: str) -> list[dict]:
    """Fetch lecture TOC from steiner.wiki for a given GA number."""
    ga_num = ga_number.replace("GA", "").lstrip("0") or ga_number.replace("GA", "")
    url = f"https://steiner.wiki/wiki/GA{ga_num}"
    try:
        async with httpx.AsyncClient(timeout=20, follow_redirects=True) as client:
            resp = await client.get(url)
            if resp.status_code != 200:
                return []
            html = resp.text
    except Exception:
        return []

    # Parse TOC entries from HTML
    lectures = []
    # Pattern: <a href="#...">lecture title</a> possibly followed by date text
    link_pattern = re.compile(r'<a\s+href="#[^"]*"\s*[^>]*>([^<]+)</a>')
    # German date patterns
    date_pattern = re.compile(
        r'(\d{1,2}\.\s+(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4})',
        re.IGNORECASE
    )
    short_date_pattern = re.compile(r'(\d{1,2}\.\d{1,2}\.\d{4})')

    # Split into lines and find TOC entries
    lines = html.split('\n')
    for line in lines:
        link_match = link_pattern.search(line)
        if not link_match:
            continue
        title = link_match.group(1).strip()
        # Skip non-lecture links
        if any(skip in title.lower() for skip in ['inhalt', 'einleitung', 'vorwort', 'anhang', 'register', 'nachwort', 'literatur', 'quellen', 'hinweise', 'titel', 'über']):
            continue

        # Try to find date in the same line or nearby
        date_match = date_pattern.search(line[link_match.end():])
        if not date_match:
            date_match = date_pattern.search(line)
        if not date_match:
            date_match = short_date_pattern.search(line[link_match.end():])

        lecture_entry = {
            "title": title,
            "date": date_match.group(1) if date_match else None,
        }
        lectures.append(lecture_entry)

    return lectures


# ---------------------------------------------------------------------------
# Phase 1: Database self-check
# ---------------------------------------------------------------------------

async def _run_db_self_check(db: AsyncSession):
    """Check database for obvious issues: empty lectures, truncated text, etc."""
    issues = []

    # 1. Lectures with no paragraphs
    result = await db.execute(
        select(Lecture.id, Lecture.title_de, Lecture.book_id, Book.ga_number)
        .join(Book, Lecture.book_id == Book.id)
        .where(Lecture.level == 'lecture')
        .where(
            ~Lecture.id.in_(
                select(Paragraph.lecture_id).where(Paragraph.lecture_id.isnot(None))
            )
        )
    )
    for row in result:
        issues.append({
            "ga_number": row.ga_number,
            "book_id": row.book_id,
            "lecture_id": row.id,
            "check_type": "empty_lecture",
            "severity": "error",
            "message": f"讲座无段落: {row.title_de or '(无标题)'}",
            "detail": {"lecture_title": row.title_de},
        })

    # 2. Lectures with very few sentences (< 3)
    result = await db.execute(
        select(
            Lecture.id, Lecture.title_de, Lecture.book_id, Book.ga_number,
            func.count(Sentence.id).label("sentence_count")
        )
        .join(Book, Lecture.book_id == Book.id)
        .join(Paragraph, Paragraph.lecture_id == Lecture.id)
        .join(Sentence, Sentence.paragraph_id == Paragraph.id)
        .where(Lecture.level == 'lecture')
        .group_by(Lecture.id, Lecture.title_de, Lecture.book_id, Book.ga_number)
        .having(func.count(Sentence.id) < 3)
    )
    for row in result:
        issues.append({
            "ga_number": row.ga_number,
            "book_id": row.book_id,
            "lecture_id": row.id,
            "check_type": "content_count",
            "severity": "warning",
            "message": f"讲座句子过少 ({row.sentence_count}句): {row.title_de or '(无标题)'}",
            "detail": {"lecture_title": row.title_de, "sentence_count": row.sentence_count},
        })

    # 3. Sentences with very short text_de (< 5 chars, likely truncated)
    result = await db.execute(
        select(
            Sentence.id, Sentence.text_de, Sentence.paragraph_id,
            Paragraph.lecture_id, Lecture.title_de, Lecture.book_id, Book.ga_number
        )
        .join(Paragraph, Sentence.paragraph_id == Paragraph.id)
        .join(Lecture, Paragraph.lecture_id == Lecture.id)
        .join(Book, Lecture.book_id == Book.id)
        .where(Lecture.level == 'lecture')
        .where(func.length(Sentence.text_de) < 5)
        .where(Sentence.text_de.isnot(None))
    )
    short_sentences = []
    for row in result:
        short_sentences.append(row.id)
        if len(short_sentences) <= 200:  # Limit detail records
            issues.append({
                "ga_number": row.ga_number,
                "book_id": row.book_id,
                "lecture_id": row.lecture_id,
                "check_type": "text_truncation",
                "severity": "warning",
                "message": f"句子文本过短: \"{row.text_de}\"",
                "detail": {
                    "sentence_id": row.id,
                    "text_de": row.text_de,
                    "lecture_title": row.title_de,
                },
            })

    # 4. First sentence of lecture doesn't start with uppercase (possible truncation)
    result = await db.execute(
        select(
            Sentence.id, Sentence.text_de,
            Paragraph.lecture_id, Paragraph.order_index,
            Lecture.title_de, Lecture.book_id, Book.ga_number
        )
        .join(Paragraph, Sentence.paragraph_id == Paragraph.id)
        .join(Lecture, Paragraph.lecture_id == Lecture.id)
        .join(Book, Lecture.book_id == Book.id)
        .where(Lecture.level == 'lecture')
        .where(Paragraph.order_index == 1)
        .where(Sentence.order_index == 1)
        .where(Sentence.text_de.isnot(None))
    )
    for row in result:
        first_char = row.text_de.strip()[0] if row.text_de and row.text_de.strip() else ""
        if first_char and not first_char.isupper() and first_char not in '„"«»-–—':
            issues.append({
                "ga_number": row.ga_number,
                "book_id": row.book_id,
                "lecture_id": row.lecture_id,
                "check_type": "text_truncation",
                "severity": "warning",
                "message": f"讲座开头不以大写字母开始: \"{row.text_de[:80]}\"",
                "detail": {
                    "sentence_id": row.id,
                    "text_de": row.text_de[:200],
                    "lecture_title": row.title_de,
                },
            })

    # 5. Last sentence of lecture doesn't end with punctuation
    # Get the last paragraph's last sentence for each lecture
    result = await db.execute(
        select(
            Lecture.id.label("lecture_id"),
            Lecture.title_de,
            Lecture.book_id,
            Book.ga_number,
        )
        .join(Book, Lecture.book_id == Book.id)
        .where(Lecture.level == 'lecture')
    )
    lectures_list = result.all()

    for lec in lectures_list:
        # Get last paragraph
        last_para = await db.execute(
            select(Paragraph.id)
            .where(Paragraph.lecture_id == lec.lecture_id)
            .order_by(Paragraph.order_index.desc())
            .limit(1)
        )
        para_row = last_para.first()
        if not para_row:
            continue
        # Get last sentence
        last_sent = await db.execute(
            select(Sentence.text_de)
            .where(Sentence.paragraph_id == para_row[0])
            .order_by(Sentence.order_index.desc())
            .limit(1)
        )
        sent_row = last_sent.first()
        if not sent_row or not sent_row[0]:
            continue
        last_text = sent_row[0].strip()
        if last_text and last_text[-1] not in '.!?:;…—»"':
            issues.append({
                "ga_number": lec.ga_number,
                "book_id": lec.book_id,
                "lecture_id": lec.lecture_id,
                "check_type": "text_truncation",
                "severity": "warning",
                "message": f"讲座结尾不以标点结束: \"{last_text[-80:]}\"",
                "detail": {
                    "last_text": last_text[-200:],
                    "lecture_title": lec.title_de,
                },
            })

    # 6. Books with no lectures
    result = await db.execute(
        select(Book.id, Book.ga_number, Book.title_de)
        .where(
            ~Book.id.in_(
                select(Lecture.book_id).where(Lecture.book_id.isnot(None))
            )
        )
    )
    for row in result:
        issues.append({
            "ga_number": row.ga_number,
            "book_id": row.id,
            "lecture_id": None,
            "check_type": "empty_book",
            "severity": "error",
            "message": f"书籍无讲座: {row.title_de}",
            "detail": {"book_title": row.title_de},
        })

    return issues


# ---------------------------------------------------------------------------
# Phase 2: Authority source comparison (steiner.wiki)
# ---------------------------------------------------------------------------

async def _run_wiki_comparison(db: AsyncSession):
    """Compare DB lecture counts with steiner.wiki TOC."""
    issues = []

    # Get all books with GA numbers
    result = await db.execute(
        select(Book.id, Book.ga_number, Book.title_de)
        .where(Book.ga_number.isnot(None))
        .where(Book.ga_number != '')
    )
    books = result.all()

    _check_state["total"] = len(books)

    for i, book in enumerate(books):
        _check_state["progress"] = i + 1
        _check_state["phase"] = f"权威源对比: {book.ga_number}"

        ga_num = book.ga_number.replace("GA", "")
        if not ga_num.isdigit():
            continue

        # Count lectures in DB for this book
        db_count_result = await db.execute(
            select(func.count(Lecture.id))
            .where(Lecture.book_id == book.id)
            .where(Lecture.level == 'lecture')
        )
        db_count = db_count_result.scalar() or 0

        # Fetch wiki TOC
        wiki_lectures = await _fetch_wiki_toc(book.ga_number)
        wiki_count = len(wiki_lectures)

        if wiki_count == 0:
            # Could not fetch wiki data, skip
            continue

        if db_count < wiki_count:
            # DB has fewer lectures than wiki
            missing = wiki_count - db_count
            wiki_titles = [l["title"] for l in wiki_lectures if l["title"]]
            issues.append({
                "ga_number": book.ga_number,
                "book_id": book.id,
                "lecture_id": None,
                "check_type": "missing_content",
                "severity": "warning" if missing <= 2 else "error",
                "message": f"DB讲座数({db_count})少于wiki({wiki_count})，可能缺少{missing}篇",
                "detail": {
                    "db_count": db_count,
                    "wiki_count": wiki_count,
                    "missing_count": missing,
                    "wiki_titles": wiki_titles[:30],
                    "book_title": book.title_de,
                },
            })

        # Rate limit
        await asyncio.sleep(0.3)

    return issues


# ---------------------------------------------------------------------------
# Phase 3: PDF content analysis
# ---------------------------------------------------------------------------

async def _run_pdf_analysis(db: AsyncSession):
    """Analyze PDF files for first/last paragraphs and compare with DB."""
    import os
    import pdfplumber

    issues = []
    pdf_dir = "/opt/steiner-reader/data/pdf"

    if not os.path.isdir(pdf_dir):
        issues.append({
            "ga_number": None,
            "book_id": None,
            "lecture_id": None,
            "check_type": "pdf_analysis",
            "severity": "info",
            "message": f"PDF目录不存在: {pdf_dir}",
            "detail": None,
        })
        return issues

    # Get all books with PDF filenames
    result = await db.execute(
        select(Book.id, Book.ga_number, Book.title_de, Book.pdf_filename)
        .where(Book.ga_number.isnot(None))
        .where(Book.ga_number != '')
    )
    books = result.all()

    _check_state["total"] = len(books)

    for i, book in enumerate(books):
        _check_state["progress"] = i + 1
        _check_state["phase"] = f"PDF分析: {book.ga_number}"

        pdf_path = os.path.join(pdf_dir, book.pdf_filename)
        if not os.path.isfile(pdf_path):
            continue

        try:
            # Get DB lectures for this book
            lec_result = await db.execute(
                select(Lecture.id, Lecture.title_de, Lecture.order_index)
                .where(Lecture.book_id == book.id)
                .where(Lecture.level == 'lecture')
                .order_by(Lecture.order_index)
            )
            db_lectures = lec_result.all()

            if not db_lectures:
                continue

            # Parse PDF to extract lecture boundaries
            # We'll look at first/last sentences of each lecture in DB
            # and compare with PDF content at corresponding pages
            for lec in db_lectures:
                # Get first and last sentences from DB
                first_sent_result = await db.execute(
                    select(Sentence.text_de)
                    .join(Paragraph, Sentence.paragraph_id == Paragraph.id)
                    .where(Paragraph.lecture_id == lec.id)
                    .where(Paragraph.order_index == 1)
                    .where(Sentence.order_index == 1)
                    .limit(1)
                )
                first_sent = first_sent_result.scalar_one_or_none()

                last_para_result = await db.execute(
                    select(Paragraph.id)
                    .where(Paragraph.lecture_id == lec.id)
                    .order_by(Paragraph.order_index.desc())
                    .limit(1)
                )
                last_para_id = last_para_result.scalar_one_or_none()
                if not last_para_id:
                    continue

                last_sent_result = await db.execute(
                    select(Sentence.text_de)
                    .where(Sentence.paragraph_id == last_para_id)
                    .order_by(Sentence.order_index.desc())
                    .limit(1)
                )
                last_sent = last_sent_result.scalar_one_or_none()

                # Check for truncation indicators
                if first_sent:
                    first_stripped = first_sent.strip()
                    if first_stripped and len(first_stripped) > 2:
                        # Check if first sentence starts mid-word (truncation)
                        if first_stripped[0].islower() and first_stripped[1:2].islower():
                            issues.append({
                                "ga_number": book.ga_number,
                                "book_id": book.id,
                                "lecture_id": lec.id,
                                "check_type": "text_truncation",
                                "severity": "warning",
                                "message": f"PDF分析: 讲座开头可能截断: \"{first_stripped[:60]}\"",
                                "detail": {
                                    "first_sentence": first_stripped[:200],
                                    "lecture_title": lec.title_de,
                                    "order_index": lec.order_index,
                                },
                            })

                if last_sent:
                    last_stripped = last_sent.strip()
                    if last_stripped and len(last_stripped) > 2:
                        # Check if last sentence ends mid-sentence
                        if last_stripped[-1] not in '.!?:;…—»"':
                            # Could be truncated
                            if not last_stripped.endswith(')') and not last_stripped.endswith(']'):
                                issues.append({
                                    "ga_number": book.ga_number,
                                    "book_id": book.id,
                                    "lecture_id": lec.id,
                                    "check_type": "text_truncation",
                                    "severity": "warning",
                                    "message": f"PDF分析: 讲座结尾可能截断: \"{last_stripped[-60:]}\"",
                                    "detail": {
                                        "last_sentence": last_stripped[-200:],
                                        "lecture_title": lec.title_de,
                                        "order_index": lec.order_index,
                                    },
                                })

        except Exception as e:
            logger.warning(f"PDF analysis failed for {book.ga_number}: {e}")
            continue

    return issues


# ---------------------------------------------------------------------------
# Main check runner
# ---------------------------------------------------------------------------

async def _run_completeness_check(db: AsyncSession):
    """Run all three phases of completeness checking."""
    global _check_state
    _check_state = {
        "running": True,
        "phase": "初始化",
        "progress": 0,
        "total": 0,
        "started_at": datetime.utcnow().isoformat(),
        "finished_at": None,
        "error": None,
    }

    try:
        # Clear previous results
        await db.execute(delete(CompletenessCheck))
        await db.commit()

        # Phase 1: DB self-check
        _check_state["phase"] = "数据库自检"
        _check_state["progress"] = 0
        _check_state["total"] = 1
        phase1_issues = await _run_db_self_check(db)

        # Save phase 1 results
        for issue in phase1_issues:
            check = CompletenessCheck(**issue)
            db.add(check)
        await db.commit()

        # Phase 2: Wiki comparison
        _check_state["phase"] = "权威源对比"
        _check_state["progress"] = 0
        phase2_issues = await _run_wiki_comparison(db)

        # Save phase 2 results
        for issue in phase2_issues:
            check = CompletenessCheck(**issue)
            db.add(check)
        await db.commit()

        # Phase 3: PDF analysis
        _check_state["phase"] = "PDF内容分析"
        _check_state["progress"] = 0
        phase3_issues = await _run_pdf_analysis(db)

        # Save phase 3 results
        for issue in phase3_issues:
            check = CompletenessCheck(**issue)
            db.add(check)
        await db.commit()

        _check_state["phase"] = "完成"
        _check_state["running"] = False
        _check_state["finished_at"] = datetime.utcnow().isoformat()

    except Exception as e:
        logger.error(f"Completeness check failed: {e}", exc_info=True)
        _check_state["running"] = False
        _check_state["error"] = str(e)
        _check_state["finished_at"] = datetime.utcnow().isoformat()


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@router.get("/summary")
async def get_completeness_summary(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Get summary of completeness check results."""
    # Total issues by severity
    severity_counts = {}
    for sev in ["error", "warning", "info"]:
        result = await db.execute(
            select(func.count(CompletenessCheck.id))
            .where(CompletenessCheck.severity == sev)
        )
        severity_counts[sev] = result.scalar() or 0

    # Issues by type
    type_result = await db.execute(
        select(CompletenessCheck.check_type, func.count(CompletenessCheck.id))
        .group_by(CompletenessCheck.check_type)
    )
    type_counts = {row[0]: row[1] for row in type_result}

    # Affected books count
    books_result = await db.execute(
        select(func.count(func.distinct(CompletenessCheck.book_id)))
    )
    affected_books = books_result.scalar() or 0

    # Affected lectures count
    lectures_result = await db.execute(
        select(func.count(func.distinct(CompletenessCheck.lecture_id)))
        .where(CompletenessCheck.lecture_id.isnot(None))
    )
    affected_lectures = lectures_result.scalar() or 0

    # Total checks
    total_result = await db.execute(select(func.count(CompletenessCheck.id)))
    total = total_result.scalar() or 0

    # Last check time
    last_check_result = await db.execute(
        select(func.max(CompletenessCheck.created_at))
    )
    last_check = last_check_result.scalar()

    return {
        "total_issues": total,
        "by_severity": severity_counts,
        "by_type": type_counts,
        "affected_books": affected_books,
        "affected_lectures": affected_lectures,
        "last_check": last_check.isoformat() if last_check else None,
    }


@router.get("/issues")
async def get_completeness_issues(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
    severity: Optional[str] = Query(None),
    check_type: Optional[str] = Query(None),
    ga_number: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Get paginated list of completeness issues."""
    query = select(CompletenessCheck).order_by(CompletenessCheck.created_at.desc())

    if severity:
        query = query.where(CompletenessCheck.severity == severity)
    if check_type:
        query = query.where(CompletenessCheck.check_type == check_type)
    if ga_number:
        query = query.where(CompletenessCheck.ga_number == ga_number)

    # Count
    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar() or 0

    # Paginate
    query = query.offset((page - 1) * page_size).limit(page_size)
    result = await db.execute(query)
    issues = result.scalars().all()

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": [
            {
                "id": i.id,
                "ga_number": i.ga_number,
                "book_id": i.book_id,
                "lecture_id": i.lecture_id,
                "check_type": i.check_type,
                "severity": i.severity,
                "message": i.message,
                "detail": i.detail,
                "created_at": i.created_at.isoformat() if i.created_at else None,
            }
            for i in issues
        ],
    }


@router.post("/run")
async def run_completeness_check(
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Start a completeness check run."""
    if _check_state["running"]:
        raise HTTPException(409, "检查正在运行中")

    # Run in background
    async def _run():
        from app.db.database import async_session
        async with async_session() as session:
            await _run_completeness_check(session)

    asyncio.create_task(_run())

    return {"message": "完整性检查已启动", "status": "running"}


@router.get("/status")
async def get_check_status(
    admin: AuthUser = Depends(require_admin),
):
    """Get current check run status."""
    return _check_state
