# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import TypeAlias

from .public_worker_ssn import PublicWorkerSsn

__all__ = ["WorkerRevealSsnResponse"]

WorkerRevealSsnResponse: TypeAlias = List[PublicWorkerSsn]
