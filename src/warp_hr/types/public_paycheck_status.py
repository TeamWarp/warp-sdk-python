# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PublicPaycheckStatus"]

PublicPaycheckStatus: TypeAlias = Literal[
    "draft", "pending", "processing", "debited", "credited", "partially_paid", "processed", "failed", "voided"
]
