# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestWorkers:
    @smoke_case("workers.update:required", operation="update", path="/v1/workers/{id}")
    def test_method_update(self) -> None:
        worker = client.workers.update(
            id="wrk_1234",
        )

    @smoke_case("workers.update:all", operation="update", path="/v1/workers/{id}")
    def test_method_update_with_all_params(self) -> None:
        worker = client.workers.update(
            id="wrk_1234",
            first_name="x",
            last_name="x",
            preferred_name="",
            t_shirt_size="XS",
            email="john@joinwarp.com",
            work_email="john@joinwarp.com",
            phone="",
            time_zone="America/New_York",
            date_of_birth="1990-06-15",
            marital_status="married",
            biological_sex="male",
            address={},
            position="x",
            department_id="dpt_1234",
            manager_id="wrk_1234",
            level_id="jlvl_1234",
            start_date="",
            workplace_id="wkp_1234",
            state_registration="self_managed",
        )

    @smoke_case("workers.get:single", operation="get", path="/v1/workers/{id}")
    def test_method_get(self) -> None:
        worker = client.workers.get(
            id="wrk_1234",
        )

    @smoke_case("workers.delete:single", operation="delete", path="/v1/workers/{id}")
    def test_method_delete(self) -> None:
        client.workers.delete(
            id="wrk_1234",
        )

    @smoke_case("workers.revealSsn:single", operation="revealSsn", path="/v1/workers/reveal_ssn")
    def test_method_reveal_ssn(self) -> None:
        worker = client.workers.reveal_ssn(
            worker_ids=["wrk_khac8380c2Lm", "wrk_q7Vm2pR9xK4c"],
        )

    @smoke_case("workers.list:required", operation="list", path="/v1/workers")
    def test_method_list(self) -> None:
        worker = client.workers.list(
            limit="limit",
        )

    @smoke_case("workers.list:all", operation="list", path="/v1/workers")
    def test_method_list_with_all_params(self) -> None:
        worker = client.workers.list(
            limit="limit",
            after_id="wrk_1234",
            before_id="wrk_1234",
            statuses=["draft"],
            types=["employee"],
            work_email="work_email",
        )

    @smoke_case("workers.createEmployee:required", operation="createEmployee", path="/v1/workers/employee")
    def test_method_create_employee(self) -> None:
        worker = client.workers.create_employee(
            first_name="Jonathan",
            last_name="Galt",
            position="Software Engineer",
            start_date="",
            email="john@joinwarp.com",
            department_id="dpt_1234",
            manager_id="wrk_1234",
            work_location={"type": "office", "workplace_id": "wkp_1234"},
            compensation={"amount": 85000, "per": "hour"},
        )

    @smoke_case("workers.createEmployee:all", operation="createEmployee", path="/v1/workers/employee")
    def test_method_create_employee_with_all_params(self) -> None:
        worker = client.workers.create_employee(
            first_name="Jonathan",
            last_name="Galt",
            position="Software Engineer",
            start_date="",
            email="john@joinwarp.com",
            work_email="john@joinwarp.com",
            require_i9=False,
            state_registration="self_managed",
            department_id="dpt_1234",
            level_id="jlvl_1234",
            manager_id="wrk_1234",
            stock_options=10000,
            work_location={"type": "office", "workplace_id": "wkp_1234"},
            compensation={"amount": 85000, "per": "hour"},
            pay_schedule="weekly",
        )

    @smoke_case("workers.createContractor:required", operation="createContractor", path="/v1/workers/contractor")
    def test_method_create_contractor(self) -> None:
        worker = client.workers.create_contractor(
            entity_type="individual",
            first_name="Melissa",
            last_name="Jones",
            position="Design Consultant",
            start_date="",
            email="john@joinwarp.com",
            department_id="dpt_1234",
            manager_id="wrk_1234",
            work_country="AD",
        )

    @smoke_case("workers.createContractor:all", operation="createContractor", path="/v1/workers/contractor")
    def test_method_create_contractor_with_all_params(self) -> None:
        worker = client.workers.create_contractor(
            entity_type="individual",
            first_name="Melissa",
            last_name="Jones",
            position="Design Consultant",
            business_name="Galt Enterprises, LLC",
            scope_of_work="Frontend development for the customer dashboard",
            start_date="",
            email="john@joinwarp.com",
            work_email="john@joinwarp.com",
            department_id="dpt_1234",
            level_id="jlvl_1234",
            manager_id="wrk_1234",
            work_country="AD",
            compensation={"currency": "USD", "amount": 5000, "per": "year"},
            pay_schedule="weekly",
        )

    @smoke_case("workers.invite:single", operation="invite", path="/v1/workers/{id}/invite")
    def test_method_invite(self) -> None:
        worker = client.workers.invite(
            id="wrk_1234",
        )
