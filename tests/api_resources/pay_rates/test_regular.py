# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRegular:
    @smoke_case("payRates.regular.create:required", operation="create", path="/v1/pay_rates/regular")
    def test_method_create(self) -> None:
        regular = client.pay_rates.regular.create(
            worker_id="wrk_khac8380c2Lm",
            type="salary",
            currency="USD",
            effective_date="",
        )

    @smoke_case("payRates.regular.create:all", operation="create", path="/v1/pay_rates/regular")
    def test_method_create_with_all_params(self) -> None:
        regular = client.pay_rates.regular.create(
            worker_id="wrk_khac8380c2Lm",
            type="salary",
            amount=12500000,
            currency="USD",
            effective_date="",
            require_hours_submission=False,
            description="",
            notes="",
        )

    @smoke_case("payRates.regular.delete:single", operation="delete", path="/v1/pay_rates/regular")
    def test_method_delete(self) -> None:
        client.pay_rates.regular.delete(
            worker_id="wrk_khac8380c2Lm",
            effective_date="",
        )
