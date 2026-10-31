# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthPlanReference"]


class HealthPlanReference(BaseModel):
    """The health plan associated with the deduction."""

    type: Literal["health_plan"]

    id: str
    """The tag of a company health plan."""

    name: str
    """The associated health plan name."""
