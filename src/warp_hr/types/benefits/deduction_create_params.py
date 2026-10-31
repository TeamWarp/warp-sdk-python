# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "DeductionCreateParams",
    "Plan",
    "Plan2",
    "Plan3",
    "Calculation",
    "CalculationFixedAmountBenefitInput",
    "CalculationFixedAmountBenefitInputEmployeeContribution",
    "CalculationFixedAmountBenefitInputEmployerContribution",
    "CalculationPercentageBenefitInput",
    "CalculationPercentageBenefitInputEmployeeContribution",
    "CalculationPercentageBenefitInputEmployerContribution",
]


class DeductionCreateParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """The id of the worker."""

    type: Required[
        Literal[
            "medical",
            "dental",
            "vision",
            "life",
            "short_term_disability",
            "long_term_disability",
            "401k",
            "roth_401k",
            "403b",
            "roth_403b",
            "457",
            "roth_457",
            "simple_ira",
            "roth_simple_ira",
            "hsa",
            "fsa_medical",
            "fsa_dependent_care",
            "transit",
            "parking",
            "accident",
            "cancer",
            "critical_illness",
            "hospital",
            "medical_other",
            "nqdc",
            "nontaxable_fringe",
        ]
    ]
    """The payroll deduction type to create."""

    plan: Optional[Plan]
    """A matching company plan, or null for a planless deduction."""

    name: Optional[str]

    calculation: Required[Calculation]
    """Both contributions must be supplied."""

    recurrence: Optional[Literal["recurring", "one_time"]]

    effective_start_date: Required[Annotated[str, PropertyInfo(alias="effectiveStartDate")]]

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


class Plan3(TypedDict, total=False):
    type: Required[Literal["retirement_plan"]]

    id: Required[str]
    """The tag of a company retirement plan."""


class Plan2(TypedDict, total=False):
    type: Required[Literal["health_plan"]]

    id: Required[str]
    """The tag of a company health plan."""


Plan: TypeAlias = Union[Plan2, Plan3]
