# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_bank_account_reference import PublicBankAccountReference
from .public_pay_split_allocation import PublicPaySplitAllocation

__all__ = ["PublicPaySplitAmountAllocation"]


class PublicPaySplitAmountAllocation(BaseModel):
    bank_account: PublicBankAccountReference = FieldInfo(alias="bankAccount")

    priority: int

    allocation: PublicPaySplitAllocation
    """A fixed amount, or the net pay remaining after earlier allocations. The final allocation of an amount split always receives the remainder."""
