# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_retirement_plan import PublicRetirementPlan

__all__ = ["RetirementPlanListResponse"]


class RetirementPlanListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[PublicRetirementPlan]
