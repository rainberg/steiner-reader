"""Thin wrapper re-exporting credit_service functions for backward compatibility.

The translate router imports from app.services.auth_client, so this module
delegates to the canonical credit_service implementations.
"""

from app.services.credit_service import (
    reserve_credits,
    settle_credits,
    refund_credits,
    get_balance as get_credits_balance,
)

__all__ = [
    "reserve_credits",
    "settle_credits",
    "refund_credits",
    "get_credits_balance",
]
