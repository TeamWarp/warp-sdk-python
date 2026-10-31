# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldClearValueParams"]


class CustomFieldClearValueParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """The id of the worker."""

    field_id: Required[Annotated[str, PropertyInfo(alias="fieldId")]]
    """The tag of a company custom worker field."""
