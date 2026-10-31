# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PercentageContribution"]


class PercentageContribution(BaseModel):
    """A contribution expressed as a percentage of eligible earnings."""

    percentage: Union[float, Literal["Infinity", "-Infinity", "NaN"]]

    display: str
    """The server-formatted percentage, for example "3%"."""
