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
from .public_paycheck_summary_totals import PublicPaycheckSummaryTotals

__all__ = [
    "PublicPaycheckSummary",
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
]


class TotalsInFundingCurrencyCurrency(BaseModel):
    pass


class TotalsInFundingCurrency(BaseModel):
    currency: TotalsInFundingCurrencyCurrency

    net_pay: Optional[object] = FieldInfo(alias="netPay", default=None)
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""


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


class PublicPaycheckSummary(BaseModel):
    """A compact per-worker paycheck within a payroll."""

    id: str
    """The tag of the paycheck."""

    payroll: Payroll

    worker: Worker

    status: Status

    payday: str

    payment_method: PaymentMethod = FieldInfo(alias="paymentMethod")

    totals: Totals
