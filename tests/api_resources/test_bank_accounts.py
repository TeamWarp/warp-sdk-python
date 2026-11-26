# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestBankAccounts:
    @smoke_case("bankAccounts.list:required", operation="list", path="/v1/bank_accounts")
    def test_method_list(self) -> None:
        bank_account = client.bank_accounts.list(
            limit="limit",
        )

    @smoke_case("bankAccounts.list:all", operation="list", path="/v1/bank_accounts")
    def test_method_list_with_all_params(self) -> None:
        bank_account = client.bank_accounts.list(
            limit="limit",
            after_id="bank_1234",
            before_id="bank_1234",
            worker_ids=["wrk_1234"],
            statuses=["verified"],
        )

    @smoke_case("bankAccounts.get:single", operation="get", path="/v1/bank_accounts/{id}")
    def test_method_get(self) -> None:
        bank_account = client.bank_accounts.get(
            id="bank_1234",
        )
