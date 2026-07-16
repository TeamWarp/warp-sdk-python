# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerCreateContractorParams", "Compensation"]


class WorkerCreateContractorParams(TypedDict, total=False):

    entity_type: Required[Annotated[Literal["individual", "business"], PropertyInfo(alias="entityType")]]
    """Whether the contractor is an individual person or a business entity."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """a non empty string"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """a non empty string"""

    position: Required[str]
    """The contractor's role or job title."""

    business_name: Annotated[str, PropertyInfo(alias="businessName")]
    """Required when entityType is "business". The legal name of the contractor's business."""

    scope_of_work: Annotated[Optional[str], PropertyInfo(alias="scopeOfWork")]
    """A description of the work the contractor will perform."""

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]
    """A date string in the form YYYY-MM-DD"""

    email: Required[str]
    """Personal email address. The invite will be sent here."""

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]
    """Company-issued email address, if applicable."""

    department_id: Required[Annotated[str, PropertyInfo(alias="departmentId")]]
    """The department to assign this contractor to."""

    manager_id: Required[Annotated[str, PropertyInfo(alias="managerId")]]
    """The worker id of this contractor's direct manager."""

    work_country: Required[Annotated[Literal["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "ZA", "ZM", "ZW"], PropertyInfo(alias="workCountry")]]

    compensation: Optional[Compensation]
    """The contractor's pay rate. Omit if you'd like to pay on-demand or via invoicing."""

    pay_schedule: Annotated[Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]], PropertyInfo(alias="paySchedule")]
    """The contractor's pay schedule. Must be a pay schedule that the company has configured."""


class Compensation(TypedDict, total=False):

    currency: Required[Literal["USD", "AUD", "BGN", "BRL", "CAD", "CHF", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "INR", "JPY", "MYR", "NOK", "NZD", "CNY", "PLN", "RON", "TRY", "SEK", "SGD", "AED", "ARS", "BDT", "BWP", "CLP", "COP", "CRC", "EGP", "FJD", "GEL", "GHS", "ILS", "KES", "KRW", "LKR", "MAD", "MXN", "NPR", "PHP", "PKR", "THB", "UAH", "UGX", "UYU", "VND", "ZAR", "ZMW", "TND", "NGN", "RSD", "TWD", "GTQ", "HNL", "DOP", "SAR", "XAF", "PEN"]]

    amount: Required[float]
    """a positive number"""

    per: Required[Literal["hour", "year", "month", "week"]]
    """The pay period for the compensation amount."""

