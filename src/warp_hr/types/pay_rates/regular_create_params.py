# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegularCreateParams"]


class RegularCreateParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """The worker whose regular pay rate will be created."""

    type: Required[Literal["salary", "monthly", "weekly", "hourly", "variable"]]
    """How the regular pay rate is measured. Salary represents an annual rate. Variable pay creates a dated boundary without a fixed pay-rate row and returns a null id."""

    amount: Optional[int]
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: Required[
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
            "COP",
            "CRC",
            "EGP",
            "FJD",
            "GEL",
            "GHS",
            "ILS",
            "KES",
            "LKR",
            "MAD",
            "MXN",
            "NPR",
            "PHP",
            "PKR",
            "THB",
            "UAH",
            "UYU",
            "ZAR",
            "ZMW",
            "NGN",
            "RSD",
            "TWD",
            "GTQ",
            "HNL",
            "DOP",
            "SAR",
            "PEN",
        ]
    ]
    """The two-decimal ISO 4217 payout currency of the pay rate."""

    effective_date: Required[Annotated[str, PropertyInfo(alias="effectiveDate")]]

    require_hours_submission: Annotated[Optional[bool], PropertyInfo(alias="requireHoursSubmission")]
    """Whether the worker must submit hours. Required when type is hourly."""

    description: Optional[str]
    """A human-readable label for the pay rate."""

    notes: Optional[str]
    """Optional internal notes about the pay rate change."""
