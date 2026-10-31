# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["TimeOffListBalancesParams"]


class TimeOffListBalancesParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The external-facing id of the worker assignment."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The external-facing id of the worker assignment."""

    policy_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="policyIds")]

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]

    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
