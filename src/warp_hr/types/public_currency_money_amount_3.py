# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount3"]


class PublicCurrencyMoneyAmount3(BaseModel):
    """Payroll taxes withheld from worker pay, reducing net pay."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
