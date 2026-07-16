# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerListParams"]


class WorkerListParams(TypedDict, total=False):

    limit: str
    """a number less than or equal to 100"""

    after_id: Annotated[str, PropertyInfo(alias="afterId")]
    """The id of the worker."""

    before_id: Annotated[str, PropertyInfo(alias="beforeId")]
    """The id of the worker."""

    statuses: Iterable[Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]]

    types: Iterable[Literal["employee", "contractor"]]

    work_email: Annotated[str, PropertyInfo(alias="workEmail")]
