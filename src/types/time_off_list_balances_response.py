# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffListBalancesResponse", "Data"]

class Data(BaseModel):

    id: str

    policy_id: str = FieldInfo(alias="policyId")
    """a string starting with "top_\""""

    legacy_worker_id: str = FieldInfo(alias="legacyWorkerId")

    accrued_unlocked: float = FieldInfo(alias="accruedUnlocked")

    accrued_locked: float = FieldInfo(alias="accruedLocked")

    used: float

    holds: float

    available: float

class TimeOffListBalancesResponse(BaseModel):

    has_more: bool = FieldInfo(alias="hasMore")

    count: int
    """an integer"""

    data: List[Data]



