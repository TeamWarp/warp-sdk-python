# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomFieldArchiveOptionResponse"]


class CustomFieldArchiveOptionResponse(BaseModel):
    id: str
    """The tag of a company custom worker field option."""

    label: str

    value: str

    sort_order: Union[float, Literal["Infinity", "-Infinity", "NaN"]] = FieldInfo(alias="sortOrder")

    status: Literal["active", "archived"]

    created_at: str = FieldInfo(alias="createdAt")
