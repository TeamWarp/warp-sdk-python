# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomFieldListResponse", "CustomFieldListResponseItem"]


class CustomFieldListResponseItem(BaseModel):
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


CustomFieldListResponse: TypeAlias = List[CustomFieldListResponseItem]
