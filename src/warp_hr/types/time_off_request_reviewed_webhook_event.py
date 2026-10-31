# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffRequestReviewedWebhookEvent", "Data"]


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


class TimeOffRequestReviewedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier (format: `<objectTag>:<uuid>`). Stable across retries."""

    type: Literal["time_off.request.reviewed"]
    """The event type."""

    timestamp: str
    """ISO 8601 timestamp of when the event occurred. Unchanged across retries."""

    data: Data
