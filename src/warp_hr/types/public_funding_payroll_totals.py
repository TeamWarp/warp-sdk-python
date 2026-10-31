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
from .public_currency_money_amount_7 import PublicCurrencyMoneyAmount7
from .public_currency_money_amount_8 import PublicCurrencyMoneyAmount8
from .public_currency_money_amount_9 import PublicCurrencyMoneyAmount9
from .public_currency_money_amount_10 import PublicCurrencyMoneyAmount10

__all__ = ["PublicFundingPayrollTotals"]


class PublicFundingPayrollTotals(BaseModel):
    """Payroll totals expressed in the parent payroll funding currency. Line-derived categories are subtotaled per paycheck in calculation currency, converted once per category, rounded to funding-currency minor units, and then summed. Net pay remains provider-authoritative."""

    gross_pay: PublicCurrencyMoneyAmount = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[PublicCurrencyMoneyAmount1] = FieldInfo(alias="netPay", default=None)
    """The provider-calculated amount to send for workers: gross pay plus reimbursements, less worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from recomputed totals because of provider and FX rounding. Null when any paycheck net pay is not yet known."""

    reimbursements: PublicCurrencyMoneyAmount2
    """Amounts reimbursed to workers in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: PublicCurrencyMoneyAmount3 = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from worker pay, reducing net pay."""

    employer_taxes: PublicCurrencyMoneyAmount4 = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: PublicCurrencyMoneyAmount5 = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from worker pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: PublicCurrencyMoneyAmount6 = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from worker pay after taxes, reducing net pay."""

    worker_benefit_contributions: PublicCurrencyMoneyAmount7 = FieldInfo(alias="workerBenefitContributions")
    """Amounts workers pay toward benefits, deducted from their pay."""

    employer_benefit_contributions: PublicCurrencyMoneyAmount8 = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward worker benefits in addition to gross pay."""

    transaction_fees: PublicCurrencyMoneyAmount9 = FieldInfo(alias="transactionFees")
    """Banking and transaction fees paid by the employer to fund and pay the payroll."""

    total_cost: PublicCurrencyMoneyAmount10 = FieldInfo(alias="totalCost")
    """The employer's total payroll cost: gross pay, reimbursements, employer taxes, employer benefit contributions, and transaction fees."""
