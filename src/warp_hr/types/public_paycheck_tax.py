# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

from .public_tax_payer import PublicTaxPayer
from .public_payroll_currency import PublicPayrollCurrency

__all__ = ["PublicPaycheckTax", "Payer", "Amount", "AmountCurrency"]


class AmountCurrency(BaseModel):
    pass


class Amount(BaseModel):
    amount: int
    """minor units — cents, e.g. 2345 for $23.45"""

    currency: AmountCurrency

    display: str
    """The server-formatted display string for the amount in its currency."""


class Payer(BaseModel):
    pass


class PublicPaycheckTax(BaseModel):
    """One tax calculation line. Lines have no durable public identity."""

    payer: Payer

    amount: Amount
    """The tax amount attributed to the party identified by payer, expressed in the amount's currency."""

    description: Optional[str] = None
