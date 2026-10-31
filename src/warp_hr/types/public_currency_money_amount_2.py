# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount2"]


class PublicCurrencyMoneyAmount2(BaseModel):
    """Amounts reimbursed to workers in addition to gross pay. Reimbursements increase net pay and employer cost."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
