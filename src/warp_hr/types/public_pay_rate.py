# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .benefits.public_worker_reference import PublicWorkerReference
from .public_pay_rate_type import PublicPayRateType
from .public_pay_rate_per import PublicPayRatePer

__all__ = ["PublicPayRate"]


class PublicPayRate(BaseModel):
    """A regular or additional pay rate assigned to a worker."""

    id: str
    """The pay rate id."""

    worker: PublicWorkerReference
    """Basic identifying information for a worker associated with another resource."""

    type: PublicPayRateType
    """Whether the rate is the worker's regular base compensation or an additional rate such as a bonus, commission, or stipend."""

    per: PublicPayRatePer
    """The period represented by the pay rate amount."""

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

    effective_start_date: Optional[str] = FieldInfo(alias="effectiveStartDate", default=None)
    """The first date on which the rate applies. Additional rates may have no start date."""

    effective_end_date: Optional[str] = FieldInfo(alias="effectiveEndDate", default=None)
    """The first date on which the rate no longer applies, or null when it is open-ended."""

    description: Optional[str] = None
    """A human-readable label for the pay rate, when one is configured."""
