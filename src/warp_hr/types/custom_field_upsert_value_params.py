# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = [
    "CustomFieldUpsertValueParams",
    "Value",
    "Value2",
    "Value3",
    "Value4",
    "Value5",
    "Value6",
    "Value7",
    "Value8",
    "Value9",
]


class CustomFieldUpsertValueParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """The id of the worker."""

    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """The tag of a company custom worker field."""

    value: Required[Value]


class Value9(TypedDict, total=False):
    type: Required[Literal["multi_select"]]

    option_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="optionIds")]]


class Value8(TypedDict, total=False):
    type: Required[Literal["select"]]

    option_id: Required[Annotated[str, PropertyInfo(alias="optionId")]]
    """The tag of a company custom worker field option."""


class Value7(TypedDict, total=False):
    type: Required[Literal["percentage"]]

    value: Required[Union[float, Literal["Infinity", "-Infinity", "NaN"]]]


class Value6(TypedDict, total=False):
    type: Required[Literal["currency"]]

    amount: Required[int]
    """Integer base units of currencyCode (e.g. cents)."""

    currency_code: Required[
        Annotated[
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
            ],
            PropertyInfo(alias="currencyCode"),
        ]
    ]


class Value5(TypedDict, total=False):
    type: Required[Literal["boolean"]]

    value: Required[bool]


class Value4(TypedDict, total=False):
    type: Required[Literal["date"]]

    value: Required[str]


class Value3(TypedDict, total=False):
    type: Required[Literal["number"]]

    value: Required[Union[float, Literal["Infinity", "-Infinity", "NaN"]]]


class Value2(TypedDict, total=False):
    type: Required[Literal["text"]]

    value: Required[str]


Value: TypeAlias = Union[Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9]
