# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from ..public_money_amount import PublicMoneyAmount

__all__ = ["FixedAmountBenefitCalculation"]


class FixedAmountBenefitCalculation(BaseModel):
    """Employee and employer contributions expressed as fixed monetary amounts."""

    type: Literal["fixed_amount"]

    frequency: Optional[Literal["per_paycheck", "monthly"]] = None
    """The fixed-amount expression frequency. Null for a one-time deduction."""

    employee_contribution: PublicMoneyAmount = FieldInfo(alias="employeeContribution")
    """A monetary amount with its currency and server-formatted display value."""

    employer_contribution: PublicMoneyAmount = FieldInfo(alias="employerContribution")
    """A monetary amount with its currency and server-formatted display value."""
