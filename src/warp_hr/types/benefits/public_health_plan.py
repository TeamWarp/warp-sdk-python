# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_health_plan_carrier import PublicHealthPlanCarrier
from .public_health_plan_status import PublicHealthPlanStatus

__all__ = ["PublicHealthPlan"]


class PublicHealthPlan(BaseModel):
    """A company health plan available through Warp."""

    id: str
    """The tag of a company health plan."""

    carrier: PublicHealthPlanCarrier
    """The insurance carrier underwriting the health plan."""

    type: Literal[
        "medical",
        "dental",
        "vision",
        "life",
        "short_term_disability",
        "long_term_disability",
        "accident",
        "critical_illness",
        "hospital",
    ]
    """The health coverage type."""

    name: str
    """The company-facing plan name."""

    group_number: Optional[str] = FieldInfo(alias="groupNumber", default=None)
    """The carrier-assigned group number."""

    network_type: Optional[Literal["hmo", "ppo", "epo", "pos", "hdhp", "indemnity"]] = FieldInfo(
        alias="networkType", default=None
    )
    """The plan network structure."""

    effective_start_date: str = FieldInfo(alias="effectiveStartDate")

    effective_end_date: Optional[str] = FieldInfo(alias="effectiveEndDate", default=None)

    status: PublicHealthPlanStatus
    """The public lifecycle status of a health plan."""

    created_at: str = FieldInfo(alias="createdAt")

    updated_at: str = FieldInfo(alias="updatedAt")
