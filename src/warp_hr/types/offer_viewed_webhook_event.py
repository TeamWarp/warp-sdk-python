# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_money_amount import PublicMoneyAmount

__all__ = [
    "OfferViewedWebhookEvent",
    "Data",
    "DataCandidate",
    "DataCandidateContractorDetails",
    "DataPosition",
    "DataDepartment",
    "DataWorkplace",
    "DataManager",
    "DataLevel",
    "DataCompensation",
    "DataCompensationBasePay",
    "DataCompensationStock",
]


class DataCompensationStock(BaseModel):
    options: int

    vesting_schedule_months: Optional[int] = FieldInfo(alias="vestingScheduleMonths", default=None)

    cliff_months: Optional[int] = FieldInfo(alias="cliffMonths", default=None)


class DataCompensationBasePay(BaseModel):
    amount: PublicMoneyAmount
    """A monetary amount with its currency and server-formatted display value."""

    basis: Literal["year", "month", "week", "hour", "variable"]

    type: Optional[Literal["fixed", "pay_as_you_go"]] = None

    variable_rate: Optional[PublicMoneyAmount] = FieldInfo(alias="variableRate", default=None)
    """A monetary amount with its currency and server-formatted display value."""


class DataCompensation(BaseModel):
    base_pay: DataCompensationBasePay = FieldInfo(alias="basePay")

    sign_on_bonus: Optional[PublicMoneyAmount] = FieldInfo(alias="signOnBonus", default=None)
    """A monetary amount with its currency and server-formatted display value."""

    relocation_bonus: Optional[PublicMoneyAmount] = FieldInfo(alias="relocationBonus", default=None)
    """A monetary amount with its currency and server-formatted display value."""

    stock: Optional[DataCompensationStock] = None


class DataLevel(BaseModel):
    id: str
    """The unique public id of the job level"""

    code: str

    name: str

    track: Literal["ic", "manager", "executive"]


class DataManager(BaseModel):
    id: str
    """The id of the worker."""

    name: Optional[str] = None


class DataWorkplace(BaseModel):
    id: str
    """Public workplace identifier"""

    name: str


class DataDepartment(BaseModel):
    id: str
    """The unique public id of the department"""

    name: str


class DataPosition(BaseModel):
    title: str

    start_date: str = FieldInfo(alias="startDate")

    country: Literal[
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

    scope_of_work: Optional[str] = FieldInfo(alias="scopeOfWork", default=None)


class DataCandidateContractorDetails(BaseModel):
    is_business: bool = FieldInfo(alias="isBusiness")

    legal_business_name: Optional[str] = FieldInfo(alias="legalBusinessName", default=None)


class DataCandidate(BaseModel):
    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")

    email: str
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    contractor_details: Optional[DataCandidateContractorDetails] = FieldInfo(alias="contractorDetails", default=None)


class Data(BaseModel):
    id: str
    """The tag of the offer."""

    status: Literal["draft", "sent", "accepted", "void", "expired"]

    void_reason: Optional[Literal["replaced", "candidate_declined", "other"]] = FieldInfo(
        alias="voidReason", default=None
    )
    """The reason the offer was voided. Null for offers that have not been voided."""

    void_notes: Optional[str] = FieldInfo(alias="voidNotes", default=None)
    """Additional notes explaining why the offer was voided."""

    worker_type: Literal["employee", "us_contractor", "global_contractor"] = FieldInfo(alias="workerType")

    candidate: DataCandidate

    position: DataPosition

    department: Optional[DataDepartment] = None

    workplace: Optional[DataWorkplace] = None

    manager: Optional[DataManager] = None

    level: Optional[DataLevel] = None
    """The offer's job level, or null if unassigned. Omitted when job levels are not enabled."""

    sent_by: Optional[str] = FieldInfo(alias="sentBy", default=None)
    """Display name of the person or company that sent the offer. Null for offers not yet sent."""

    compensation: DataCompensation

    offer_url: Optional[str] = FieldInfo(alias="offerUrl", default=None)
    """The candidate-facing offer portal URL. Null for offers that have not been sent."""

    expiration_time: Optional[str] = FieldInfo(alias="expirationTime", default=None)

    last_viewed_at: Optional[str] = FieldInfo(alias="lastViewedAt", default=None)

    created_at: str = FieldInfo(alias="createdAt")


class OfferViewedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier (format: `<objectTag>:<uuid>`). Stable across retries."""

    type: Literal["offer.viewed"]
    """The event type."""

    timestamp: str
    """ISO 8601 timestamp of when the event occurred. Unchanged across retries."""

    data: Data
