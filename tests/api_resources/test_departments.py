# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestDepartments:
    @smoke_case("departments.list:required", operation="list", path="/v1/departments")
    def test_method_list(self) -> None:
        department = client.departments.list(
            limit="limit",
        )

    @smoke_case("departments.list:all", operation="list", path="/v1/departments")
    def test_method_list_with_all_params(self) -> None:
        department = client.departments.list(
            limit="limit",
            after_id="dpt_1234",
            before_id="dpt_1234",
        )

    @smoke_case("departments.create:single", operation="create", path="/v1/departments")
    def test_method_create(self) -> None:
        department = client.departments.create(
            name="x",
        )

    @smoke_case("departments.update:required", operation="update", path="/v1/departments/{id}")
    def test_method_update(self) -> None:
        department = client.departments.update(
            id="dpt_1234",
        )

    @smoke_case("departments.update:all", operation="update", path="/v1/departments/{id}")
    def test_method_update_with_all_params(self) -> None:
        department = client.departments.update(
            id="dpt_1234",
            name="",
        )
