# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency
from .public_currency_money_amount_7 import PublicCurrencyMoneyAmount7
from .public_currency_money_amount_8 import PublicCurrencyMoneyAmount8
from .public_currency_money_amount_9 import PublicCurrencyMoneyAmount9
from .public_currency_money_amount_10 import PublicCurrencyMoneyAmount10
from .public_currency_money_amount_11 import PublicCurrencyMoneyAmount11
from .public_currency_money_amount_12 import PublicCurrencyMoneyAmount12

__all__ = ["PublicPaycheckCurrencyTotals", "Currency", "NetPay", "WorkerTaxes", "EmployerTaxes"]


class EmployerTaxes(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""


class WorkerTaxes(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""


class NetPay(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""


class Currency(BaseModel):
    pass


class PublicPaycheckCurrencyTotals(BaseModel):
    """Paycheck category totals in one currency. Every category is present, including zero-valued categories; netPay is null until known."""

    currency: Currency

    gross_pay: PublicCurrencyMoneyAmount7 = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[NetPay] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""

    reimbursements: PublicCurrencyMoneyAmount8
    """Amounts reimbursed to the worker in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: WorkerTaxes = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from the worker's pay, reducing net pay."""

    employer_taxes: EmployerTaxes = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: PublicCurrencyMoneyAmount9 = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: PublicCurrencyMoneyAmount10 = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from the worker's pay after taxes, reducing net pay."""

    worker_benefit_contributions: PublicCurrencyMoneyAmount11 = FieldInfo(alias="workerBenefitContributions")
    """Amounts the worker pays toward benefits, deducted from their pay."""

    employer_benefit_contributions: PublicCurrencyMoneyAmount12 = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward the worker's benefits in addition to gross pay."""
