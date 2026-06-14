"""
Backfill book_id, lecture_id, sentence_id into Qdrant payload.
Runs on the Steiner backend server (66.154.112.162).

Usage:
  python qdrant_backfill.py                    # from start or resume

Progress is saved to qdrant_backfill_progress.json after each batch.
"""

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
from sqlalchemy import text
from app.db.database import async_session

QDRANT_URL = "https://a7e5f6a9-437c-4b92-91a7-b4de5661aa24.ap-northeast-1-0.aws.cloud.qdrant.io:6333"
QDRANT_API_KEY = "4fhMJy51skJRL8z2sFrnfrzEWtL3k_-NK6BTWYGoK7jgxkV9H3LT1w"
COLLECTION = "rs_werke"
BATCH_SIZE = 100
PROGRESS_FILE = Path(__file__).parent / "qdrant_backfill_progress.json"


import re


def escape_like(s: str) -> str:
    return s.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')


def normalize_text(s: str) -> str:
    """Remove soft hyphens and normalize whitespace for matching."""
    # Remove soft hyphen patterns: "word- nextword" -> "wordnextword"
    s = re.sub(r'(\w)- (\w)', r'\1\2', s)
    # Normalize whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"last_offset": 0, "total_processed": 0, "total_matched": 0, "total_unmatched": 0}


def save_progress(progress: dict):
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))


async def get_book_id_by_source(db, source: str) -> int | None:
    pn = source.replace(".pdf", "").replace(".epub", "").replace(".bdn", "")
    result = await db.execute(
        text("SELECT id FROM books WHERE REPLACE(pdf_filename, '.pdf', '') LIKE '%' || :pn || '%' OR REPLACE(pdf_filename, '.epub', '') LIKE '%' || :pn || '%' OR REPLACE(pdf_filename, '.bdn', '') LIKE '%' || :pn || '%' LIMIT 1"),
        {"pn": pn}
    )
    row = result.first()
    return row[0] if row else None


async def locate_sentence(db, book_id: int, content_de: str) -> tuple[int | None, int | None]:
    # Normalize the Qdrant content prefix for matching
    prefix = normalize_text(content_de[:80])
    escaped = escape_like(prefix)
    # Use REGEXP_REPLACE to strip soft hyphens from DB text before comparing
    result = await db.execute(
        text("""
            SELECT s.id, p.lecture_id
            FROM sentences s
            JOIN paragraphs p ON s.paragraph_id = p.id
            WHERE p.lecture_id IN (SELECT id FROM lectures WHERE book_id = :book_id)
            AND REGEXP_REPLACE(REGEXP_REPLACE(s.text_de, '(\\w)- (\\w)', '\\1\\2', 'g'), '\\s+', ' ', 'g') LIKE :prefix ESCAPE '\\'
            LIMIT 1
        """),
        {"book_id": book_id, "prefix": f"{escaped}%"}
    )
    row = result.first()
    if row:
        return row[0], row[1]
    return None, None


async def update_qdrant_payload(client: httpx.AsyncClient, updates: list[dict]):
    """Set payload fields on multiple points using Qdrant set_payload API (merge mode).
    Sends requests concurrently for speed."""
    import asyncio

    async def set_one(point_update: dict):
        pid = point_update["id"]
        payload = point_update["payload"]
        new_fields = {
            "book_id": payload.get("book_id"),
            "lecture_id": payload.get("lecture_id"),
            "sentence_id": payload.get("sentence_id"),
        }
        resp = await client.post(
            f"{QDRANT_URL}/collections/{COLLECTION}/points/payload",
            json={"payload": new_fields, "points": [pid]},
            headers={"api-key": QDRANT_API_KEY, "Content-Type": "application/json"},
        )
        resp.raise_for_status()

    # Run with concurrency limit to avoid overwhelming the API
    sem = asyncio.Semaphore(10)

    async def limited(task):
        async with sem:
            return await task

    tasks = [limited(set_one(u)) for u in updates]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    errors = [r for r in results if isinstance(r, Exception)]
    if errors:
        raise errors[0]


async def scroll_qdrant(client: httpx.AsyncClient, offset: int = 0) -> tuple[list[dict], int | None]:
    resp = await client.post(
        f"{QDRANT_URL}/collections/{COLLECTION}/points/scroll",
        json={"limit": BATCH_SIZE, "offset": offset, "with_payload": True, "with_vector": False},
        headers={"api-key": QDRANT_API_KEY},
    )
    resp.raise_for_status()
    data = resp.json().get("result", {})
    points = data.get("points", [])
    next_offset = data.get("next_page_offset")
    return points, next_offset


async def main():
    progress = load_progress()
    offset = progress["last_offset"]
    print(f"Starting from offset {offset} (processed: {progress['total_processed']}, matched: {progress['total_matched']}, unmatched: {progress['total_unmatched']})")

    book_cache: dict[str, int | None] = {}

    async with httpx.AsyncClient(timeout=60) as qdrant_client:
        async with async_session() as db:
            while True:
                try:
                    points, next_offset = await scroll_qdrant(qdrant_client, offset)
                except Exception as e:
                    print(f"Error scrolling Qdrant: {e}")
                    break

                if not points:
                    print("No more points to process.")
                    break

                updates = []
                for point in points:
                    pid = point["id"]
                    payload = point.get("payload", {})
                    meta = payload.get("metadata", {}) if isinstance(payload.get("metadata"), dict) else {}
                    source = meta.get("source", "")
                    content_de = payload.get("page_content", "")

                    # Skip if already fully backfilled
                    if payload.get("book_id") is not None and payload.get("sentence_id") is not None:
                        progress["total_processed"] += 1
                        progress["total_matched"] += 1
                        continue

                    book_id = payload.get("book_id")  # May already be set from first run
                    lecture_id = None
                    sentence_id = None

                    # Step 1: Find book_id if not already set
                    if book_id is None and source:
                        if source not in book_cache:
                            book_cache[source] = await get_book_id_by_source(db, source)
                        book_id = book_cache[source]

                    # Step 2: Find sentence_id and lecture_id
                    if book_id and content_de:
                        sentence_id, lecture_id = await locate_sentence(db, book_id, content_de)

                    # Build update payload (merge with existing)
                    new_payload = dict(payload)
                    new_payload["book_id"] = book_id
                    new_payload["lecture_id"] = lecture_id
                    new_payload["sentence_id"] = sentence_id

                    updates.append({"id": pid, "payload": new_payload})

                    progress["total_processed"] += 1
                    if book_id is not None:
                        progress["total_matched"] += 1
                    else:
                        progress["total_unmatched"] += 1

                    if progress["total_processed"] % 100 == 0:
                        print(f"  Processed {progress['total_processed']}... (matched: {progress['total_matched']}, unmatched: {progress['total_unmatched']})")

                # Batch update Qdrant
                if updates:
                    try:
                        await update_qdrant_payload(qdrant_client, updates)
                        print(f"  Updated {len(updates)} points in Qdrant")
                    except Exception as e:
                        print(f"  ERROR updating Qdrant: {e}")
                        break

                # Save progress
                progress["last_offset"] = next_offset or 0
                save_progress(progress)

                if next_offset is None:
                    print("Reached end of collection.")
                    break

                offset = next_offset

    print(f"\nDone! Total: {progress['total_processed']}, Matched: {progress['total_matched']}, Unmatched: {progress['total_unmatched']}")


if __name__ == "__main__":
    asyncio.run(main())
