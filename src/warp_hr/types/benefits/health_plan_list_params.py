# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from .public_health_plan_status import PublicHealthPlanStatus

__all__ = ["HealthPlanListParams"]


class HealthPlanListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of a company health plan."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of a company health plan."""

    types: Optional[
        List[
            Literal[
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
        ]
    ]

    statuses: Required[Optional[List[PublicHealthPlanStatus]]]

    carrier_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="carrierIds")]
