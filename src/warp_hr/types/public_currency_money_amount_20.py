# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount20"]


class PublicCurrencyMoneyAmount20(BaseModel):
    """Amounts the employer pays toward the worker's benefits in addition to gross pay."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
