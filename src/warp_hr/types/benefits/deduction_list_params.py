# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

from .public_benefit_deduction_category import PublicBenefitDeductionCategory
from .public_benefit_deduction_status import PublicBenefitDeductionStatus

__all__ = ["DeductionListParams"]


class DeductionListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The version-group tag of a payroll benefit deduction. Stable across edits."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The version-group tag of a payroll benefit deduction. Stable across edits."""

    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]

    categories: Optional[List[PublicBenefitDeductionCategory]]

    types: Optional[
        List[
            Literal[
                "medical",
                "dental",
                "vision",
                "life",
                "short_term_disability",
                "long_term_disability",
                "401k",
                "roth_401k",
                "403b",
                "roth_403b",
                "457",
                "roth_457",
                "hsa",
                "fsa_medical",
                "fsa_dependent_care",
                "transit",
                "parking",
                "accident",
                "cancer",
                "critical_illness",
                "hospital",
                "medical_other",
                "simple_ira",
                "roth_simple_ira",
                "nqdc",
                "nontaxable_fringe",
                "pucc",
                "voluntary",
                "post_tax",
                "other",
            ]
        ]
    ]

    statuses: Required[Optional[List[PublicBenefitDeductionStatus]]]

    health_plan_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="healthPlanIds")]

    retirement_plan_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="retirementPlanIds")]
