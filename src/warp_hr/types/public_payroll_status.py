# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PublicPayrollStatus"]

PublicPayrollStatus: TypeAlias = Literal[
    "preparing", "draft", "approving", "pending", "processing", "partially_paid", "processed", "failed", "voided"
]
