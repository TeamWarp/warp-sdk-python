# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicPayrollList"]


class PublicPayrollList(BaseModel):
    """A cursor-paginated page of payroll summaries."""

    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: object
