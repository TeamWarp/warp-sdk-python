# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "OfferCreateParams",
    "Candidate",
    "CandidateContractorDetails",
    "Position",
    "Compensation",
    "BackgroundCheckWorkLocation",
]


class OfferCreateParams(TypedDict, total=False):
    candidate: Required[Candidate]

    position: Required[Position]

    department_id: Annotated[Optional[str], PropertyInfo(alias="departmentId")]
    """The unique public id of the department"""

    workplace_id: Annotated[Optional[str], PropertyInfo(alias="workplaceId")]
    """Public workplace identifier"""

    manager_id: Annotated[Optional[str], PropertyInfo(alias="managerId")]
    """The id of the worker."""

    level_id: Annotated[Optional[str], PropertyInfo(alias="levelId")]
    """The unique public id of the job level"""

    worker_type: Required[
        Annotated[Literal["employee", "us_contractor", "global_contractor"], PropertyInfo(alias="workerType")]
    ]

    compensation: Required[Compensation]

    expiration_time: Annotated[Optional[str], PropertyInfo(alias="expirationTime")]

    background_check_work_location: Annotated[
        Optional[BackgroundCheckWorkLocation], PropertyInfo(alias="backgroundCheckWorkLocation")
    ]


class BackgroundCheckWorkLocation(TypedDict, total=False):
    country: Required[str]

    state: Required[str]

    city: Required[str]


class Compensation(TypedDict, total=False):
    pay_basis: Required[Annotated[Literal["year", "month", "week", "hour", "variable"], PropertyInfo(alias="payBasis")]]

    pay_currency: Required[
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
            PropertyInfo(alias="payCurrency"),
        ]
    ]

    pay_rate: Required[Annotated[float, PropertyInfo(alias="payRate")]]
    """major units (dollars), e.g. 23.45"""

    pay_type: Annotated[Optional[Literal["fixed", "pay_as_you_go"]], PropertyInfo(alias="payType")]

    pay_variable_rate: Annotated[Optional[float], PropertyInfo(alias="payVariableRate")]
    """major units (dollars), e.g. 23.45"""

    sign_on_bonus: Annotated[Optional[float], PropertyInfo(alias="signOnBonus")]
    """major units (dollars), e.g. 23.45"""

    relocation_bonus: Annotated[Optional[float], PropertyInfo(alias="relocationBonus")]
    """major units (dollars), e.g. 23.45"""

    stock_options: Annotated[Optional[int], PropertyInfo(alias="stockOptions")]

    vesting_schedule_months: Annotated[Optional[int], PropertyInfo(alias="vestingScheduleMonths")]

    cliff_months: Annotated[Optional[int], PropertyInfo(alias="cliffMonths")]


class Position(TypedDict, total=False):
    title: Required[str]

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]

    country: Optional[
        Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AX",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BQ",
            "BR",
            "BS",
            "BT",
            "BV",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GF",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GP",
            "GQ",
            "GR",
            "GS",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HM",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IO",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MQ",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NF",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PS",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "SS",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TF",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "UM",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "XK",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ]
    """Required when workerType is global_contractor. Ignored for employee and us_contractor offers."""

    scope_of_work: Annotated[Optional[str], PropertyInfo(alias="scopeOfWork")]


class CandidateContractorDetails(TypedDict, total=False):
    is_business: Required[Annotated[bool, PropertyInfo(alias="isBusiness")]]

    legal_business_name: Required[Annotated[Optional[str], PropertyInfo(alias="legalBusinessName")]]


class Candidate(TypedDict, total=False):
    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]

    email: Required[str]
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    contractor_details: Annotated[Optional[CandidateContractorDetails], PropertyInfo(alias="contractorDetails")]
