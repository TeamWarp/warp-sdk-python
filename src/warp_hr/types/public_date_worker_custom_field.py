# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicDateWorkerCustomField"]


class PublicDateWorkerCustomField(BaseModel):
    type: Literal["date"]

    id: str
    """The tag of a company custom worker field."""

    name: str

    redacted: bool
    """True when this API key’s permission scopes cannot read the field’s category. The value fields are withheld (null), not absent — null does not imply the worker has no value."""

    display: Optional[str] = None
    """The value rendered as the Warp dashboard displays it; null when unset or redacted."""

    value: Optional[str] = None
    """The worker’s date; null when unset or when the field is redacted for this API key."""
