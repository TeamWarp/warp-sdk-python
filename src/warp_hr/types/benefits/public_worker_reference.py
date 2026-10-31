# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWorkerReference"]


class PublicWorkerReference(BaseModel):
    """Basic identifying information for a worker associated with another resource."""

    id: str
    """The worker id."""

    first_name: str = FieldInfo(alias="firstName")
    """The worker first name."""

    last_name: str = FieldInfo(alias="lastName")
    """The worker last name."""
