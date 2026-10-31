# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffListRequestsResponse", "Data"]


class Data(BaseModel):
    id: str

    time_off_policy_id: str = FieldInfo(alias="timeOffPolicyId")

    worker_id: str = FieldInfo(alias="workerId")
    """The id of the worker."""

    status: Literal["pending", "approved", "denied"]

    start_at: str = FieldInfo(alias="startAt")

    start_range_type: Literal["date", "datetime"] = FieldInfo(alias="startRangeType")

    end_at: str = FieldInfo(alias="endAt")

    end_range_type: Literal["date", "datetime"] = FieldInfo(alias="endRangeType")

    reason: Optional[str] = None

    created_at: str = FieldInfo(alias="createdAt")

    requested_minutes: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="requestedMinutes")

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)
    """The time zone that the worker is requesting time off in."""


class TimeOffListRequestsResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[Data]
