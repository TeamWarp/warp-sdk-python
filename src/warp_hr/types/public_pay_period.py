# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicPayPeriod"]


class PublicPayPeriod(BaseModel):
    """The inclusive calendar boundaries of a payroll reporting period."""

    start_date: str = FieldInfo(alias="startDate")

    end_date: str = FieldInfo(alias="endDate")
