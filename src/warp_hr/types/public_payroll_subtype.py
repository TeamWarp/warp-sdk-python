# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PublicPayrollSubtype"]

PublicPayrollSubtype: TypeAlias = Literal[
    "regular", "off_cycle", "bonus", "invoice", "contractor", "dismissal", "reimbursement", "manual"
]
