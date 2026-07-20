# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DepartmentCreateParams"]


class DepartmentCreateParams(TypedDict, total=False):

    name: Required[str]
    """a non empty string"""
