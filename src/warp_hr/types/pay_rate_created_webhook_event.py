# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PayRateCreatedWebhookEvent", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The fixed pay-rate id, or null when the event represents a variable-pay boundary with no row."""

    worker_id: str = FieldInfo(alias="workerId")
    """The worker whose regular pay-rate timeline changed."""

    effective_date: str = FieldInfo(alias="effectiveDate")


class PayRateCreatedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier (format: `<objectTag>:<uuid>`). Stable across retries."""

    type: Literal["pay_rate.created"]
    """The event type."""

    timestamp: str
    """ISO 8601 timestamp of when the event occurred. Unchanged across retries."""

    data: Data
