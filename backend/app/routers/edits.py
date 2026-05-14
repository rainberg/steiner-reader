"""Sentence editing router — edit source or translation text with credit cost."""

import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import User, Sentence, Paragraph, Lecture, EditAuditLog
from app.routers.auth import require_user
from app.services.credit_service import (
    get_credit_price, atomic_deduct_credits, add_contribution, grant_access,
)
from app.models.schemas import EditSentenceRequest, EditSentenceResult, EditLogEntry

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/sentences", tags=["edits"])

VALID_FIELDS = {"text_de": "edit_source_sentence", "text_zh": "edit_translation_sentence"}
FIELD_LABELS = {"text_de": "原文", "text_zh": "译文"}


@router.put("/{sentence_id}", response_model=EditSentenceResult)
async def edit_sentence(
    sentence_id: int,
    req: EditSentenceRequest,
    user: User = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """Edit a sentence's source or translation text. Costs credits per edit."""
    if req.field not in VALID_FIELDS:
        raise HTTPException(status_code=400, detail="无效的编辑字段，只允许 text_de 或 text_zh")

    # Fetch sentence with its parent paragraph and lecture
    result = await db.execute(
        select(Sentence)
        .where(Sentence.id == sentence_id)
        .options(
            selectinload(Sentence.paragraph).selectinload(Paragraph.lecture)
        )
    )
    sentence = result.scalar_one_or_none()
    if not sentence:
        raise HTTPException(status_code=404, detail="句子不存在")

    lecture = sentence.paragraph.lecture
    if not lecture.is_published:
        raise HTTPException(status_code=400, detail="译文尚未公开，无法编辑")

    price_key = VALID_FIELDS[req.field]
    cost = await get_credit_price(db, price_key)

    old_value = getattr(sentence, req.field)

    try:
        new_credits = await atomic_deduct_credits(
            db, user, cost,
            transaction_type=f"edit_{'source' if req.field == 'text_de' else 'translation'}",
            reference_type="sentence",
            reference_id=sentence_id,
            description=f"编辑{lecture.title_de or lecture.id}句子{FIELD_LABELS[req.field]}",
        )
    except ValueError:
        raise HTTPException(
            status_code=402,
            detail=f"点数不足：编辑{FIELD_LABELS[req.field]}需要 {cost} 点，当前余额 {user.credits} 点"
        )

    # Update the sentence
    setattr(sentence, req.field, req.new_value)

    # Write audit log
    db.add(EditAuditLog(
        user_id=user.id,
        sentence_id=sentence_id,
        field_changed=req.field,
        old_value=old_value,
        new_value=req.new_value,
        credits_cost=cost,
    ))

    # Record contribution and grant download access
    await add_contribution(db, user.id, lecture.id, "revision")
    await grant_access(db, user.id, lecture.id, "reviser")

    await db.commit()

    return EditSentenceResult(
        success=True,
        new_text=req.new_value,
        cost=cost,
        credits_remaining=new_credits,
    )


@router.get("/{sentence_id}/edits")
async def get_sentence_edits(
    sentence_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get edit history for a sentence."""
    result = await db.execute(
        select(EditAuditLog, User.username)
        .join(User, EditAuditLog.user_id == User.id)
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
        for row, username in rows
    ]
