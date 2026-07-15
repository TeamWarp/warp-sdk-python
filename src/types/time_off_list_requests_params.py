# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, Literal, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["TimeOffListRequestsParams"]


class TimeOffListRequestsParams(TypedDict, total=False):

    limit: str
    """a number less than or equal to 100"""

    after_id: Annotated[str, PropertyInfo(alias="afterId")]

    before_id: Annotated[str, PropertyInfo(alias="beforeId")]

    statuses: Iterable[Literal["pending", "approved", "denied"]]

    policy_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="policyIds")]

    worker_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workerIds")]

    starts_on_or_after: Annotated[str, PropertyInfo(alias="startsOnOrAfter")]
    """a string to be decoded into a Date"""

    starts_before: Annotated[str, PropertyInfo(alias="startsBefore")]
    """a string to be decoded into a Date"""

    ends_on_or_after: Annotated[str, PropertyInfo(alias="endsOnOrAfter")]
    """a string to be decoded into a Date"""

    ends_before: Annotated[str, PropertyInfo(alias="endsBefore")]
    """a string to be decoded into a Date"""
