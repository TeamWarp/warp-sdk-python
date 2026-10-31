# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .benefits.public_worker_reference import PublicWorkerReference

__all__ = ["PublicBankAccount"]


class PublicBankAccount(BaseModel):
    """Stored worker bank account metadata without full account numbers, routing details or provider identifiers."""

    id: str
    """The tag of the bank account."""

    institution_name: Optional[str] = FieldInfo(alias="institutionName", default=None)

    account_type: Optional[Literal["checking", "savings"]] = FieldInfo(alias="accountType", default=None)

    account_number_last_four: str = FieldInfo(alias="accountNumberLastFour")

    worker: PublicWorkerReference
    """Basic identifying information for a worker associated with another resource."""

    status: Literal["verified", "pending_verification", "needs_address", "unverified", "blocked"]

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")
