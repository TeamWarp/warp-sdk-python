# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestI9Verifications:
    @smoke_case("i9Verifications.list:required", operation="list", path="/v1/i9_verifications")
    def test_method_list(self) -> None:
        i9_verification = client.i9_verifications.list(
            limit="limit",
        )

    @smoke_case("i9Verifications.list:all", operation="list", path="/v1/i9_verifications")
    def test_method_list_with_all_params(self) -> None:
        i9_verification = client.i9_verifications.list(
            limit="limit",
            after_id="i9v_1234",
            before_id="i9v_1234",
            worker_ids=["wrk_1234"],
            statuses=["not_started"],
        )

    @smoke_case("i9Verifications.get:single", operation="get", path="/v1/i9_verifications/{id}")
    def test_method_get(self) -> None:
        i9_verification = client.i9_verifications.get(
            id="i9v_1234",
        )
