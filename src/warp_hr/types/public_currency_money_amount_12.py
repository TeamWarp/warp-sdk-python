# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["PublicCurrencyMoneyAmount12"]


class PublicCurrencyMoneyAmount12(BaseModel):
    """Calculated net pay after reimbursements, worker taxes, deductions, and benefit contributions. It excludes payment execution fees and may differ from the amount the worker ultimately receives. Null in both calculation and funding currencies until net pay is known in both."""

    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    display: str
    """The server-formatted display string for the amount in its currency."""
