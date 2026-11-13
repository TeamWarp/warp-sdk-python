# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestCustomFields:
    @smoke_case("customFields.list:single", operation="list", path="/v1/custom_fields")
    def test_method_list(self) -> None:
        custom_field = client.custom_fields.list()

    @smoke_case("customFields.create:required", operation="create", path="/v1/custom_fields")
    def test_method_create(self) -> None:
        custom_field = client.custom_fields.create(
            name="x",
            type="text",
            category="info",
        )

    @smoke_case("customFields.create:all", operation="create", path="/v1/custom_fields")
    def test_method_create_with_all_params(self) -> None:
        custom_field = client.custom_fields.create(
            name="x",
            description="",
            type="text",
            config={},
            category="info",
            access_level="admins",
            input_by="admin",
            required=False,
            options=[{"label": "x", "value": "x"}],
        )

    @smoke_case("customFields.get:single", operation="get", path="/v1/custom_fields/{id}")
    def test_method_get(self) -> None:
        custom_field = client.custom_fields.get(
            id="cf_1234",
        )

    @smoke_case("customFields.update:required", operation="update", path="/v1/custom_fields/{id}")
    def test_method_update(self) -> None:
        custom_field = client.custom_fields.update(
            id="cf_1234",
        )

    @smoke_case("customFields.update:all", operation="update", path="/v1/custom_fields/{id}")
    def test_method_update_with_all_params(self) -> None:
        custom_field = client.custom_fields.update(
            id="cf_1234",
            name="x",
            description="",
            config={},
            category="info",
            access_level="admins",
            input_by="admin",
            required=False,
        )

    @smoke_case("customFields.archive:single", operation="archive", path="/v1/custom_fields/{id}/archive")
    def test_method_archive(self) -> None:
        custom_field = client.custom_fields.archive(
            id="cf_1234",
        )

    @smoke_case("customFields.createOption:required", operation="createOption", path="/v1/custom_fields/{id}/options")
    def test_method_create_option(self) -> None:
        custom_field = client.custom_fields.create_option(
            id="cf_1234",
            label="x",
            value="x",
        )

    @smoke_case("customFields.createOption:all", operation="createOption", path="/v1/custom_fields/{id}/options")
    def test_method_create_option_with_all_params(self) -> None:
        custom_field = client.custom_fields.create_option(
            id="cf_1234",
            label="x",
            value="x",
            sort_order=0,
        )

    @smoke_case("customFields.updateOption:required", operation="updateOption", path="/v1/custom_field_options/{id}")
    def test_method_update_option(self) -> None:
        custom_field = client.custom_fields.update_option(
            id="cfo_1234",
        )

    @smoke_case("customFields.updateOption:all", operation="updateOption", path="/v1/custom_field_options/{id}")
    def test_method_update_option_with_all_params(self) -> None:
        custom_field = client.custom_fields.update_option(
            id="cfo_1234",
            label="x",
            sort_order=0,
        )

    @smoke_case("customFields.deleteOption:single", operation="deleteOption", path="/v1/custom_field_options/{id}")
    def test_method_delete_option(self) -> None:
        client.custom_fields.delete_option(
            id="cfo_1234",
        )

    @smoke_case(
        "customFields.archiveOption:single", operation="archiveOption", path="/v1/custom_field_options/{id}/archive"
    )
    def test_method_archive_option(self) -> None:
        custom_field = client.custom_fields.archive_option(
            id="cfo_1234",
        )

    @smoke_case("customFields.listValues:required", operation="listValues", path="/v1/custom_field_values")
    def test_method_list_values(self) -> None:
        custom_field = client.custom_fields.list_values()

    @smoke_case("customFields.listValues:all", operation="listValues", path="/v1/custom_field_values")
    def test_method_list_values_with_all_params(self) -> None:
        custom_field = client.custom_fields.list_values(
            worker_ids=["wrk_1234"],
            field_ids=["cf_1234"],
        )

    @smoke_case("customFields.upsertValue:single", operation="upsertValue", path="/v1/custom_field_values")
    def test_method_upsert_value(self) -> None:
        custom_field = client.custom_fields.upsert_value(
            worker_id="wrk_1234",
            field_id="cf_1234",
            value={"type": "text", "value": ""},
        )

    @smoke_case("customFields.clearValue:single", operation="clearValue", path="/v1/custom_field_values")
    def test_method_clear_value(self) -> None:
        client.custom_fields.clear_value(
            worker_id="wrk_1234",
            field_id="cf_1234",
        )
