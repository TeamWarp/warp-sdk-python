# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .public_payroll_money_amount import PublicPayrollMoneyAmount
from .public_hourly_rate import PublicHourlyRate
from .public_payroll_money_amount_1 import PublicPayrollMoneyAmount1

__all__ = ["PublicPaycheckEarning", "SourceRate", "SourceRateAmount", "SourceRateAmountCurrency"]


class SourceRateAmountCurrency(BaseModel):
    pass


class SourceRateAmount(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: SourceRateAmountCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class SourceRate(BaseModel):
    amount: SourceRateAmount

    basis: Literal["yearly", "monthly", "weekly", "hourly"]


class PublicPaycheckEarning(BaseModel):
    """One earning calculation line. Lines have no durable public identity."""

    type: Literal[
        "hourly",
        "salaried",
        "overtime",
        "double_overtime",
        "paid_holiday",
        "pto",
        "sick",
        "commission",
        "bonus",
        "severance",
        "non_hourly_regular",
        "fixed",
        "group_term_life",
        "other_imputed",
        "2_percent_shareholder_benefits",
    ]

    workplace_id: Optional[str] = FieldInfo(alias="workplaceId", default=None)
    """Public workplace identifier"""

    amount: PublicPayrollMoneyAmount
    """The gross earnings attributed to this line in the amount's currency."""

    hours: Optional[float] = None

    hourly_rate: Optional[PublicHourlyRate] = FieldInfo(alias="hourlyRate", default=None)
    """A non-negative major-unit hourly rate. The earning amount remains authoritative."""

    source_rate: Optional[SourceRate] = FieldInfo(alias="sourceRate", default=None)
    """The effective compensation rate captured when the earning was saved, before proration."""

    description: Optional[str] = None
