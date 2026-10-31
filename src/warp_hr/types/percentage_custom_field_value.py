# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PercentageCustomFieldValue"]


class PercentageCustomFieldValue(BaseModel):
    type: Literal["percentage"]

    value: Union[float, Literal["Infinity", "-Infinity", "NaN"]]
