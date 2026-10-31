# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional, Union
from typing_extensions import TypeAlias

from .health_plan_reference import HealthPlanReference
from .retirement_plan_reference import RetirementPlanReference

__all__ = ["PublicBenefitDeductionPlan"]

PublicBenefitDeductionPlan: TypeAlias = Optional[Union[HealthPlanReference, RetirementPlanReference]]
