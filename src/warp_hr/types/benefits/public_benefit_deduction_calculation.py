# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .fixed_amount_benefit_calculation import FixedAmountBenefitCalculation
from .percentage_benefit_calculation import PercentageBenefitCalculation

__all__ = ["PublicBenefitDeductionCalculation"]

PublicBenefitDeductionCalculation: TypeAlias = Union[FixedAmountBenefitCalculation, PercentageBenefitCalculation]
