# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldUpdateParams"]


class CustomFieldUpdateParams(TypedDict, total=False):
    name: Optional[str]

    description: Optional[str]

    config: Optional[object]

    category: Optional[Literal["info", "pii", "compensation", "banking", "it", "compliance"]]

    access_level: Annotated[Optional[Literal["admins", "manager", "worker"]], PropertyInfo(alias="accessLevel")]

    input_by: Annotated[Optional[Literal["admin", "worker"]], PropertyInfo(alias="inputBy")]

    required: Optional[bool]
