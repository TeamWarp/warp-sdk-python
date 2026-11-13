# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPayRates:
    @smoke_case("payRates.list:required", operation="list", path="/v1/pay_rates")
    def test_method_list(self) -> None:
        pay_rate = client.pay_rates.list(
            limit="limit",
        )

    @smoke_case("payRates.list:all", operation="list", path="/v1/pay_rates")
    def test_method_list_with_all_params(self) -> None:
        pay_rate = client.pay_rates.list(
            limit="limit",
            after_id="pyr_1234",
            before_id="pyr_1234",
            worker_id="wrk_1234",
            effective_on_or_after="effective_on_or_after",
            effective_before="effective_before",
            type="regular",
        )

    @smoke_case("payRates.get:single", operation="get", path="/v1/pay_rates/{id}")
    def test_method_get(self) -> None:
        pay_rate = client.pay_rates.get(
            id="pyr_1234",
        )
