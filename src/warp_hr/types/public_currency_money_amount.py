# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount"]


class PublicCurrencyMoneyAmount(BaseModel):
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
