# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency
from .public_currency_money_amount_13 import PublicCurrencyMoneyAmount13
from .public_currency_money_amount_12 import PublicCurrencyMoneyAmount12
from .public_currency_money_amount_14 import PublicCurrencyMoneyAmount14
from .public_currency_money_amount_15 import PublicCurrencyMoneyAmount15
from .public_currency_money_amount_16 import PublicCurrencyMoneyAmount16
from .public_currency_money_amount_17 import PublicCurrencyMoneyAmount17
from .public_currency_money_amount_18 import PublicCurrencyMoneyAmount18
from .public_currency_money_amount_19 import PublicCurrencyMoneyAmount19
from .public_currency_money_amount_20 import PublicCurrencyMoneyAmount20

__all__ = ["PublicPaycheckCurrencyTotals", "Currency"]


class Currency(BaseModel):
    pass


class PublicPaycheckCurrencyTotals(BaseModel):
    """Paycheck category totals in one currency. Every category is present, including zero-valued categories; netPay is null until known."""

    currency: Currency

    gross_pay: PublicCurrencyMoneyAmount13 = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[PublicCurrencyMoneyAmount12] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""

    reimbursements: PublicCurrencyMoneyAmount14
    """Amounts reimbursed to the worker in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: PublicCurrencyMoneyAmount15 = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from the worker's pay, reducing net pay."""

    employer_taxes: PublicCurrencyMoneyAmount16 = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: PublicCurrencyMoneyAmount17 = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: PublicCurrencyMoneyAmount18 = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay after taxes, reducing net pay."""

    worker_benefit_contributions: PublicCurrencyMoneyAmount19 = FieldInfo(alias="workerBenefitContributions")
    """Amounts the worker pays toward benefits, deducted from their pay."""

    employer_benefit_contributions: PublicCurrencyMoneyAmount20 = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward the worker's benefits in addition to gross pay."""
