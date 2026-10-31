# File generated from our OpenAPI spec by Scalar. See README.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_custom_field_value_output import PublicCustomFieldValueOutput

__all__ = ["CustomFieldUpsertValueResponse"]


class CustomFieldUpsertValueResponse(BaseModel):
    id: str
    """The tag of a company custom worker field value."""

    worker_id: str = FieldInfo(alias="workerId")
    """The id of the worker."""

    field_id: str = FieldInfo(alias="fieldId")
    """The tag of a company custom worker field."""

    value: PublicCustomFieldValueOutput

    updated_at: str = FieldInfo(alias="updatedAt")
