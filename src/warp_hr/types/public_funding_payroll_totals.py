# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_currency_money_amount import PublicCurrencyMoneyAmount
from .public_currency_money_amount_1 import PublicCurrencyMoneyAmount1
from .public_currency_money_amount_2 import PublicCurrencyMoneyAmount2
from .public_currency_money_amount_3 import PublicCurrencyMoneyAmount3
from .public_currency_money_amount_4 import PublicCurrencyMoneyAmount4
from .public_currency_money_amount_5 import PublicCurrencyMoneyAmount5
from .public_currency_money_amount_6 import PublicCurrencyMoneyAmount6

__all__ = ["PublicFundingPayrollTotals", "NetPay", "WorkerTaxes", "EmployerTaxes", "TotalCost"]


class TotalCost(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""


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


class PublicFundingPayrollTotals(BaseModel):
    """Payroll totals expressed in the parent payroll funding currency. Line-derived categories are subtotaled per paycheck in calculation currency, converted once per category, rounded to funding-currency minor units, and then summed. Net pay remains provider-authoritative."""

    gross_pay: PublicCurrencyMoneyAmount = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[NetPay] = FieldInfo(alias="netPay", default=None)
    """The provider-calculated amount to send for workers: gross pay plus reimbursements, less worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from recomputed totals because of provider and FX rounding. Null when any paycheck net pay is not yet known."""

    reimbursements: PublicCurrencyMoneyAmount1
    """Amounts reimbursed to workers in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: WorkerTaxes = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from worker pay, reducing net pay."""

    employer_taxes: EmployerTaxes = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: PublicCurrencyMoneyAmount2 = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from worker pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: PublicCurrencyMoneyAmount3 = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from worker pay after taxes, reducing net pay."""

    worker_benefit_contributions: PublicCurrencyMoneyAmount4 = FieldInfo(alias="workerBenefitContributions")
    """Amounts workers pay toward benefits, deducted from their pay."""

    employer_benefit_contributions: PublicCurrencyMoneyAmount5 = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward worker benefits in addition to gross pay."""

    transaction_fees: PublicCurrencyMoneyAmount6 = FieldInfo(alias="transactionFees")
    """Banking and transaction fees paid by the employer to fund and pay the payroll."""

    total_cost: TotalCost = FieldInfo(alias="totalCost")
    """The employer's total payroll cost: gross pay, reimbursements, employer taxes, employer benefit contributions, and transaction fees."""
