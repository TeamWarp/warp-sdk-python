# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_money_amount_4 import PublicPayrollMoneyAmount4
from .public_payroll_money_amount_5 import PublicPayrollMoneyAmount5

__all__ = ["PublicPaycheckBenefit"]


class PublicPaycheckBenefit(BaseModel):
    """One benefit contribution calculation line. Lines have no durable public identity."""

    name: str

    benefit_deduction_id: Optional[str] = FieldInfo(alias="benefitDeductionId", default=None)
    """The version-group tag of a payroll benefit deduction. Stable across edits."""

    category: Optional[
        Literal["health", "retirement", "health_savings", "commuter", "voluntary", "post_tax", "other"]
    ] = None

    type: Optional[
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
    ] = None

    worker_contribution: PublicPayrollMoneyAmount4 = FieldInfo(alias="workerContribution")
    """The amount the worker pays toward this benefit on the paycheck in the amount's currency."""

    employer_contribution: PublicPayrollMoneyAmount5 = FieldInfo(alias="employerContribution")
    """The amount the employer pays toward this benefit on the paycheck in the amount's currency."""
