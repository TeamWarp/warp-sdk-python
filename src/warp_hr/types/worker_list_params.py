# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerListParams"]


class WorkerListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The id of the worker."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The id of the worker."""

    statuses: Optional[List[Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]]]

    types: Optional[List[Literal["employee", "contractor"]]]

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]
