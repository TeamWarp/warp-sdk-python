# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DepartmentCreateResponse"]

class DepartmentCreateResponse(BaseModel):

    id: str
    """The unique public id of the department"""

    name: str

    created_at: str = FieldInfo(alias="createdAt")
    """a string to be decoded into a Date"""



