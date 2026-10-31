# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicPayrollMoneyAmount3", "Currency"]


class Currency(BaseModel):
    pass


class PublicPayrollMoneyAmount3(BaseModel):
    """The amount deducted from the worker's pay on this line in the amount's currency."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: Currency

    display: str
    """The server-formatted display string for the amount in its currency."""
