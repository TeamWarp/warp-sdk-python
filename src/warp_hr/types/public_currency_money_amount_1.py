# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount1"]


class PublicCurrencyMoneyAmount1(BaseModel):
    """The provider-calculated amount to send for workers: gross pay plus reimbursements, less worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from recomputed totals because of provider and FX rounding. Null when any paycheck net pay is not yet known."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
