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
    score: float = 0.0


@router.get("/search")
async def search_steiner(q: str = Query(..., min_length=1), k: int = Query(5, ge=1, le=20)):
    """Semantic search over Rudolf Steiner's complete works via Qdrant."""
    try:
        # Step 1: Get embedding from OpenAI
        async with httpx.AsyncClient(timeout=30) as client:
            emb_resp = await client.post(
                f"{OPENAI_BASE}/v1/embeddings",
                json={"model": EMBED_MODEL, "input": [q]},
                headers={"Authorization": f"Bearer {OPENAI_KEY}"},
            )
            if emb_resp.status_code != 200:
                return {"query": q, "results": [], "count": 0, "error": f"Embedding failed: {emb_resp.status_code}"}
            vector = emb_resp.json()["data"][0]["embedding"]

        # Step 2: Search Qdrant
        async with httpx.AsyncClient(timeout=30) as client:
            search_resp = await client.post(
                f"{QDRANT_URL}/collections/{COLLECTION}/points/search",
                json={"vector": vector, "limit": k, "with_payload": True},
                headers={"api-key": QDRANT_API_KEY},
            )
            if search_resp.status_code != 200:
                return {"query": q, "results": [], "count": 0, "error": f"Qdrant failed: {search_resp.status_code}"}

            results = search_resp.json().get("result", [])

        items = []
        for r in results:
            p = r.get("payload", {})
            meta = p.get("metadata", {}) if isinstance(p.get("metadata"), dict) else {}
            items.append(SearchResult(
                content_de=p.get("page_content", ""),
                content_zh=p.get("zh_content", ""),
                book=meta.get("source", ""),
                score=r.get("score", 0),
            ))

        return {"query": q, "results": [i.model_dump() for i in items], "count": len(items)}

    except Exception as e:
        logger.error(f"Search error: {e}")
        return {"query": q, "results": [], "count": 0, "error": str(e)}
