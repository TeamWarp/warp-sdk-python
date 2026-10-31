# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicPayrollTimeline"]


class PublicPayrollTimeline(BaseModel):
    """The approval timestamp for a payroll."""

    approved_at: Optional[str] = FieldInfo(alias="approvedAt", default=None)
