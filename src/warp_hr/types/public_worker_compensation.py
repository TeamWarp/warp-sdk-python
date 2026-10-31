# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_pay_rate_per import PublicPayRatePer

__all__ = ["PublicWorkerCompensation", "Per"]


class Per(BaseModel):
    pass


class PublicWorkerCompensation(BaseModel):
    """The worker's current regular pay rate. For a worker whose start date is in the future, this is the regular rate effective on their start date. Null when no regular rate applies or when the API key lacks the corresponding US or global compensation read scope."""

    pay_rate_id: str = FieldInfo(alias="payRateId")
    """The tag of the pay rate."""

    per: Per

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: Literal[
        "USD",
        "AUD",
        "BGN",
        "BRL",
        "CAD",
        "CHF",
        "CZK",
        "DKK",
        "EUR",
        "GBP",
        "HKD",
        "HUF",
        "IDR",
        "INR",
        "JPY",
        "MYR",
        "NOK",
        "NZD",
        "CNY",
        "PLN",
        "RON",
        "TRY",
        "SEK",
        "SGD",
        "AED",
        "ARS",
        "BDT",
        "BWP",
        "CLP",
        "COP",
        "CRC",
        "EGP",
        "FJD",
        "GEL",
        "GHS",
        "ILS",
        "KES",
        "KRW",
        "LKR",
        "MAD",
        "MXN",
        "NPR",
        "PHP",
        "PKR",
        "THB",
        "UAH",
        "UGX",
        "UYU",
        "VND",
        "ZAR",
        "ZMW",
        "TND",
        "NGN",
        "RSD",
        "TWD",
        "GTQ",
        "HNL",
        "DOP",
        "SAR",
        "XAF",
        "PEN",
    ]

    display: str
    """The server-formatted pay rate, including its period."""
