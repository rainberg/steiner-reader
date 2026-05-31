import pytest
from decimal import Decimal
from app.services.credit_service import compute_price, add_contribution
from app.db.models import CreditSetting


class TestComputePrice:
    async def test_returns_price_when_setting_exists(self, db_session):
        db_session.add(CreditSetting(action="translate_per_lecture", price=Decimal("10.00"), description="翻译"))
        await db_session.flush()

        result = await compute_price(db_session, "translate_per_lecture")
        assert result == Decimal("10.00")

    async def test_raises_valueerror_when_setting_missing(self, db_session):
        with pytest.raises(ValueError, match="No credit setting found"):
            await compute_price(db_session, "nonexistent_action")

    async def test_returns_default_when_setting_missing_and_default_provided(self, db_session):
        result = await compute_price(db_session, "nonexistent_action", default=Decimal("5.00"))
        assert result == Decimal("5.00")

    async def test_returns_db_value_when_setting_exists_even_with_default(self, db_session):
        db_session.add(CreditSetting(action="download_per_lecture", price=Decimal("3.00"), description="下载"))
        await db_session.flush()

        result = await compute_price(db_session, "download_per_lecture", default=Decimal("5.00"))
        assert result == Decimal("3.00")


class TestAddContribution:
    async def test_creates_contribution_without_amount(self, db_session):
        entry = await add_contribution(
            db_session,
            user_id="user-123",
            lecture_id=1,
            access_type="translate",
            display_name="Test User",
            book_id=42,
            cost=10,
            grants_download=True,
        )
        assert entry.user_id == "user-123"
        assert entry.lecture_id == 1
        assert entry.contribution_type == "translate"
        assert entry.display_name == "Test User"
        assert entry.cost == 10
        assert entry.grants_download is True
