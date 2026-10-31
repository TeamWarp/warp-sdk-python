# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_paycheck_payroll import PublicPaycheckPayroll
from .public_paycheck_worker import PublicPaycheckWorker
from .public_paycheck_status import PublicPaycheckStatus
from .public_paycheck_payment_method import PublicPaycheckPaymentMethod
from .public_paycheck_detail_totals import PublicPaycheckDetailTotals
from .public_payroll_currency import PublicPayrollCurrency

__all__ = [
    "PublicPaycheckDetail",
    "Payroll",
    "PayrollType",
    "PayrollSubtype",
    "PayrollStatus",
    "PayrollFundingCurrency",
    "PayrollPayPeriod",
    "Worker",
    "Status",
    "PaymentMethod",
    "Totals",
    "TotalsInFundingCurrency",
    "TotalsInFundingCurrencyCurrency",
    "YearToDate",
    "YearToDateTotals",
    "YearToDateTotalsGrossPay",
    "YearToDateTotalsGrossPayCurrency",
    "YearToDateTotalsNetPay",
    "YearToDateTotalsNetPayCurrency",
    "YearToDateTotalsWorkerTaxes",
    "YearToDateTotalsWorkerTaxesCurrency",
    "YearToDateTotalsWorkerBenefitContributions",
    "YearToDateTotalsWorkerBenefitContributionsCurrency",
    "YearToDateTotalsReimbursements",
    "YearToDateTotalsReimbursementsCurrency",
    "YearToDateTotalsPostTaxDeductions",
    "YearToDateTotalsPostTaxDeductionsCurrency",
]


class YearToDateTotalsPostTaxDeductionsCurrency(BaseModel):
    pass


class YearToDateTotalsPostTaxDeductions(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsPostTaxDeductionsCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotalsReimbursementsCurrency(BaseModel):
    pass


class YearToDateTotalsReimbursements(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsReimbursementsCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotalsWorkerBenefitContributionsCurrency(BaseModel):
    pass


class YearToDateTotalsWorkerBenefitContributions(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsWorkerBenefitContributionsCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotalsWorkerTaxesCurrency(BaseModel):
    pass


class YearToDateTotalsWorkerTaxes(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsWorkerTaxesCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotalsNetPayCurrency(BaseModel):
    pass


class YearToDateTotalsNetPay(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsNetPayCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotalsGrossPayCurrency(BaseModel):
    pass


class YearToDateTotalsGrossPay(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: YearToDateTotalsGrossPayCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class YearToDateTotals(BaseModel):
    gross_pay: YearToDateTotalsGrossPay = FieldInfo(alias="grossPay")
    """Gross earnings year-to-date for the selected paystub."""

    net_pay: YearToDateTotalsNetPay = FieldInfo(alias="netPay")
    """Net pay year-to-date for the selected paystub."""

    worker_taxes: YearToDateTotalsWorkerTaxes = FieldInfo(alias="workerTaxes")
    """Employee taxes withheld year-to-date for the selected paystub."""

    worker_benefit_contributions: YearToDateTotalsWorkerBenefitContributions = FieldInfo(
        alias="workerBenefitContributions"
    )
    """Employee benefit contributions year-to-date for the selected paystub."""

    reimbursements: YearToDateTotalsReimbursements
    """Reimbursements year-to-date for the selected paystub."""

    post_tax_deductions: YearToDateTotalsPostTaxDeductions = FieldInfo(alias="postTaxDeductions")
    """Post-tax deductions year-to-date for the selected paystub."""


class YearToDate(BaseModel):
    as_of_date: str = FieldInfo(alias="asOfDate")

    totals: YearToDateTotals
    """Provider-reported employee YTD category totals, in signed USD cents."""

    earnings: object

    taxes: object

    benefits: object

    reimbursements: object

    deductions: object


class TotalsInFundingCurrencyCurrency(BaseModel):
    pass


class TotalsInFundingCurrency(BaseModel):
    currency: TotalsInFundingCurrencyCurrency

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


class Totals(BaseModel):
    by_currency: object = FieldInfo(alias="byCurrency")

    in_funding_currency: TotalsInFundingCurrency = FieldInfo(alias="inFundingCurrency")


class PaymentMethod(BaseModel):
    pass


class Status(BaseModel):
    pass


class Worker(BaseModel):
    id: str
    """The worker id."""

    first_name: str = FieldInfo(alias="firstName")
    """The worker first name."""

    last_name: str = FieldInfo(alias="lastName")
    """The worker last name."""

    display_name: str = FieldInfo(alias="displayName")

    worker_type: Literal["us_w2", "us_1099", "global_contractor", "eor_employee"] = FieldInfo(alias="workerType")


class PayrollPayPeriod(BaseModel):
    start_date: str = FieldInfo(alias="startDate")

    end_date: str = FieldInfo(alias="endDate")


class PayrollFundingCurrency(BaseModel):
    pass


class PayrollStatus(BaseModel):
    pass


class PayrollSubtype(BaseModel):
    pass


class PayrollType(BaseModel):
    pass


class Payroll(BaseModel):
    id: str
    """The tag of the payroll."""

    type: PayrollType

    subtype: PayrollSubtype

    status: PayrollStatus

    funding_currency: PayrollFundingCurrency = FieldInfo(alias="fundingCurrency")

    pay_period: PayrollPayPeriod = FieldInfo(alias="payPeriod")

    pay_frequency: Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]] = (
        FieldInfo(alias="payFrequency", default=None)
    )
    """The cadence at which workers are paid."""


class PublicPaycheckDetail(BaseModel):
    """A paycheck with currency-specific calculation lines, totals grouped by currency, and authoritative parent-payroll funding-currency totals. Source currencies for expenses, benefits, or other inputs are outside this payroll-calculation resource."""

    id: str
    """The tag of the paycheck."""

    payroll: Payroll

    worker: Worker

    status: Status

    payday: str

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    totals: Totals

    year_to_date: Optional[YearToDate] = FieldInfo(alias="yearToDate", default=None)
    """Employee YTD amounts for the selected US W-2 paystub. Groups with a nonzero current or YTD amount are included, including historical-only groups with no amount on this paycheck."""

    description: Optional[str] = None

    exchange_rates: object = FieldInfo(alias="exchangeRates")

    reported_hours: Optional[float] = FieldInfo(alias="reportedHours", default=None)

    earnings: object

    reimbursements: object

    deductions: object

    benefits: object

    taxes: object
