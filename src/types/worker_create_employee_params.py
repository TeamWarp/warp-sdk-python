# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerCreateEmployeeParams", "WorkLocation", "WorkLocation2", "Compensation"]


class WorkerCreateEmployeeParams(TypedDict, total=False):

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """a non empty string"""

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """a non empty string"""

    position: Required[str]
    """The employee's job title."""

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]
    """A date string in the form YYYY-MM-DD"""

    email: Required[str]
    """Personal email address. The invite will be sent here."""

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]
    """Company-issued email address, if applicable."""

    require_i9: Annotated[bool, PropertyInfo(alias="requireI9")]
    """Whether the employee is required to complete I-9 work authorization. Set to false if the employee has already been verified off-platform. Defaults to true."""

    state_registration: Annotated[Literal["self_managed", "warp_managed"], PropertyInfo(alias="stateRegistration")]
    """How state tax registration is handled for this employee's work state. Required when hiring in a state where your company doesn't have an existing registration. Use 'self_managed' if you've already registered in this state, or 'warp_managed' for Warp to handle registration on your behalf."""

    department_id: Required[Annotated[str, PropertyInfo(alias="departmentId")]]
    """The department to assign this employee to."""

    manager_id: Required[Annotated[str, PropertyInfo(alias="managerId")]]
    """The worker id of this employee's direct manager."""

    stock_options: Annotated[Optional[float], PropertyInfo(alias="stockOptions")]
    """Number of stock options granted to this employee."""

    work_location: Required[Annotated[Union[WorkLocation, WorkLocation2], PropertyInfo(alias="workLocation")]]
    """Where the employee will work. Either an existing company workplace or a remote US state."""

    compensation: Required[Compensation]
    """The employee's base compensation."""

    pay_schedule: Annotated[Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]], PropertyInfo(alias="paySchedule")]
    """The employee's pay schedule. Must be a pay schedule that the company has configured."""


class Compensation(TypedDict, total=False):

    amount: Required[float]
    """a positive number"""

    per: Required[Literal["hour", "year"]]
    """Whether the amount is per hour or per year."""

class WorkLocation2(TypedDict, total=False):

    type: Required[Literal["remote"]]

    state: Required[Literal["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]]
    """The US state where the remote employee works. Required for tax purposes."""

class WorkLocation(TypedDict, total=False):

    type: Required[Literal["office"]]

    workplace_id: Required[Annotated[str, PropertyInfo(alias="workplaceId")]]
    """Public workplace identifier"""

