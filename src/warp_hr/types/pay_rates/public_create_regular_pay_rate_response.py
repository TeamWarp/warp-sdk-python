# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PublicCreateRegularPayRateResponse"]


class PublicCreateRegularPayRateResponse(BaseModel):
    id: Optional[str] = None
    """The created pay rate id, or null when variable pay is represented by no active regular rate."""
