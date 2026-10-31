# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["TimeOffListRequestsParams"]


class TimeOffListRequestsParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]

    statuses: Optional[List[Literal["pending", "approved", "denied"]]]

    policy_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="policyIds")]

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]

    starts_on_or_after: Annotated[Optional[str], PropertyInfo(alias="startsOnOrAfter")]

    starts_before: Annotated[Optional[str], PropertyInfo(alias="startsBefore")]

    ends_on_or_after: Annotated[Optional[str], PropertyInfo(alias="endsOnOrAfter")]

    ends_before: Annotated[Optional[str], PropertyInfo(alias="endsBefore")]
