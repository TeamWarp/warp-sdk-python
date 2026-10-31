# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount9"]


class PublicCurrencyMoneyAmount9(BaseModel):
    """Banking and transaction fees paid by the employer to fund and pay the payroll."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
