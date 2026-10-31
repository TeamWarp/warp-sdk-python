# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TimeOffBalanceAdjustedWebhookEvent"]


class TimeOffBalanceAdjustedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier (format: `<objectTag>:<uuid>`). Stable across retries."""

    type: Literal["time_off.balance.adjusted"]
    """The event type."""

    timestamp: str
    """ISO 8601 timestamp of when the event occurred. Unchanged across retries."""

    data: Dict[str, object]
