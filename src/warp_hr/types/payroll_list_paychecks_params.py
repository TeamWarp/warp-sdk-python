# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .public_payroll_type import PublicPayrollType
from .public_paycheck_status import PublicPaycheckStatus
from .public_paycheck_payment_method import PublicPaycheckPaymentMethod
from .public_payroll_currency import PublicPayrollCurrency
from .public_pay_frequency import PublicPayFrequency

__all__ = ["PayrollListPaychecksParams"]


class PayrollListPaychecksParams(TypedDict, total=False):
    limit: Required[Optional[str]]
    """The maximum number of paychecks to return, from 1 to 50."""

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """Return paychecks after this paycheck ID in the stable cursor order. Cannot be used with beforeId."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """Return paychecks before this paycheck ID in the stable cursor order. Cannot be used with afterId."""

    payroll_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="payrollIds")]
    """Payrolls whose paychecks should be included."""

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]
    """Workers whose paychecks should be included."""

    worker_types: Annotated[
        Optional[List[Literal["us_w2", "us_1099", "global_contractor", "eor_employee"]]],
        PropertyInfo(alias="workerTypes"),
    ]
    """Worker classifications in effect for the paycheck to include. Omit to include every worker type visible to the API key."""

    payroll_types: Annotated[Optional[List[PublicPayrollType]], PropertyInfo(alias="payrollTypes")]
    """Payroll calculation types to include, subject to the API key permissions."""

    statuses: Optional[List[PublicPaycheckStatus]]
    """Lifecycle statuses to include. Omit to include every status."""

    payment_methods: Annotated[Optional[List[PublicPaycheckPaymentMethod]], PropertyInfo(alias="paymentMethods")]
    """Payment methods to include."""

    compensation_currencies: Annotated[
        Optional[List[PublicPayrollCurrency]], PropertyInfo(alias="compensationCurrencies")
    ]
    """Paycheck compensation currencies to include."""

    pay_frequencies: Annotated[Optional[List[PublicPayFrequency]], PropertyInfo(alias="payFrequencies")]
    """Pay cadences to include."""

    payday_on_or_after: Annotated[Optional[str], PropertyInfo(alias="paydayOnOrAfter")]
    """Inclusive start of the half-open payday range."""

    payday_before: Annotated[Optional[str], PropertyInfo(alias="paydayBefore")]
    """Exclusive end of the half-open payday range."""
