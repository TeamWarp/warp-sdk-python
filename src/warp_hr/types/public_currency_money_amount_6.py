# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount6"]


class PublicCurrencyMoneyAmount6(BaseModel):
    """Non-benefit amounts deducted from worker pay after taxes, reducing net pay."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
