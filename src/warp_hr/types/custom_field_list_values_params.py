# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

__all__ = ["CustomFieldListValuesParams"]


class CustomFieldListValuesParams(TypedDict, total=False):
    worker_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="workerIds")]

    field_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="fieldIds")]
