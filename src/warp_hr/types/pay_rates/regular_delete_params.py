# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RegularDeleteParams"]


class RegularDeleteParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """The worker whose future regular pay rate will be deleted."""

    effective_date: Required[Annotated[str, PropertyInfo(alias="effectiveDate")]]
