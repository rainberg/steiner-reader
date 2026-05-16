"""Semantic search over Steiner's works via Qdrant REST API."""

import logging
import httpx
from fastapi import APIRouter, Query
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["search"])

QDRANT_URL = "https://a7e5f6a9-437c-4b92-91a7-b4de5661aa24.ap-northeast-1-0.aws.cloud.qdrant.io:6333"
QDRANT_API_KEY = "4fhMJy51skJRL8z2sFrnfrzEWtL3k_-NK6BTWYGoK7jgxkV9H3LT1w"
COLLECTION = "rs_werke"

OPENAI_KEY = "fk201403-hCEJwCHpGTrUkdzzkvBW93gvrWCM9vDm"
OPENAI_BASE = "https://openai.api2d.net"
EMBED_MODEL = "text-embedding-ada-002"


class SearchResult(BaseModel):
    content_de: str = ""
    content_zh: str = ""
    book: str = ""
    ga_number: str = ""
    score: float = 0.0


@router.get("/search")
async def search_steiner(q: str = Query(..., min_length=1), k: int = Query(5, ge=1, le=20)):
    """Semantic search over Rudolf Steiner's complete works via Qdrant."""
    try:
        # Step 1: Get embedding
        async with httpx.AsyncClient(timeout=30) as client:
            emb_resp = await client.post(
                f"{OPENAI_BASE}/v1/embeddings",
                json={"model": EMBED_MODEL, "input": [q]},
                headers={"Authorization": f"Bearer {OPENAI_KEY}"},
            )
            if emb_resp.status_code != 200:
                return {"query": q, "results": [], "count": 0}
            vector = emb_resp.json()["data"][0]["embedding"]

        # Step 2: Search Qdrant
        async with httpx.AsyncClient(timeout=30) as client:
            search_resp = await client.post(
                f"{QDRANT_URL}/collections/{COLLECTION}/points/search",
                json={"vector": vector, "limit": k, "with_payload": True},
                headers={"api-key": QDRANT_API_KEY},
            )
            results = search_resp.json().get("result", []) if search_resp.status_code == 200 else []

        # Step 3: Map PDF filenames to book info
        pdf_map = {}
        pdf_names = set()
        for r in results:
            p = r.get("payload", {})
            meta = p.get("metadata", {}) if isinstance(p.get("metadata"), dict) else {}
            src = meta.get("source", "")
            if src:
                pdf_names.add(src)

        if pdf_names:
            try:
                from app.db.database import async_session
                from sqlalchemy import text
                async with async_session() as db:
                    for pdf_name in pdf_names:
                        pn = pdf_name.replace(".pdf", "")
                        result = await db.execute(
                            text("SELECT ga_number, title_de, title_zh FROM books WHERE REPLACE(pdf_filename, '.pdf', '') LIKE '%' || :pn || '%' OR REPLACE(pdf_filename, '.epub', '') LIKE '%' || :pn || '%' OR REPLACE(pdf_filename, '.bdn', '') LIKE '%' || :pn || '%' LIMIT 1"),
                            {"pn": pn}
                        )
                        row = result.first()
                        if row:
                            pdf_map[pdf_name] = {"ga": row[0], "de": row[1], "zh": row[2]}
            except Exception as e:
                logger.warning(f"Book lookup: {e}")

        items = []
        for r in results:
            p = r.get("payload", {})
            meta = p.get("metadata", {}) if isinstance(p.get("metadata"), dict) else {}
            src = meta.get("source", "")
            info = pdf_map.get(src, {})
            ga = info.get("ga", "")
            label = f"{ga}: {info.get('zh') or info.get('de') or ''}" if ga else src
            items.append(SearchResult(
                content_de=p.get("page_content", ""),
                content_zh=p.get("zh_content", ""),
                book=label,
                ga_number=ga,
                score=r.get("score", 0),
            ))

        return {"query": q, "results": [i.model_dump() for i in items], "count": len(items)}

    except Exception as e:
        logger.error(f"Search error: {e}")
        return {"query": q, "results": [], "count": 0, "error": str(e)}
