# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["LevelListResponse", "LevelListResponseItem"]


class LevelListResponseItem(BaseModel):
    id: str
    """The unique public id of the job level"""

    code: str

    name: str

    track: Literal["ic", "manager", "executive"]


LevelListResponse: TypeAlias = List[LevelListResponseItem]
