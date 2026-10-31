# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount10"]


class PublicCurrencyMoneyAmount10(BaseModel):
    """The employer's total payroll cost: gross pay, reimbursements, employer taxes, employer benefit contributions, and transaction fees."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
