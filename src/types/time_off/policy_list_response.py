# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PolicyListResponse", "Data"]

class Data(BaseModel):

    id: str
    """a string starting with "top_\""""

    time_off_type_id: str = FieldInfo(alias="timeOffTypeId")
    """a string starting with "tot_\""""

    time_off_type_name: str = FieldInfo(alias="timeOffTypeName")

    paid: bool

    is_unlimited: bool = FieldInfo(alias="isUnlimited")

    schedule: Literal["per_hour_worked", "monthly", "yearly", "unlimited"]

    unit: Literal["hour", "day"]

    name: str

    description: Optional[str] = None

    hours_worked_per_chunk: Optional[float] = FieldInfo(alias="hoursWorkedPerChunk", default=None)

    minutes_per_chunk: Optional[float] = FieldInfo(alias="minutesPerChunk", default=None)

    minutes_per_period: Optional[float] = FieldInfo(alias="minutesPerPeriod", default=None)

class PolicyListResponse(BaseModel):

    has_more: bool = FieldInfo(alias="hasMore")

    count: int
    """an integer"""

    data: List[Data]



