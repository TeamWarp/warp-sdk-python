# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomFieldGetResponse", "Option"]


class Option(BaseModel):
    id: str
    """The tag of a company custom worker field option."""

    label: str

    value: str

    sort_order: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="sortOrder")

    status: Literal["active", "archived"]

    created_at: str = FieldInfo(alias="createdAt")


class CustomFieldGetResponse(BaseModel):
    id: str
    """The tag of a company custom worker field."""

    name: str

    description: Optional[str] = None

    type: Literal["text", "number", "date", "boolean", "currency", "percentage", "select", "multi_select"]

    config: object

    status: Literal["active", "archived"]

    category: Literal["info", "pii", "compensation", "banking", "it", "compliance"]

    access_level: Literal["admins", "manager", "worker"] = FieldInfo(alias="accessLevel")

    input_by: Literal["admin", "worker"] = FieldInfo(alias="inputBy")

    required: Optional[bool] = None

    can_write: bool = FieldInfo(alias="canWrite")

    created_at: str = FieldInfo(alias="createdAt")

    options: List[Option]
