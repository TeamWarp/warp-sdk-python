# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestWorkplaces:
    @smoke_case("workplaces.list:required", operation="list", path="/v1/workplaces")
    def test_method_list(self) -> None:
        workplace = client.workplaces.list(
            limit="limit",
        )

    @smoke_case("workplaces.list:all", operation="list", path="/v1/workplaces")
    def test_method_list_with_all_params(self) -> None:
        workplace = client.workplaces.list(
            limit="limit",
            after_id="wkp_1234",
            before_id="wkp_1234",
        )

    @smoke_case("workplaces.create:required", operation="create", path="/v1/workplaces")
    def test_method_create(self) -> None:
        workplace = client.workplaces.create(
            name="x",
            type="remote",
            address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
        )

    @smoke_case("workplaces.create:all", operation="create", path="/v1/workplaces")
    def test_method_create_with_all_params(self) -> None:
        workplace = client.workplaces.create(
            name="x",
            type="remote",
            address={"line1": "x", "line2": "", "city": "", "postal_code": "", "state": "AL", "country": "US"},
        )

    @smoke_case("workplaces.update:required", operation="update", path="/v1/workplaces/{id}")
    def test_method_update(self) -> None:
        workplace = client.workplaces.update(
            id="wkp_1234",
        )

    @smoke_case("workplaces.update:all", operation="update", path="/v1/workplaces/{id}")
    def test_method_update_with_all_params(self) -> None:
        workplace = client.workplaces.update(
            id="wkp_1234",
            name="",
        )
