# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .benefits.public_worker_reference import PublicWorkerReference
from .public_pay_split_status import PublicPaySplitStatus
from .public_pay_split_amount_allocation import PublicPaySplitAmountAllocation

__all__ = ["PublicAmountPaySplit", "Status"]


class Status(BaseModel):
    pass


class PublicAmountPaySplit(BaseModel):
    id: str
    """The tag of the bank account pay split."""

    worker: PublicWorkerReference
    """Basic identifying information for a worker associated with another resource."""

    status: Status

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    type: Literal["amount"]

    allocations: List[PublicPaySplitAmountAllocation]
