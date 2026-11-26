# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestDeductions:
    @smoke_case("benefits.deductions.list:required", operation="list", path="/v1/benefits/deductions")
    def test_method_list(self) -> None:
        deduction = client.benefits.deductions.list(
            limit="limit",
            statuses=["active"],
        )

    @smoke_case("benefits.deductions.list:all", operation="list", path="/v1/benefits/deductions")
    def test_method_list_with_all_params(self) -> None:
        deduction = client.benefits.deductions.list(
            limit="limit",
            after_id="pbdg_1234",
            before_id="pbdg_1234",
            worker_ids=["wrk_1234"],
            categories=["health"],
            types=["medical"],
            statuses=["active"],
            health_plan_ids=["chpl_1234"],
            retirement_plan_ids=["crpl_1234"],
        )

    @smoke_case("benefits.deductions.create:required", operation="create", path="/v1/benefits/deductions")
    def test_method_create(self) -> None:
        deduction = client.benefits.deductions.create(
            worker_id="wrk_1234",
            type="medical",
            calculation={
                "type": "fixed_amount",
                "frequency": "monthly",
                "employee_contribution": {"amount": 0, "currency": "USD"},
                "employer_contribution": {"amount": 0, "currency": "USD"},
            },
            effective_start_date="",
        )

    @smoke_case("benefits.deductions.create:all", operation="create", path="/v1/benefits/deductions")
    def test_method_create_with_all_params(self) -> None:
        deduction = client.benefits.deductions.create(
            worker_id="wrk_1234",
            type="medical",
            plan={"type": "health_plan", "id": "chpl_1234"},
            name="x",
            calculation={
                "type": "fixed_amount",
                "frequency": "monthly",
                "employee_contribution": {"amount": 0, "currency": "USD"},
                "employer_contribution": {"amount": 0, "currency": "USD"},
            },
            recurrence="recurring",
            effective_start_date="",
            effective_end_date="",
        )

    @smoke_case("benefits.deductions.get:single", operation="get", path="/v1/benefits/deductions/{id}")
    def test_method_get(self) -> None:
        deduction = client.benefits.deductions.get(
            id="pbdg_1234",
        )

    @smoke_case("benefits.deductions.update:required", operation="update", path="/v1/benefits/deductions/{id}")
    def test_method_update(self) -> None:
        deduction = client.benefits.deductions.update(
            id="pbdg_1234",
        )

    @smoke_case("benefits.deductions.update:all", operation="update", path="/v1/benefits/deductions/{id}")
    def test_method_update_with_all_params(self) -> None:
        deduction = client.benefits.deductions.update(
            id="pbdg_1234",
            name="x",
            calculation={
                "type": "fixed_amount",
                "frequency": "monthly",
                "employee_contribution": {"amount": 0, "currency": "USD"},
                "employer_contribution": {"amount": 0, "currency": "USD"},
            },
            recurrence="recurring",
            status="active",
            effective_end_date="",
        )
