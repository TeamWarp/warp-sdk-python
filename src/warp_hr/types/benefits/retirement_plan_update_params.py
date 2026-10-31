# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RetirementPlanUpdateParams"]


class RetirementPlanUpdateParams(TypedDict, total=False):
    name: Optional[str]

    effective_start_date: Annotated[Optional[str], PropertyInfo(alias="effectiveStartDate")]

    effective_end_date: Annotated[Optional[str], PropertyInfo(alias="effectiveEndDate")]
