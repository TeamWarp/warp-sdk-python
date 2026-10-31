# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["PublicHealthPlanCarrier"]


class PublicHealthPlanCarrier(BaseModel):
    """The insurance carrier underwriting the health plan."""

    id: str
    """The tag of a carrier."""

    name: str
    """The carrier name."""
