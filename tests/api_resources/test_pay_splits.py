# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPaySplits:
    @smoke_case("paySplits.list:required", operation="list", path="/v1/pay_splits")
    def test_method_list(self) -> None:
        pay_split = client.pay_splits.list(
            limit="limit",
            statuses=["active"],
        )

    @smoke_case("paySplits.list:all", operation="list", path="/v1/pay_splits")
    def test_method_list_with_all_params(self) -> None:
        pay_split = client.pay_splits.list(
            limit="limit",
            after_id="nps_1234",
            before_id="nps_1234",
            worker_ids=["wrk_1234"],
            types=["percentage"],
            statuses=["active"],
        )

    @smoke_case("paySplits.get:single", operation="get", path="/v1/pay_splits/{id}")
    def test_method_get(self) -> None:
        pay_split = client.pay_splits.get(
            id="nps_1234",
        )
