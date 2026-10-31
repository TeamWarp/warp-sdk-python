# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency
from .public_currency_money_amount_12 import PublicCurrencyMoneyAmount12

__all__ = ["PublicPaycheckSummaryCurrencyTotals", "Currency"]


class Currency(BaseModel):
    pass


class PublicPaycheckSummaryCurrencyTotals(BaseModel):
    """Compact paycheck totals in one calculation currency."""

    currency: Currency

    net_pay: Optional[PublicCurrencyMoneyAmount12] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""
