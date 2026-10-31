# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RetirementPlanCreateParams"]


class RetirementPlanCreateParams(TypedDict, total=False):
    type: Required[
        Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"]
    ]

    name: Required[str]

    effective_start_date: Required[Annotated[str, PropertyInfo(alias="effectiveStartDate")]]
