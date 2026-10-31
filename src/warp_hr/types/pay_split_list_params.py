# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .public_pay_split_status import PublicPaySplitStatus

__all__ = ["PaySplitListParams"]


class PaySplitListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of the bank account pay split."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of the bank account pay split."""

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]
    """Worker IDs as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches."""

    types: Optional[List[Literal["percentage", "amount"]]]
    """Configuration types as repeated parameters. Omit for all types."""

    statuses: Required[Optional[List[PublicPaySplitStatus]]]
    """Statuses as repeated parameters. Defaults to active; explicitly request inactive or both to include retained configurations."""
