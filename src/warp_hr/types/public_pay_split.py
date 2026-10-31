# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .public_percentage_pay_split import PublicPercentagePaySplit
from .public_amount_pay_split import PublicAmountPaySplit

__all__ = ["PublicPaySplit"]

PublicPaySplit: TypeAlias = Union[PublicPercentagePaySplit, PublicAmountPaySplit]
