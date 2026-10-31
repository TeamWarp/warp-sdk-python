# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .percentage_contribution import PercentageContribution

__all__ = ["PercentageBenefitCalculation"]


class PercentageBenefitCalculation(BaseModel):
    """Employee and employer contributions expressed as percentages of eligible earnings."""

    type: Literal["percentage"]

    employee_contribution: PercentageContribution = FieldInfo(alias="employeeContribution")
    """A contribution expressed as a percentage of eligible earnings."""

    employer_contribution: PercentageContribution = FieldInfo(alias="employerContribution")
    """A contribution expressed as a percentage of eligible earnings."""
