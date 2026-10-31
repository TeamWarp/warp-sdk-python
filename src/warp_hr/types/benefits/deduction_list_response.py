# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_benefit_deduction import PublicBenefitDeduction

__all__ = ["DeductionListResponse"]


class DeductionListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[PublicBenefitDeduction]
