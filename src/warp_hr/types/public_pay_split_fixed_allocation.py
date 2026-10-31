# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicPaySplitFixedAllocation"]


class PublicPaySplitFixedAllocation(BaseModel):
    type: Literal["amount"]

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
    """The server-formatted display string for the amount in its currency."""
