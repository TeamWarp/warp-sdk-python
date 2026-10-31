# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_paycheck_currency_totals import PublicPaycheckCurrencyTotals

__all__ = ["PublicPaycheckDetailTotals", "InFundingCurrency", "InFundingCurrencyCurrency"]


class InFundingCurrencyCurrency(BaseModel):
    pass


class InFundingCurrency(BaseModel):
    currency: InFundingCurrencyCurrency

    gross_pay: object = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[object] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""

    reimbursements: object
    """Amounts reimbursed to the worker in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: object = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from the worker's pay, reducing net pay."""

    employer_taxes: object = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: object = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: object = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay after taxes, reducing net pay."""

    worker_benefit_contributions: object = FieldInfo(alias="workerBenefitContributions")
    """Amounts the worker pays toward benefits, deducted from their pay."""

    employer_benefit_contributions: object = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward the worker's benefits in addition to gross pay."""


class PublicPaycheckDetailTotals(BaseModel):
    """Detailed paycheck totals in calculation and payroll funding currencies."""

    by_currency: object = FieldInfo(alias="byCurrency")

    in_funding_currency: InFundingCurrency = FieldInfo(alias="inFundingCurrency")
