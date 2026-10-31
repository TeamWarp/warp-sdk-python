# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldUpdateOptionParams"]


class CustomFieldUpdateOptionParams(TypedDict, total=False):
    label: Optional[str]

    sort_order: Annotated[
        Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]], PropertyInfo(alias="sortOrder")
    ]
