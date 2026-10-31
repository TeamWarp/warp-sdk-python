# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
