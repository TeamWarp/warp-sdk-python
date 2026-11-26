# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestCompany:
    @smoke_case("company.list:single", operation="list", path="/v1/company")
    def test_method_list(self) -> None:
        company = client.company.list()
