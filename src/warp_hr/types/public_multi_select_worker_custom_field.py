# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicMultiSelectWorkerCustomField", "Option"]


class Option(BaseModel):
    id: str
    """The tag of a company custom worker field option."""

    label: str

    value: str

    sort_order: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="sortOrder")

    status: Literal["active", "archived"]

    created_at: str = FieldInfo(alias="createdAt")


class PublicMultiSelectWorkerCustomField(BaseModel):
    type: Literal["multi_select"]

    id: str
    """The tag of a company custom worker field."""

    name: str

    redacted: bool
    """True when this API key’s permission scopes cannot read the field’s category. The value fields are withheld (null), not absent — null does not imply the worker has no value."""

    display: Optional[str] = None
    """The value rendered as the Warp dashboard displays it; null when unset or redacted."""

    options: Optional[List[Option]] = None
    """The selected options; null when unset or when the field is redacted for this API key."""
