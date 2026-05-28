"""Sentence editing with revision voting system."""

import logging
from fastapi import APIRouter, Depends, HTTPException
import hashlib
import re
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.models import (
    Sentence, Paragraph, Lecture, EditAuditLog,
    SentenceRevision, RevisionVote,
)
from app.routers.auth import AuthUser, require_user, require_admin
from app.services.credit_service import (
    compute_price, atomic_deduct_credits, add_contribution, grant_access,
)
from app.models.schemas import EditSentenceRequest, EditSentenceResult, EditLogEntry

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/sentences", tags=["edits"])


@router.put("/{sentence_id}", response_model=EditSentenceResult)
async def submit_revision(
    sentence_id: int,
    req: EditSentenceRequest,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Submit a revision. Creates a new revision entry (not direct update)."""
    if req.field not in ("text_de", "text_zh"):
        raise HTTPException(status_code=400, detail="无效字段")

    result = await db.execute(
        select(Sentence).where(Sentence.id == sentence_id).options(
            selectinload(Sentence.paragraph).selectinload(Paragraph.lecture)
        )
    )
    sentence = result.scalar_one_or_none()
    if not sentence:
        raise HTTPException(status_code=404, detail="句子不存在")

    lecture = sentence.paragraph.lecture
    if not lecture.is_published:
        raise HTTPException(status_code=400, detail="译文尚未公开，无法编辑")

    price_key = "edit_source_coefficient" if req.field == "text_de" else "edit_translation_coefficient"
    cost = await compute_price(db, price_key, 1)

    try:
        deduct_result = await atomic_deduct_credits(
            user.raw_token, cost,
            reference_id=f"edit-sentence-{sentence_id}",
            description=f"修订句子 #{sentence_id}",
        )
    if "error" in deduct_result:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足，需要 {cost} 点"
        )

    # Compute hash and anchor from original text for persistence
    original_text = getattr(sentence, req.field) or ""
    normalized = re.sub(r'\s+', ' ', original_text).strip()
    text_hash = hashlib.sha256(normalized.encode()).hexdigest()
    anchor = (normalized[:60] + "|" + normalized[-60:])[:200]

    # Create revision (not direct update of sentence)
    rev = SentenceRevision(
        sentence_id=sentence_id,
        field=req.field,
        new_value=req.new_value,
        user_id=user.id,
        status="active",
        vote_count=1,
        text_hash=text_hash,
        text_anchor=anchor,
    )
    db.add(rev)
    await db.flush()

    # Auto-vote: submitter votes for their own revision
    db.add(RevisionVote(revision_id=rev.id, user_id=user.id))

    # Record contribution
    await add_contribution(db, user.id, lecture.id, "revision")
    await grant_access(db, user.id, lecture.id, "reviser")

    # Write audit log
    db.add(EditAuditLog(
        user_id=user.id,
        sentence_id=sentence_id,
        field_changed=req.field,
        old_value=getattr(sentence, req.field),
        new_value=req.new_value,
        credits_cost=cost,
    ))

    await db.commit()

    return EditSentenceResult(
        success=True,
        new_text=req.new_value,
        cost=cost,
        credits_remaining=deduct_result.get("credits", 0),
    )


@router.post("/{sentence_id}/revisions/{revision_id}/vote")
async def vote_revision(
    sentence_id: int,
    revision_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Vote for a revision. Costs same credits as submitting a revision."""
    rev_result = await db.execute(
        select(SentenceRevision).where(
            SentenceRevision.id == revision_id,
            SentenceRevision.sentence_id == sentence_id,
            SentenceRevision.status == "active",
        )
    )
    rev = rev_result.scalar_one_or_none()
    if not rev:
        raise HTTPException(status_code=404, detail="修订不存在或已被拒绝")

    if rev.user_id == user.id and False:  # self-vote already counted on submit
        pass

    # Check if already voted
    existing = await db.execute(
        select(RevisionVote).where(
            RevisionVote.revision_id == revision_id,
            RevisionVote.user_id == user.id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="您已投过票")

    # Deduct credits (same cost as submitting)
    price_key = "edit_source_coefficient" if rev.field == "text_de" else "edit_translation_coefficient"
    cost = await compute_price(db, price_key, 1)

    try:
        deduct_result = await atomic_deduct_credits(
            user.raw_token, cost,
            reference_id=f"vote-revision-{revision_id}",
            description=f"投票修订 #{revision_id}",
        )
    except ValueError:
        raise HTTPException(status_code=402, detail=f"点数不足，需要 {cost} 点")

    db.add(RevisionVote(revision_id=revision_id, user_id=user.id))
    rev.vote_count = (rev.vote_count or 0) + 1
    await db.commit()

    return {"success": True, "vote_count": rev.vote_count, "credits_remaining": deduct_result.get("credits", 0)}


@router.post("/{sentence_id}/revisions/{revision_id}/reject")
async def reject_revision(
    sentence_id: int,
    revision_id: int,
    admin: AuthUser = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Admin rejects a revision (hides it from voting)."""
    rev_result = await db.execute(
        select(SentenceRevision).where(
            SentenceRevision.id == revision_id,
            SentenceRevision.sentence_id == sentence_id,
        )
    )
    rev = rev_result.scalar_one_or_none()
    if not rev:
        raise HTTPException(status_code=404, detail="修订不存在")
    rev.status = "rejected"
    await db.commit()
    return {"success": True, "message": "修订已拒绝"}


@router.get("/{sentence_id}/revisions")
async def get_revisions(
    sentence_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get all active revisions for a sentence, sorted by votes."""
    result = await db.execute(
        select(SentenceRevision)
        .where(
            SentenceRevision.sentence_id == sentence_id,
            SentenceRevision.status == "active",
        )
        .order_by(SentenceRevision.vote_count.desc(), SentenceRevision.created_at.desc())
    )
    rows = result.all()
    return [
        {
            "id": r.id,
            "field": r.field,
            "new_value": r.new_value,
            "user_id": r.user_id,
            "username": "",
            "vote_count": r.vote_count or 0,
            "created_at": r.created_at,
        }
        for r in rows
    ]


@router.get("/{sentence_id}/edits")
async def get_sentence_edits(
    sentence_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get edit history for a sentence."""
    result = await db.execute(
        select(EditAuditLog)
        .where(EditAuditLog.sentence_id == sentence_id)
        .order_by(EditAuditLog.created_at.desc())
    )
    rows = result.all()
    return [
        EditLogEntry(
            id=row.id,
            user_id=row.user_id,
            username=username,
            sentence_id=row.sentence_id,
            field_changed=row.field_changed,
            old_value=row.old_value,
            new_value=row.new_value,
            credits_cost=row.credits_cost,
            created_at=row.created_at,
        )
        for row in rows
    ]
