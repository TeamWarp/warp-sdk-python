# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RetirementPlanReference"]


class RetirementPlanReference(BaseModel):
    """The retirement plan associated with the deduction."""

    type: Literal["retirement_plan"]

    id: str
    """The tag of a company retirement plan."""

    name: str
    """The associated retirement plan name."""
