# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PublicPaycheckWorker"]


class PublicPaycheckWorker(BaseModel):
    """The worker identity and historical classification associated with a paycheck."""

    id: str
    """The worker id."""

    first_name: str = FieldInfo(alias="firstName")
    """The worker first name."""

    last_name: str = FieldInfo(alias="lastName")
    """The worker last name."""

    display_name: str = FieldInfo(alias="displayName")

    worker_type: Literal["us_w2", "us_1099", "global_contractor", "eor_employee"] = FieldInfo(alias="workerType")
