# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .benefits.public_worker_reference import PublicWorkerReference

__all__ = ["PublicI9Verification"]


class PublicI9Verification(BaseModel):
    """I-9 workflow metadata and basic worker information without document contents or file links."""

    id: str
    """The tag of the i9 verification."""

    worker: PublicWorkerReference
    """Basic identifying information for a worker associated with another resource."""

    status: Literal["not_started", "awaiting_worker", "awaiting_admin", "verified"]

    start_date: str = FieldInfo(alias="startDate")

    verified_at: Optional[datetime] = FieldInfo(alias="verifiedAt", default=None)

    retention_until: Optional[str] = FieldInfo(alias="retentionUntil", default=None)

    due_date: Optional[str] = FieldInfo(alias="dueDate", default=None)
