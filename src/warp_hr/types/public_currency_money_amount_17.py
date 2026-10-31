# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount17"]


class PublicCurrencyMoneyAmount17(BaseModel):
    """Non-benefit amounts deducted from the worker's pay before taxes, reducing taxable pay and net pay."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
