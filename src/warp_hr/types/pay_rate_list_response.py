# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_pay_rate import PublicPayRate

__all__ = ["PayRateListResponse"]


class PayRateListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[PublicPayRate]
