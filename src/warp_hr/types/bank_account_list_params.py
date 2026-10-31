# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["BankAccountListParams"]


class BankAccountListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of the bank account."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of the bank account."""

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]
    """Worker IDs to include as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches."""

    statuses: Optional[List[Literal["verified", "pending_verification", "needs_address", "unverified", "blocked"]]]
    """Verification states to include as repeated parameters. Omit for all states."""
