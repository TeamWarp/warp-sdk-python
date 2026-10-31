# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["OfferVoidParams"]


class OfferVoidParams(TypedDict, total=False):
    void_reason: Required[Annotated[Literal["candidate_declined", "other"], PropertyInfo(alias="voidReason")]]

    void_notes: Annotated[Optional[str], PropertyInfo(alias="voidNotes")]
