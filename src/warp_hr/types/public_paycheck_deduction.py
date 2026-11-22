# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_paycheck_deduction_tax_treatment import PublicPaycheckDeductionTaxTreatment
from .public_payroll_money_amount_2 import PublicPayrollMoneyAmount2

__all__ = ["PublicPaycheckDeduction", "TaxTreatment"]


class TaxTreatment(BaseModel):
    pass


class PublicPaycheckDeduction(BaseModel):
    """One non-benefit deduction calculation line. Lines have no durable public identity."""

    tax_treatment: TaxTreatment = FieldInfo(alias="taxTreatment")

    amount: PublicPayrollMoneyAmount2
    """The amount deducted from the worker's pay on this line in the amount's currency."""

    description: Optional[str] = None
