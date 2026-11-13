# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestRetirementPlans:
    @smoke_case("benefits.retirementPlans.list:required", operation="list", path="/v1/benefits/retirement_plans")
    def test_method_list(self) -> None:
        retirement_plan = client.benefits.retirement_plans.list(
            limit="limit",
            statuses=["active"],
        )

    @smoke_case("benefits.retirementPlans.list:all", operation="list", path="/v1/benefits/retirement_plans")
    def test_method_list_with_all_params(self) -> None:
        retirement_plan = client.benefits.retirement_plans.list(
            limit="limit",
            after_id="crpl_1234",
            before_id="crpl_1234",
            types=["401k"],
            statuses=["active"],
        )

    @smoke_case("benefits.retirementPlans.create:single", operation="create", path="/v1/benefits/retirement_plans")
    def test_method_create(self) -> None:
        retirement_plan = client.benefits.retirement_plans.create(
            type="401k",
            name="x",
            effective_start_date="",
        )

    @smoke_case("benefits.retirementPlans.get:single", operation="get", path="/v1/benefits/retirement_plans/{id}")
    def test_method_get(self) -> None:
        retirement_plan = client.benefits.retirement_plans.get(
            id="crpl_1234",
        )

    @smoke_case(
        "benefits.retirementPlans.update:required", operation="update", path="/v1/benefits/retirement_plans/{id}"
    )
    def test_method_update(self) -> None:
        retirement_plan = client.benefits.retirement_plans.update(
            id="crpl_1234",
        )

    @smoke_case("benefits.retirementPlans.update:all", operation="update", path="/v1/benefits/retirement_plans/{id}")
    def test_method_update_with_all_params(self) -> None:
        retirement_plan = client.benefits.retirement_plans.update(
            id="crpl_1234",
            name="x",
            effective_start_date="",
            effective_end_date="",
        )
