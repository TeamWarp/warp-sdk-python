# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffListAssignmentsResponse", "Data"]


class Data(BaseModel):
    id: str
    """The external-facing id of the worker assignment."""

    policy_id: str = FieldInfo(alias="policyId")

    worker_id: str = FieldInfo(alias="workerId")
    """The id of the worker."""

    assigned_at: str = FieldInfo(alias="assignedAt")


class TimeOffListAssignmentsResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: List[Data]
