# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_health_plan import PublicHealthPlan

__all__ = ["HealthPlanListResponse"]


class HealthPlanListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[PublicHealthPlan]
