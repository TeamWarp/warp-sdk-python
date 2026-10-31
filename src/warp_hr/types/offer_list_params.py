# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["OfferListParams"]


class OfferListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of the offer."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of the offer."""

    statuses: Optional[List[Literal["draft", "sent", "accepted", "void", "expired"]]]

    worker_types: Annotated[
        Optional[List[Literal["employee", "us_contractor", "global_contractor"]]], PropertyInfo(alias="workerTypes")
    ]

    candidate_email: Annotated[Optional[str], PropertyInfo(alias="candidateEmail")]
    """An email with a reasonably valid regex (based on RFC 5321 atext characters)"""
