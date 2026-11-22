# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicPaycheckSummaryCurrencyTotals", "Currency", "NetPay"]


class NetPay(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""


class Currency(BaseModel):
    pass


class PublicPaycheckSummaryCurrencyTotals(BaseModel):
    """Compact paycheck totals in one calculation currency."""

    currency: Currency

    net_pay: Optional[NetPay] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""
