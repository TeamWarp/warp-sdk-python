# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .public_payroll_type import PublicPayrollType
from .public_payroll_subtype import PublicPayrollSubtype
from .public_payroll_status import PublicPayrollStatus
from .public_pay_frequency import PublicPayFrequency

__all__ = ["PayrollListParams"]


class PayrollListParams(TypedDict, total=False):
    limit: Required[Optional[str]]
    """The maximum number of payrolls to return, from 1 to 50."""

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """Return payrolls after this payroll ID in the stable cursor order. Cannot be used with beforeId."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """Return payrolls before this payroll ID in the stable cursor order. Cannot be used with afterId."""

    types: Optional[List[PublicPayrollType]]
    """Payroll calculation types to include."""

    subtypes: Optional[List[PublicPayrollSubtype]]
    """Payroll subtypes to include."""

    statuses: Optional[List[PublicPayrollStatus]]
    """Lifecycle statuses to include. Omit to include every status."""

    pay_frequencies: Annotated[Optional[List[PublicPayFrequency]], PropertyInfo(alias="payFrequencies")]
    """Pay cadences to include."""

    payday_on_or_after: Annotated[Optional[str], PropertyInfo(alias="paydayOnOrAfter")]
    """Inclusive start of the half-open payday range."""

    payday_before: Annotated[Optional[str], PropertyInfo(alias="paydayBefore")]
    """Exclusive end of the half-open payday range."""

    pay_period_end_on_or_after: Annotated[Optional[str], PropertyInfo(alias="payPeriodEndOnOrAfter")]
    """Inclusive start of the half-open pay-period-end range."""

    pay_period_end_before: Annotated[Optional[str], PropertyInfo(alias="payPeriodEndBefore")]
    """Exclusive end of the half-open pay-period-end range."""
