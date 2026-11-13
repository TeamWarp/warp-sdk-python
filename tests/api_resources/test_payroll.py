# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPayroll:
    @smoke_case("payroll.list:required", operation="list", path="/v1/payrolls")
    def test_method_list(self) -> None:
        payroll = client.payroll.list(
            limit="limit",
        )

    @smoke_case("payroll.list:all", operation="list", path="/v1/payrolls")
    def test_method_list_with_all_params(self) -> None:
        payroll = client.payroll.list(
            limit="limit",
            after_id="pay_1234",
            before_id="pay_1234",
            types=["us"],
            subtypes=["regular"],
            statuses=["processing"],
            pay_frequencies=["semimonthly"],
            payday_on_or_after="payday_on_or_after",
            payday_before="payday_before",
            pay_period_end_on_or_after="pay_period_end_on_or_after",
            pay_period_end_before="pay_period_end_before",
        )

    @smoke_case("payroll.get:single", operation="get", path="/v1/payrolls/{id}")
    def test_method_get(self) -> None:
        payroll = client.payroll.get(
            id="pay_1234",
        )

    @smoke_case("payroll.listPaychecks:required", operation="listPaychecks", path="/v1/paychecks")
    def test_method_list_paychecks(self) -> None:
        payroll = client.payroll.list_paychecks(
            limit="limit",
        )

    @smoke_case("payroll.listPaychecks:all", operation="listPaychecks", path="/v1/paychecks")
    def test_method_list_paychecks_with_all_params(self) -> None:
        payroll = client.payroll.list_paychecks(
            limit="limit",
            after_id="pyc_1234",
            before_id="pyc_1234",
            payroll_ids=["pay_1234"],
            worker_ids=["wrk_1234"],
            worker_types=["us_w2"],
            payroll_types=["us"],
            statuses=["processing"],
            payment_methods=["direct_deposit"],
            compensation_currencies=["USD"],
            pay_frequencies=["semimonthly"],
            payday_on_or_after="payday_on_or_after",
            payday_before="payday_before",
        )

    @smoke_case("payroll.getPaycheck:single", operation="getPaycheck", path="/v1/paychecks/{id}")
    def test_method_get_paycheck(self) -> None:
        payroll = client.payroll.get_paycheck(
            id="pyc_1234",
        )
