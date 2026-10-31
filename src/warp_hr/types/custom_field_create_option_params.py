# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldCreateOptionParams"]


class CustomFieldCreateOptionParams(TypedDict, total=False):
    label: Required[str]

    value: Required[str]

    sort_order: Annotated[
        Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]], PropertyInfo(alias="sortOrder")
    ]
