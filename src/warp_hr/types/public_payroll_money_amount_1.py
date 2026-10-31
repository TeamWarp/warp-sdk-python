# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicPayrollMoneyAmount1", "Currency"]


class Currency(BaseModel):
    pass


class PublicPayrollMoneyAmount1(BaseModel):
    """An amount in ISO currency minor units with a server-formatted display value."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: Currency

    display: str
    """The server-formatted display string for the amount in its currency."""
