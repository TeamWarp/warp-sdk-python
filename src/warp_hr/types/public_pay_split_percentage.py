# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PublicPaySplitPercentage"]


class PublicPaySplitPercentage(BaseModel):
    """A stored percentage from 0 to 100 with at most four decimal places and its server-formatted display. Values are preserved, not normalized to total 100 or predicted from provider execution."""

    percentage: Union[float, Literal["Infinity", "-Infinity", "NaN"]]

    display: str
