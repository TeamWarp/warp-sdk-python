# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PublicWorkerSsn"]


class PublicWorkerSsn(BaseModel):
    """A worker's decrypted Social Security number."""

    id: str
    """The id of the worker."""

    ssn: Optional[str] = None
    """The nine-digit Social Security number, or null when the worker has no SSN on file."""
