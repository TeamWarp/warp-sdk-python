# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .public_worker_reference import PublicWorkerReference
from .public_benefit_deduction_category import PublicBenefitDeductionCategory
from .health_plan_reference import HealthPlanReference
from .retirement_plan_reference import RetirementPlanReference
from .public_benefit_deduction_calculation import PublicBenefitDeductionCalculation
from .public_benefit_deduction_status import PublicBenefitDeductionStatus
from .public_benefit_deduction_plan import PublicBenefitDeductionPlan

__all__ = ["PublicBenefitDeduction1"]


class PublicBenefitDeduction1(BaseModel):
    """The current version of a stable payroll benefit deduction."""

    id: str
    """Stable identifier shared by every internal version of this deduction."""

    worker: PublicWorkerReference
    """Basic identifying information for a worker associated with another resource."""

    name: str
    """The deduction name shown in payroll and benefits surfaces."""

    category: PublicBenefitDeductionCategory
    """The broad reporting category. The type field identifies the specific payroll deduction."""

    type: Literal[
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
    """The specific payroll deduction type within the broader category."""

    recurrence: Literal["recurring", "one_time"]
    """Whether the deduction recurs or applies once."""

    plan: Optional[PublicBenefitDeductionPlan] = None
    """The associated benefit plan, or null for a planless payroll deduction."""

    calculation: PublicBenefitDeductionCalculation
    """How the employee and employer contributions are calculated."""

    effective_start_date: str = FieldInfo(alias="effectiveStartDate")

    effective_end_date: Optional[str] = FieldInfo(alias="effectiveEndDate", default=None)

    status: PublicBenefitDeductionStatus
    """The public lifecycle status of the current deduction version."""

    created_at: str = FieldInfo(alias="createdAt")

    updated_at: str = FieldInfo(alias="updatedAt")
