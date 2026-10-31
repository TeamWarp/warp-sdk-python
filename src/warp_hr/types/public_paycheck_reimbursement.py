# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .public_payroll_money_amount_2 import PublicPayrollMoneyAmount2

__all__ = ["PublicPaycheckReimbursement"]


class PublicPaycheckReimbursement(BaseModel):
    """One reimbursement calculation line. Lines have no durable public identity."""

    amount: PublicPayrollMoneyAmount2
    """The amount reimbursed to the worker on this paycheck in the amount's currency. It may differ from the currency of the original expense."""

    description: Optional[str] = None
