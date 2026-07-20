# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkplaceCreateResponse", "Address"]

class Address(BaseModel):

    line1: str
    """a non empty string"""

    line2: Optional[str] = None

    city: str

    postal_code: str = FieldInfo(alias="postalCode")

    state: Literal["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    country: Literal["US"]

class WorkplaceCreateResponse(BaseModel):

    id: str
    """Public workplace identifier"""

    name: str

    type: Literal["remote", "office"]

    status: Literal["active", "archived"]

    address: Address
    """A valid US address"""

    created_at: str = FieldInfo(alias="createdAt")
    """a string to be decoded into a Date"""



