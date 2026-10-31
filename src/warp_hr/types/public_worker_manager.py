# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicWorkerManager"]


class PublicWorkerManager(BaseModel):
    """The worker's manager."""

    id: str
    """The id of the worker."""

    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")

    display_name: str = FieldInfo(alias="displayName")
