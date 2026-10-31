# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_i9_verification import PublicI9Verification

__all__ = ["I9VerificationListResponse"]


class I9VerificationListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[PublicI9Verification]
