# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["I9VerificationListParams"]


class I9VerificationListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of the i9 verification."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of the i9 verification."""

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]
    """Worker IDs to include, supplied as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches."""

    statuses: Optional[List[Literal["not_started", "awaiting_worker", "awaiting_admin", "verified"]]]
    """Statuses to include, supplied as repeated parameters. Omit for all workflow states."""
