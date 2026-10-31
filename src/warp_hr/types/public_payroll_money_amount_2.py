# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicPayrollMoneyAmount2", "Currency"]


class Currency(BaseModel):
    pass


class PublicPayrollMoneyAmount2(BaseModel):
    """The amount reimbursed to the worker on this paycheck in the amount's currency. It may differ from the currency of the original expense."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: Currency

    display: str
    """The server-formatted display string for the amount in its currency."""
