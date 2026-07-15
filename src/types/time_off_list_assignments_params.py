# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["TimeOffListAssignmentsParams"]


class TimeOffListAssignmentsParams(TypedDict, total=False):

    limit: str
    """a number less than or equal to 100"""

    after_id: Annotated[str, PropertyInfo(alias="afterId")]

    before_id: Annotated[str, PropertyInfo(alias="beforeId")]

    policy_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="policyIds")]

    worker_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workerIds")]
