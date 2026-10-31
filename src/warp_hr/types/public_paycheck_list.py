# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicPaycheckList"]


class PublicPaycheckList(BaseModel):
    """A cursor-paginated page of paycheck summaries."""

    has_more: bool = FieldInfo(alias="hasMore")

    count: int

    data: object
