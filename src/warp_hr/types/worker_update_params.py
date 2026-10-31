# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerUpdateParams"]


class WorkerUpdateParams(TypedDict, total=False):
    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    preferred_name: Annotated[Optional[str], PropertyInfo(alias="preferredName")]

    t_shirt_size: Annotated[
        Optional[Literal["XS", "S", "M", "L", "XL", "XXL", "XXXL"]], PropertyInfo(alias="tShirtSize")
    ]

    email: str
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    phone: str

    time_zone: Annotated[str, PropertyInfo(alias="timeZone")]

    date_of_birth: Annotated[str, PropertyInfo(alias="dateOfBirth")]

    marital_status: Annotated[Literal["married", "not_married"], PropertyInfo(alias="maritalStatus")]

    biological_sex: Annotated[Literal["male", "female"], PropertyInfo(alias="biologicalSex")]

    address: object

    position: str

    department_id: Annotated[Optional[str], PropertyInfo(alias="departmentId")]
    """The unique public id of the department"""

    manager_id: Annotated[Optional[str], PropertyInfo(alias="managerId")]
    """The id of the worker."""

    level_id: Annotated[Optional[str], PropertyInfo(alias="levelId")]
    """The unique public id of the job level"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]

    workplace_id: Annotated[Optional[str], PropertyInfo(alias="workplaceId")]
    """Public workplace identifier"""

    state_registration: Annotated[Literal["self_managed", "warp_managed"], PropertyInfo(alias="stateRegistration")]
