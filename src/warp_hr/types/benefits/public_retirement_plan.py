# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_retirement_plan_provider import PublicRetirementPlanProvider
from .public_retirement_plan_status import PublicRetirementPlanStatus

__all__ = ["PublicRetirementPlan"]


class PublicRetirementPlan(BaseModel):
    """A company retirement plan available through Warp."""

    id: str
    """The tag of a company retirement plan."""

    type: Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"]
    """The retirement plan type."""

    name: str
    """The company-facing plan name."""

    provider: PublicRetirementPlanProvider
    """The system administering the plan. Manual plans are administered by the company outside a connected provider."""

    effective_start_date: str = FieldInfo(alias="effectiveStartDate")

    effective_end_date: Optional[str] = FieldInfo(alias="effectiveEndDate", default=None)

    status: PublicRetirementPlanStatus
    """The public lifecycle status of a retirement plan."""

    created_at: str = FieldInfo(alias="createdAt")

    updated_at: str = FieldInfo(alias="updatedAt")
