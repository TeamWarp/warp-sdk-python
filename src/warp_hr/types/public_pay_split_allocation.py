# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .public_pay_split_fixed_allocation import PublicPaySplitFixedAllocation
from .public_pay_split_remainder_allocation import PublicPaySplitRemainderAllocation

__all__ = ["PublicPaySplitAllocation"]

PublicPaySplitAllocation: TypeAlias = Union[PublicPaySplitFixedAllocation, PublicPaySplitRemainderAllocation]
