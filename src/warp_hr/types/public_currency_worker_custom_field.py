# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicCurrencyWorkerCustomField"]


class PublicCurrencyWorkerCustomField(BaseModel):
    type: Literal["currency"]

    id: str
    """The tag of a company custom worker field."""

    name: str

    redacted: bool
    """True when this API key’s permission scopes cannot read the field’s category. The value fields are withheld (null), not absent — null does not imply the worker has no value."""

    display: Optional[str] = None
    """The value rendered as the Warp dashboard displays it; null when unset or redacted."""

    amount: Optional[int] = None
    """The amount in integer base units of currencyCode (e.g. cents); null when unset or when the field is redacted for this API key."""

    currency_code: Optional[
        Literal[
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
    ] = FieldInfo(alias="currencyCode", default=None)
    """The amount’s currency; null when unset or when the field is redacted for this API key."""
