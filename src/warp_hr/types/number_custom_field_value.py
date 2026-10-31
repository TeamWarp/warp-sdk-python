# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NumberCustomFieldValue"]


class NumberCustomFieldValue(BaseModel):
    type: Literal["number"]

    value: Union[float, Literal["Infinity", "-Infinity", "NaN"]]
