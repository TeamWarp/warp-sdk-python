# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_bank_account_reference import PublicBankAccountReference
from .public_pay_split_percentage import PublicPaySplitPercentage

__all__ = ["PublicPaySplitPercentageAllocation"]


class PublicPaySplitPercentageAllocation(BaseModel):
    bank_account: PublicBankAccountReference = FieldInfo(alias="bankAccount")

    priority: int

    percentage: PublicPaySplitPercentage
    """A stored percentage from 0 to 100 with at most four decimal places and its server-formatted display. Values are preserved, not normalized to total 100 or predicted from provider execution."""
