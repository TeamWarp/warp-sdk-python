# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount11"]


class PublicCurrencyMoneyAmount11(BaseModel):
    """The provider-reported amount the employer must fund for the payroll, when available."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
