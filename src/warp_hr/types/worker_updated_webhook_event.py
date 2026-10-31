# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_worker_address import PublicWorkerAddress
from .public_worker_manager import PublicWorkerManager
from .public_worker_compensation import PublicWorkerCompensation
from .public_worker_custom_field import PublicWorkerCustomField

__all__ = ["WorkerUpdatedWebhookEvent", "Data", "DataDepartment", "DataPrimaryWorkplace", "DataLevel"]


class DataLevel(BaseModel):
    id: str
    """The unique public id of the job level"""

    code: str

    name: str

    track: Literal["ic", "manager", "executive"]


class DataPrimaryWorkplace(BaseModel):
    id: str
    """Public workplace identifier"""

    name: str

    type: Literal["remote", "office"]


class DataDepartment(BaseModel):
    id: str
    """The unique public id of the department"""

    name: str


class Data(BaseModel):
    id: str
    """The id of the worker."""

    position: str

    type: Literal["employee", "contractor"]

    status: Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]

    benefit_eligible: bool = FieldInfo(alias="benefitEligible")

    start_date: str = FieldInfo(alias="startDate")

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    is_business: Optional[bool] = FieldInfo(alias="isBusiness", default=None)

    business_name: Optional[str] = FieldInfo(alias="businessName", default=None)

    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")

    email: str
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    work_email: Optional[str] = FieldInfo(alias="workEmail", default=None)
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""

    preferred_name: Optional[str] = FieldInfo(alias="preferredName", default=None)

    biological_sex: Optional[Literal["male", "female"]] = FieldInfo(alias="biologicalSex", default=None)
    """The worker's biological sex, or null when unavailable."""

    marital_status: Optional[Literal["married", "not_married"]] = FieldInfo(alias="maritalStatus", default=None)
    """The worker's marital status, or null when unavailable."""

    date_of_birth: Optional[str] = FieldInfo(alias="dateOfBirth", default=None)
    """The worker's date of birth, or null when unavailable."""

    phone: Optional[str] = None
    """The worker's personal phone number, or null when unavailable."""

    address: Optional[PublicWorkerAddress] = None
    """The worker's home address, or null when unavailable."""

    display_name: str = FieldInfo(alias="displayName")
    """The "ui" name of a worker. If it's a business contractor business name is used. Otherwise we default to preferred name, then first-last."""

    manager: Optional[PublicWorkerManager] = None
    """The worker's manager, or null if unassigned."""

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)
    """The IANA timezone of the worker (e.g., America/New_York)."""

    t_shirt_size: Optional[Literal["XS", "S", "M", "L", "XL", "XXL", "XXXL"]] = FieldInfo(
        alias="tShirtSize", default=None
    )
    """The worker's stored T-shirt size, or null when unset or unavailable."""

    department: Optional[DataDepartment] = None
    """The department the worker belongs to, or null if unassigned."""

    primary_workplace: Optional[DataPrimaryWorkplace] = FieldInfo(alias="primaryWorkplace", default=None)
    """The primary workplace the worker is assigned to, or null if unassigned."""

    latest_rehire_date: Optional[str] = FieldInfo(alias="latestRehireDate", default=None)
    """The date the worker was most recently reactivated after an offboarding. This is distinct from startDate and is null if the worker has not been rehired."""

    termination_reason: Optional[str] = FieldInfo(alias="terminationReason", default=None)
    """The reason the worker was terminated, or null when no termination reason is recorded."""

    updated_at: str = FieldInfo(alias="updatedAt")

    level: Optional[DataLevel] = None
    """The worker's assigned job level, or null if unassigned. Omitted when job levels are not enabled."""

    compensation: Optional[PublicWorkerCompensation] = None
    """The worker's current regular compensation, or the rate effective on a future start date. Null when the worker has no applicable regular pay rate or the API key lacks the corresponding compensation read scope."""

    custom_fields: Optional[List[PublicWorkerCustomField]] = FieldInfo(alias="customFields", default=None)
    """The worker's custom field values. Every active company custom field appears; fields outside this API key's permission scopes are redacted (value null, redacted true) rather than omitted, so the list is identical across keys. Empty when the company has no custom fields."""


class WorkerUpdatedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier (format: `<objectTag>:<uuid>`). Stable across retries."""

    type: Literal["worker.updated"]
    """The event type."""

    timestamp: str
    """ISO 8601 timestamp of when the event occurred. Unchanged across retries."""

    data: Data
    """A worker profile, including lifecycle, workplace, profile, and compensation fields."""
