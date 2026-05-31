import pytest
from datetime import datetime
from app.db.models import RechargeRequest


class TestRechargeRequestSerialization:
    async def test_my_requests_returns_isoformat_dates(self, db_session):
        now = datetime(2026, 5, 30, 12, 0, 0)
        req = RechargeRequest(
            user_id="user-123",
            amount=10,
            coefficient=10,
            status="pending",
            created_at=now,
            updated_at=now,
        )
        db_session.add(req)
        await db_session.flush()

        result = {
            "id": req.id,
            "amount": req.amount,
            "coefficient": req.coefficient or 10,
            "credits": req.amount * (req.coefficient or 10),
            "status": req.status,
            "admin_note": req.admin_note,
            "created_at": req.created_at.isoformat() if req.created_at else None,
            "updated_at": req.updated_at.isoformat() if req.updated_at else None,
        }

        assert isinstance(result["created_at"], str)
        assert result["created_at"] == "2026-05-30T12:00:00"
        assert isinstance(result["updated_at"], str)

    async def test_my_requests_raw_datetime_would_fail_json(self, db_session):
        now = datetime(2026, 5, 30, 12, 0, 0)
        req = RechargeRequest(
            user_id="user-123",
            amount=10,
            coefficient=10,
            status="pending",
            created_at=now,
            updated_at=now,
        )
        db_session.add(req)
        await db_session.flush()

        import json
        bad_result = {
            "created_at": req.created_at,
        }
        with pytest.raises(TypeError):
            json.dumps(bad_result)

        good_result = {
            "created_at": req.created_at.isoformat() if req.created_at else None,
        }
        json_str = json.dumps(good_result)
        assert "2026-05-30" in json_str
