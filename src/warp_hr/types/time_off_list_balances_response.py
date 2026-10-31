# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffListBalancesResponse", "Data"]


class Data(BaseModel):
    id: str
    """The external-facing id of the worker assignment."""

    policy_id: str = FieldInfo(alias="policyId")

    legacy_worker_id: str = FieldInfo(alias="legacyWorkerId")

    accrued_unlocked: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="accruedUnlocked")

    accrued_locked: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="accruedLocked")

    used: Union[float, Literal["Infinity", "-Infinity", "NaN"]]

    holds: Union[float, Literal["Infinity", "-Infinity", "NaN"]]

    available: Union[float, Literal["Infinity", "-Infinity", "NaN"]]


class TimeOffListBalancesResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[Data]
