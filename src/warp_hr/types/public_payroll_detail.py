# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_type import PublicPayrollType
from .public_payroll_subtype import PublicPayrollSubtype
from .public_payroll_status import PublicPayrollStatus
from .public_payroll_currency import PublicPayrollCurrency
from .public_pay_period import PublicPayPeriod
from .public_pay_frequency import PublicPayFrequency
from .public_payroll_detail_totals import PublicPayrollDetailTotals
from .public_payroll_funding_method import PublicPayrollFundingMethod
from .public_payroll_timeline import PublicPayrollTimeline

__all__ = [
    "PublicPayrollDetail",
    "Type",
    "Subtype",
    "Status",
    "FundingCurrency",
    "PayPeriod",
    "Totals",
    "FundingMethod",
    "Timeline",
]


class Timeline(BaseModel):
    approved_at: Optional[str] = FieldInfo(alias="approvedAt", default=None)


class FundingMethod(BaseModel):
    pass


class Totals(BaseModel):
    cash_requirement: Optional[object] = FieldInfo(alias="cashRequirement", default=None)
    """The provider-reported amount the employer must fund for the payroll, when available."""

    gross_pay: object = FieldInfo(alias="grossPay")
    """Gross earnings before worker taxes, deductions, and benefit contributions. Reimbursements are reported separately."""

    net_pay: Optional[object] = FieldInfo(alias="netPay", default=None)
    """The provider-calculated amount to send for workers: gross pay plus reimbursements, less worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from recomputed totals because of provider and FX rounding. Null when any paycheck net pay is not yet known."""

    reimbursements: object
    """Amounts reimbursed to workers in addition to gross pay. Reimbursements increase net pay and employer cost."""

    worker_taxes: object = FieldInfo(alias="workerTaxes")
    """Payroll taxes withheld from worker pay, reducing net pay."""

    employer_taxes: object = FieldInfo(alias="employerTaxes")
    """Payroll taxes paid by the employer in addition to gross pay."""

    pre_tax_deductions: object = FieldInfo(alias="preTaxDeductions")
    """Non-benefit amounts deducted from worker pay before taxes, reducing taxable pay and net pay."""

    post_tax_deductions: object = FieldInfo(alias="postTaxDeductions")
    """Non-benefit amounts deducted from worker pay after taxes, reducing net pay."""

    worker_benefit_contributions: object = FieldInfo(alias="workerBenefitContributions")
    """Amounts workers pay toward benefits, deducted from their pay."""

    employer_benefit_contributions: object = FieldInfo(alias="employerBenefitContributions")
    """Amounts the employer pays toward worker benefits in addition to gross pay."""

    transaction_fees: object = FieldInfo(alias="transactionFees")
    """Banking and transaction fees paid by the employer to fund and pay the payroll."""

    total_cost: object = FieldInfo(alias="totalCost")
    """The employer's total payroll cost: gross pay, reimbursements, employer taxes, employer benefit contributions, and transaction fees."""


class PayPeriod(BaseModel):
    start_date: str = FieldInfo(alias="startDate")

    end_date: str = FieldInfo(alias="endDate")


class FundingCurrency(BaseModel):
    pass


class Status(BaseModel):
    pass


class Subtype(BaseModel):
    pass


class Type(BaseModel):
    pass


class PublicPayrollDetail(BaseModel):
    """A payroll run with funding and lifecycle details. Every amount in totals is expressed in fundingCurrency; line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative."""

    id: str
    """The tag of the payroll."""

    type: Type

    subtype: Subtype

    status: Status

    funding_currency: FundingCurrency = FieldInfo(alias="fundingCurrency")

    payday: str

    pay_period: PayPeriod = FieldInfo(alias="payPeriod")

    pay_frequency: Optional[PublicPayFrequency] = FieldInfo(alias="payFrequency", default=None)
    """The cadence at which workers are paid."""

    description: Optional[str] = None

    approval_deadline: Optional[str] = FieldInfo(alias="approvalDeadline", default=None)

    paycheck_count: int = FieldInfo(alias="paycheckCount")

    totals: Totals

    funding_method: FundingMethod = FieldInfo(alias="fundingMethod")

    reopen_deadline: Optional[str] = FieldInfo(alias="reopenDeadline", default=None)

    timeline: Timeline
