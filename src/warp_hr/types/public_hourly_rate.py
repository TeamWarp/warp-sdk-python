# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

from .public_hourly_rate_amount import PublicHourlyRateAmount
from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicHourlyRate", "Amount", "Currency"]


class Currency(BaseModel):
    pass


class Amount(BaseModel):
    pass


class PublicHourlyRate(BaseModel):
    """A non-negative major-unit hourly rate. The earning amount remains authoritative."""

    amount: Amount

    currency: Currency

    per: Literal["hour"]
