# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPolicies:
    @smoke_case("timeOff.policies.list:required", operation="list", path="/v1/time_off/policies")
    def test_method_list(self) -> None:
        policy = client.time_off.policies.list(
            limit="limit",
        )

    @smoke_case("timeOff.policies.list:all", operation="list", path="/v1/time_off/policies")
    def test_method_list_with_all_params(self) -> None:
        policy = client.time_off.policies.list(
            limit="limit",
            after_id="top_1234",
            before_id="top_1234",
        )

    @smoke_case("timeOff.policies.get:single", operation="get", path="/v1/time_off/policies/{id}")
    def test_method_get(self) -> None:
        policy = client.time_off.policies.get(
            id="top_1234",
        )
