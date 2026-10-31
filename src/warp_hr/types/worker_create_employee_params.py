# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WorkerCreateEmployeeParams",
    "WorkLocation",
    "WorkLocationOfficeWorkLocation",
    "WorkLocationRemoteWorkLocation",
    "Compensation",
]


class WorkerCreateEmployeeParams(TypedDict, total=False):
    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]

    position: Required[str]
    """The employee's job title."""

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]

    email: Required[str]
    """Personal email address. The invite will be sent here."""

    work_email: Annotated[Optional[str], PropertyInfo(alias="workEmail")]
    """Company-issued email address, if applicable."""

    require_i9: Annotated[Optional[bool], PropertyInfo(alias="requireI9")]
    """Whether the employee is required to complete I-9 work authorization. Set to false if the employee has already been verified off-platform. Defaults to true."""

    state_registration: Annotated[
        Optional[Literal["self_managed", "warp_managed"]], PropertyInfo(alias="stateRegistration")
    ]
    """How state tax registration is handled for this employee's work state. Required when hiring in a state where your company doesn't have an existing registration. Use 'self_managed' if you've already registered in this state, or 'warp_managed' for Warp to handle registration on your behalf."""

    department_id: Required[Annotated[str, PropertyInfo(alias="departmentId")]]
    """The department to assign this employee to."""

    level_id: Annotated[Optional[str], PropertyInfo(alias="levelId")]
    """The job level to assign this employee to, or null to leave unassigned. Omit this field when job levels are not enabled."""

    manager_id: Required[Annotated[str, PropertyInfo(alias="managerId")]]
    """The worker id of this employee's direct manager."""

    stock_options: Annotated[
        Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]], PropertyInfo(alias="stockOptions")
    ]
    """Number of stock options granted to this employee."""

    work_location: Required[Annotated[WorkLocation, PropertyInfo(alias="workLocation")]]
    """Where the employee will work. Either an existing company workplace or a remote US state."""

    compensation: Required[Compensation]
    """The employee's base compensation."""

    pay_schedule: Annotated[
        Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]],
        PropertyInfo(alias="paySchedule"),
    ]
    """The employee's pay schedule. Must be a pay schedule that the company has configured."""


class Compensation(TypedDict, total=False):
    amount: Required[float]
    """The pay amount. Interpreted based on the "per" field."""

    per: Required[Literal["hour", "year"]]
    """Whether the amount is per hour or per year."""


class WorkLocationRemoteWorkLocation(TypedDict, total=False):
    """Employee works remotely from a US state."""

    type: Required[Literal["remote"]]

    state: Required[
        Literal[
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DC",
            "DE",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
        ]
    ]
    """The US state where the remote employee works. Required for tax purposes."""


class WorkLocationOfficeWorkLocation(TypedDict, total=False):
    """Employee works from a company workplace."""

    type: Required[Literal["office"]]

    workplace_id: Required[Annotated[str, PropertyInfo(alias="workplaceId")]]
    """Public workplace identifier"""


WorkLocation: TypeAlias = Union[WorkLocationOfficeWorkLocation, WorkLocationRemoteWorkLocation]
