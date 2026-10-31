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

__all__ = ["PublicPaycheckPayroll", "Type", "Subtype", "Status", "FundingCurrency", "PayPeriod"]


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


class PublicPaycheckPayroll(BaseModel):
    """The parent payroll context for a paycheck."""

    id: str
    """The tag of the payroll."""

    type: Type

    subtype: Subtype

    status: Status

    funding_currency: FundingCurrency = FieldInfo(alias="fundingCurrency")

    pay_period: PayPeriod = FieldInfo(alias="payPeriod")

    pay_frequency: Optional[PublicPayFrequency] = FieldInfo(alias="payFrequency", default=None)
    """The cadence at which workers are paid."""
