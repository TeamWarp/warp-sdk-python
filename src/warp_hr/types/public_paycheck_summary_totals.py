# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_paycheck_summary_currency_totals import PublicPaycheckSummaryCurrencyTotals

__all__ = ["PublicPaycheckSummaryTotals", "InFundingCurrency", "InFundingCurrencyCurrency"]


class InFundingCurrencyCurrency(BaseModel):
    pass


class InFundingCurrency(BaseModel):
    currency: InFundingCurrencyCurrency

    net_pay: Optional[object] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""


class PublicPaycheckSummaryTotals(BaseModel):
    """Compact paycheck totals in calculation and payroll funding currencies."""

    by_currency: object = FieldInfo(alias="byCurrency")

    in_funding_currency: InFundingCurrency = FieldInfo(alias="inFundingCurrency")
