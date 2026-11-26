# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestOffers:
    @smoke_case("offers.list:required", operation="list", path="/v1/offers")
    def test_method_list(self) -> None:
        offer = client.offers.list(
            limit="limit",
        )

    @smoke_case("offers.list:all", operation="list", path="/v1/offers")
    def test_method_list_with_all_params(self) -> None:
        offer = client.offers.list(
            limit="limit",
            after_id="offr_1234",
            before_id="offr_1234",
            statuses=["draft"],
            worker_types=["employee"],
            candidate_email="john@joinwarp.com",
        )

    @smoke_case("offers.create:required", operation="create", path="/v1/offers")
    def test_method_create(self) -> None:
        offer = client.offers.create(
            candidate={"first_name": "x", "last_name": "x", "email": "john@joinwarp.com"},
            position={"title": "x", "start_date": ""},
            worker_type="employee",
            compensation={"pay_basis": "year", "pay_currency": "USD", "pay_rate": 1},
        )

    @smoke_case("offers.create:all", operation="create", path="/v1/offers")
    def test_method_create_with_all_params(self) -> None:
        offer = client.offers.create(
            candidate={
                "first_name": "x",
                "last_name": "x",
                "email": "john@joinwarp.com",
                "contractor_details": {"is_business": False, "legal_business_name": ""},
            },
            position={"title": "x", "start_date": "", "country": "AD", "scope_of_work": ""},
            department_id="dpt_1234",
            workplace_id="wkp_1234",
            manager_id="wrk_1234",
            level_id="jlvl_1234",
            worker_type="employee",
            compensation={
                "pay_basis": "year",
                "pay_currency": "USD",
                "pay_rate": 1,
                "pay_type": "fixed",
                "pay_variable_rate": 1,
                "sign_on_bonus": 1,
                "relocation_bonus": 1,
                "stock_options": 0,
                "vesting_schedule_months": 0,
                "cliff_months": 0,
            },
            expiration_time="",
            background_check_work_location={"country": "", "state": "", "city": ""},
        )

    @smoke_case("offers.void:required", operation="void", path="/v1/offers/{id}/void")
    def test_method_void(self) -> None:
        offer = client.offers.void(
            id="offr_1234",
            void_reason="candidate_declined",
        )

    @smoke_case("offers.void:all", operation="void", path="/v1/offers/{id}/void")
    def test_method_void_with_all_params(self) -> None:
        offer = client.offers.void(
            id="offr_1234",
            void_reason="candidate_declined",
            void_notes="",
        )

    @smoke_case("offers.extendDeadline:single", operation="extendDeadline", path="/v1/offers/{id}/extend-deadline")
    def test_method_extend_deadline(self) -> None:
        offer = client.offers.extend_deadline(
            id="offr_1234",
            expiration_time="",
        )

    @smoke_case("offers.resend:single", operation="resend", path="/v1/offers/{id}/resend")
    def test_method_resend(self) -> None:
        offer = client.offers.resend(
            id="offr_1234",
        )
