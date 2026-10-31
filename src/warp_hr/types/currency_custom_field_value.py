# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CurrencyCustomFieldValue"]


class CurrencyCustomFieldValue(BaseModel):
    type: Literal["currency"]

    amount: int
    """Integer base units of currencyCode (e.g. cents)."""

    currency_code: Literal[
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
    ] = FieldInfo(alias="currencyCode")
