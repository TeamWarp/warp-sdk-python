# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "DeductionUpdateParams",
    "Calculation",
    "CalculationFixedAmountBenefitInput",
    "CalculationFixedAmountBenefitInputEmployeeContribution",
    "CalculationFixedAmountBenefitInputEmployerContribution",
    "CalculationPercentageBenefitInput",
    "CalculationPercentageBenefitInputEmployeeContribution",
    "CalculationPercentageBenefitInputEmployerContribution",
]


class DeductionUpdateParams(TypedDict, total=False):
    name: Optional[str]

    calculation: Optional[Calculation]
    """Both contributions must be supplied."""

    recurrence: Optional[Literal["recurring", "one_time"]]

    status: Optional[Literal["active", "terminated"]]

    effective_end_date: Annotated[Optional[str], PropertyInfo(alias="effectiveEndDate")]


class CalculationPercentageBenefitInputEmployerContribution(TypedDict, total=False):
    percentage: Required[Union[float, Literal["Infinity", "-Infinity", "NaN"]]]


class CalculationPercentageBenefitInputEmployeeContribution(TypedDict, total=False):
    percentage: Required[Union[float, Literal["Infinity", "-Infinity", "NaN"]]]


class CalculationPercentageBenefitInput(TypedDict, total=False):
    """Employee and employer contributions as percentages of eligible earnings."""

    type: Required[Literal["percentage"]]

    employee_contribution: Required[
        Annotated[CalculationPercentageBenefitInputEmployeeContribution, PropertyInfo(alias="employeeContribution")]
    ]

    employer_contribution: Required[
        Annotated[CalculationPercentageBenefitInputEmployerContribution, PropertyInfo(alias="employerContribution")]
    ]


class CalculationFixedAmountBenefitInputEmployerContribution(TypedDict, total=False):
    """A non-negative amount in cents. Currently only USD is accepted."""

    amount: Required[int]
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
    ]


class CalculationFixedAmountBenefitInputEmployeeContribution(TypedDict, total=False):
    """A non-negative amount in cents. Currently only USD is accepted."""

    amount: Required[int]
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
    ]


class CalculationFixedAmountBenefitInput(TypedDict, total=False):
    """Fixed contributions. Frequency must be null for one-time deductions."""

    type: Required[Literal["fixed_amount"]]

    frequency: Required[Optional[Literal["monthly", "per_paycheck"]]]

    employee_contribution: Required[
        Annotated[CalculationFixedAmountBenefitInputEmployeeContribution, PropertyInfo(alias="employeeContribution")]
    ]
    """A non-negative amount in cents. Currently only USD is accepted."""

    employer_contribution: Required[
        Annotated[CalculationFixedAmountBenefitInputEmployerContribution, PropertyInfo(alias="employerContribution")]
    ]
    """A non-negative amount in cents. Currently only USD is accepted."""


Calculation: TypeAlias = Union[CalculationFixedAmountBenefitInput, CalculationPercentageBenefitInput]
