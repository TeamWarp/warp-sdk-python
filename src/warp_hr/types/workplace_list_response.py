# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkplaceListResponse", "Data", "DataAddress"]


class DataAddress(BaseModel):
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


class Data(BaseModel):
    id: str
    """Public workplace identifier"""

    name: str

    type: Literal["remote", "office"]

    status: Literal["active", "archived"]

    address: DataAddress
    """A valid US address"""

    created_at: str = FieldInfo(alias="createdAt")


class WorkplaceListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[Data]
