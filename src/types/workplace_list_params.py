# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkplaceListParams"]


class WorkplaceListParams(TypedDict, total=False):

    limit: str
    """a number less than or equal to 100"""

    after_id: Annotated[str, PropertyInfo(alias="afterId")]
    """Public workplace identifier"""

    before_id: Annotated[str, PropertyInfo(alias="beforeId")]
    """Public workplace identifier"""
