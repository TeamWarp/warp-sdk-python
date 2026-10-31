# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

from .public_retirement_plan_status import PublicRetirementPlanStatus

__all__ = ["RetirementPlanListParams"]


class RetirementPlanListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of a company retirement plan."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of a company retirement plan."""

    types: Optional[
        List[Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"]]
    ]

    statuses: Required[Optional[List[PublicRetirementPlanStatus]]]
