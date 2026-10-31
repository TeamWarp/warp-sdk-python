# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_company_address import PublicCompanyAddress
from .public_company_business_type import PublicCompanyBusinessType

__all__ = ["PublicCompany", "BusinessAddress", "MailingAddress"]


class MailingAddress(BaseModel):
    line1: str

    line2: Optional[str] = None

    city: str

    postal_code: str = FieldInfo(alias="postalCode")

    state: Literal[
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]

    country: Literal["US"]


class BusinessAddress(BaseModel):
    line1: str

    line2: Optional[str] = None

    city: str

    postal_code: str = FieldInfo(alias="postalCode")

    state: Literal[
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]

    country: Literal["US"]


class PublicCompany(BaseModel):
    """Basic identity, contact, address, and incorporation information for your company."""

    id: str
    """The tag of the company."""

    ein: str
    """An Employer Identification Number (EIN) is assigned to a US corporation by the IRS to identify them for tax purposes"""

    display_name: str = FieldInfo(alias="displayName")
    """The company’s display name."""

    legal_name: str = FieldInfo(alias="legalName")
    """The company’s legal business name."""

    website: str

    phone: str

    contact_email: str = FieldInfo(alias="contactEmail")
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    description: str
    """The company’s business description."""

    business_address: BusinessAddress = FieldInfo(alias="businessAddress")

    mailing_address: MailingAddress = FieldInfo(alias="mailingAddress")

    business_type: PublicCompanyBusinessType = FieldInfo(alias="businessType")
    """The company’s US business type."""

    incorporation_state: Literal[
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ] = FieldInfo(alias="incorporationState")

    incorporation_date: Optional[str] = FieldInfo(alias="incorporationDate", default=None)
