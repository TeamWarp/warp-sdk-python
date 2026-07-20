# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkplaceCreateParams", "Address"]


class WorkplaceCreateParams(TypedDict, total=False):

    name: Required[str]
    """a non empty string"""

    type: Required[Literal["remote", "office"]]

    address: Required[Address]
    """A valid US address"""


class Address(TypedDict, total=False):

    line1: Required[str]
    """a non empty string"""

    line2: Optional[str]

    city: Required[str]

    postal_code: Required[Annotated[str, PropertyInfo(alias="postalCode")]]

    state: Required[Literal["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]]

    country: Required[Literal["US"]]

