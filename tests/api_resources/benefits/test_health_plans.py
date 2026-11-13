# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestHealthPlans:
    @smoke_case("benefits.healthPlans.list:required", operation="list", path="/v1/benefits/health_plans")
    def test_method_list(self) -> None:
        health_plan = client.benefits.health_plans.list(
            limit="limit",
            statuses=["active"],
        )

    @smoke_case("benefits.healthPlans.list:all", operation="list", path="/v1/benefits/health_plans")
    def test_method_list_with_all_params(self) -> None:
        health_plan = client.benefits.health_plans.list(
            limit="limit",
            after_id="chpl_1234",
            before_id="chpl_1234",
            types=["medical"],
            statuses=["active"],
            carrier_ids=["car_1234"],
        )

    @smoke_case("benefits.healthPlans.get:single", operation="get", path="/v1/benefits/health_plans/{id}")
    def test_method_get(self) -> None:
        health_plan = client.benefits.health_plans.get(
            id="chpl_1234",
        )
