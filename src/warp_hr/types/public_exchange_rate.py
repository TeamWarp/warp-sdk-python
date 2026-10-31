# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_currency import PublicPayrollCurrency
from .public_exchange_rate_value import PublicExchangeRateValue

__all__ = ["PublicExchangeRate", "FromCurrency", "ToCurrency", "Rate"]


class Rate(BaseModel):
    pass


class ToCurrency(BaseModel):
    pass


class FromCurrency(BaseModel):
    pass


class PublicExchangeRate(BaseModel):
    """A directed exchange rate where a fromCurrency major-unit amount multiplied by rate equals its toCurrency equivalent."""

    from_currency: FromCurrency = FieldInfo(alias="fromCurrency")

    to_currency: ToCurrency = FieldInfo(alias="toCurrency")

    rate: Rate
