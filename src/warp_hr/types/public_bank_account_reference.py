# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicBankAccountReference"]


class PublicBankAccountReference(BaseModel):
    id: str
    """The tag of the bank account."""

    institution_name: Optional[str] = FieldInfo(alias="institutionName", default=None)

    account_type: Optional[Literal["checking", "savings"]] = FieldInfo(alias="accountType", default=None)

    account_number_last_four: str = FieldInfo(alias="accountNumberLastFour")
