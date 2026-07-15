# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeOffListAssignmentsResponse", "Data"]

class Data(BaseModel):

    id: str

    policy_id: str = FieldInfo(alias="policyId")
    """a string starting with "top_\""""

    worker_id: str = FieldInfo(alias="workerId")
    """The id of the worker."""

    assigned_at: str = FieldInfo(alias="assignedAt")
    """a string to be decoded into a Date"""

class TimeOffListAssignmentsResponse(BaseModel):

    has_more: bool = FieldInfo(alias="hasMore")

    count: int
    """an integer"""

    data: List[Data]



