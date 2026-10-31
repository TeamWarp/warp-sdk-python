# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .public_pay_rate_type import PublicPayRateType

__all__ = ["PayRateListParams"]


class PayRateListParams(TypedDict, total=False):
    limit: Required[Optional[str]]

    after_id: Annotated[Optional[str], PropertyInfo(alias="afterId")]
    """The tag of the pay rate."""

    before_id: Annotated[Optional[str], PropertyInfo(alias="beforeId")]
    """The tag of the pay rate."""

    worker_id: Annotated[Optional[str], PropertyInfo(alias="workerId")]
    """Only return pay rates assigned to this worker."""

    effective_on_or_after: Annotated[Optional[str], PropertyInfo(alias="effectiveOnOrAfter")]
    """Only return pay rates whose effective start date is on or after this date."""

    effective_before: Annotated[Optional[str], PropertyInfo(alias="effectiveBefore")]
    """Only return pay rates whose effective start date is before this date."""

    type: Optional[PublicPayRateType]
    """Only return regular or additional pay rates of this type."""
