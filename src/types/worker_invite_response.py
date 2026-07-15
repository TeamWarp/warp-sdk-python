# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkerInviteResponse", "Department"]

class Department(BaseModel):

    id: str
    """The unique public id of the department"""

    name: str

class WorkerInviteResponse(BaseModel):

    id: str
    """The id of the worker."""

    position: str

    type: Literal["employee", "contractor"]

    status: Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]

    start_date: str = FieldInfo(alias="startDate")
    """A date string in the form YYYY-MM-DD"""

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    is_business: Optional[bool] = FieldInfo(alias="isBusiness", default=None)

    business_name: Optional[str] = FieldInfo(alias="businessName", default=None)

    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")

    email: str
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    work_email: Optional[str] = FieldInfo(alias="workEmail", default=None)

    preferred_name: Optional[str] = FieldInfo(alias="preferredName", default=None)

    display_name: str = FieldInfo(alias="displayName")
    """The "ui" name of a worker. If it's a business contractor business name is used. Otherwise we default to preferred name, then first-last."""

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)
    """The IANA timezone of the worker (e.g., America/New_York)."""

    department: Optional[Department] = None
    """The department the worker belongs to, or null if unassigned."""



