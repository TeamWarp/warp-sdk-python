# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldCreateParams", "Option"]


class CustomFieldCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    type: Required[Literal["text", "number", "date", "boolean", "currency", "percentage", "select", "multi_select"]]

    config: Optional[object]

    category: Required[Literal["info", "pii", "compensation", "banking", "it", "compliance"]]

    access_level: Annotated[Optional[Literal["admins", "manager", "worker"]], PropertyInfo(alias="accessLevel")]

    input_by: Annotated[Optional[Literal["admin", "worker"]], PropertyInfo(alias="inputBy")]

    required: Optional[bool]

    options: Optional[Iterable[Option]]


class Option(TypedDict, total=False):
    label: Required[str]

    value: Required[str]

    sort_order: Annotated[
        Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]], PropertyInfo(alias="sortOrder")
    ]
