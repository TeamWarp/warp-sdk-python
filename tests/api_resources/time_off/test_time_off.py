# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestTimeOff:
    @smoke_case("timeOff.listAssignments:required", operation="listAssignments", path="/v1/time_off/assignments")
    def test_method_list_assignments(self) -> None:
        time_off = client.time_off.list_assignments(
            limit="limit",
        )

    @smoke_case("timeOff.listAssignments:all", operation="listAssignments", path="/v1/time_off/assignments")
    def test_method_list_assignments_with_all_params(self) -> None:
        time_off = client.time_off.list_assignments(
            limit="limit",
            after_id="wrkasn_1234",
            before_id="wrkasn_1234",
            policy_ids=["top_1234"],
            worker_ids=["wrk_1234"],
        )

    @smoke_case("timeOff.listBalances:required", operation="listBalances", path="/v1/time_off/balances")
    def test_method_list_balances(self) -> None:
        time_off = client.time_off.list_balances(
            limit="limit",
        )

    @smoke_case("timeOff.listBalances:all", operation="listBalances", path="/v1/time_off/balances")
    def test_method_list_balances_with_all_params(self) -> None:
        time_off = client.time_off.list_balances(
            limit="limit",
            after_id="wrkasn_1234",
            before_id="wrkasn_1234",
            policy_ids=["top_1234"],
            worker_ids=["wrk_1234"],
            start_date="start_date",
            end_date="end_date",
        )

    @smoke_case("timeOff.listRequests:required", operation="listRequests", path="/v1/time_off/requests")
    def test_method_list_requests(self) -> None:
        time_off = client.time_off.list_requests(
            limit="limit",
        )

    @smoke_case("timeOff.listRequests:all", operation="listRequests", path="/v1/time_off/requests")
    def test_method_list_requests_with_all_params(self) -> None:
        time_off = client.time_off.list_requests(
            limit="limit",
            after_id="after_id",
            before_id="before_id",
            statuses=["pending"],
            policy_ids=["top_1234"],
            worker_ids=["wrk_1234"],
            starts_on_or_after="starts_on_or_after",
            starts_before="starts_before",
            ends_on_or_after="ends_on_or_after",
            ends_before="ends_before",
        )
