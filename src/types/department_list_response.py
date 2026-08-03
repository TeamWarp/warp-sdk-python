# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DepartmentListResponse", "Data"]

class Data(BaseModel):

    id: str
    """The unique public id of the department"""

    name: str

    created_at: str = FieldInfo(alias="createdAt")
    """a string to be decoded into a Date"""

class DepartmentListResponse(BaseModel):

    has_more: bool = FieldInfo(alias="hasMore")

    count: int
    """an integer"""

    data: List[Data]



