# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from warp_hr import Warp

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Warp(max_retries=2, timeout=10)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    health_plan = client.benefits.health_plans.list(
        limit="limit",
        statuses=["active"],
    )


def _smoke_case_1() -> None:
    health_plan = client.benefits.health_plans.list(
        limit="limit",
        after_id="chpl_1234",
        before_id="chpl_1234",
        types=["medical"],
        statuses=["active"],
        carrier_ids=["car_1234"],
    )


def _smoke_case_2() -> None:
    health_plan = client.benefits.health_plans.get(
        id="chpl_1234",
    )


def _smoke_case_3() -> None:
    retirement_plan = client.benefits.retirement_plans.list(
        limit="limit",
        statuses=["active"],
    )


def _smoke_case_4() -> None:
    retirement_plan = client.benefits.retirement_plans.list(
        limit="limit",
        after_id="crpl_1234",
        before_id="crpl_1234",
        types=["401k"],
        statuses=["active"],
    )


def _smoke_case_5() -> None:
    retirement_plan = client.benefits.retirement_plans.create(
        type="401k",
        name="x",
        effective_start_date="",
    )


def _smoke_case_6() -> None:
    retirement_plan = client.benefits.retirement_plans.get(
        id="crpl_1234",
    )


def _smoke_case_7() -> None:
    retirement_plan = client.benefits.retirement_plans.update(
        id="crpl_1234",
    )


def _smoke_case_8() -> None:
    retirement_plan = client.benefits.retirement_plans.update(
        id="crpl_1234",
        name="x",
        effective_start_date="",
        effective_end_date="",
    )


def _smoke_case_9() -> None:
    deduction = client.benefits.deductions.list(
        limit="limit",
        statuses=["active"],
    )


def _smoke_case_10() -> None:
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


def _smoke_case_11() -> None:
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


def _smoke_case_12() -> None:
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


def _smoke_case_13() -> None:
    deduction = client.benefits.deductions.get(
        id="pbdg_1234",
    )


def _smoke_case_14() -> None:
    deduction = client.benefits.deductions.update(
        id="pbdg_1234",
    )


def _smoke_case_15() -> None:
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


def _smoke_case_16() -> None:
    company = client.company.list()


def _smoke_case_17() -> None:
    custom_field = client.custom_fields.list()


def _smoke_case_18() -> None:
    custom_field = client.custom_fields.create(
        name="x",
        type="text",
        category="info",
    )


def _smoke_case_19() -> None:
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


def _smoke_case_20() -> None:
    custom_field = client.custom_fields.get(
        id="cf_1234",
    )


def _smoke_case_21() -> None:
    custom_field = client.custom_fields.update(
        id="cf_1234",
    )


def _smoke_case_22() -> None:
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


def _smoke_case_23() -> None:
    custom_field = client.custom_fields.archive(
        id="cf_1234",
    )


def _smoke_case_24() -> None:
    custom_field = client.custom_fields.create_option(
        id="cf_1234",
        label="x",
        value="x",
    )


def _smoke_case_25() -> None:
    custom_field = client.custom_fields.create_option(
        id="cf_1234",
        label="x",
        value="x",
        sort_order=0,
    )


def _smoke_case_26() -> None:
    custom_field = client.custom_fields.update_option(
        id="cfo_1234",
    )


def _smoke_case_27() -> None:
    custom_field = client.custom_fields.update_option(
        id="cfo_1234",
        label="x",
        sort_order=0,
    )


def _smoke_case_28() -> None:
    client.custom_fields.delete_option(
        id="cfo_1234",
    )


def _smoke_case_29() -> None:
    custom_field = client.custom_fields.archive_option(
        id="cfo_1234",
    )


def _smoke_case_30() -> None:
    custom_field = client.custom_fields.list_values()


def _smoke_case_31() -> None:
    custom_field = client.custom_fields.list_values(
        worker_ids=["wrk_1234"],
        field_ids=["cf_1234"],
    )


def _smoke_case_32() -> None:
    custom_field = client.custom_fields.upsert_value(
        worker_id="wrk_1234",
        field_id="cf_1234",
        value={"type": "text", "value": ""},
    )


def _smoke_case_33() -> None:
    client.custom_fields.clear_value(
        worker_id="wrk_1234",
        field_id="cf_1234",
    )


def _smoke_case_34() -> None:
    department = client.departments.list(
        limit="limit",
    )


def _smoke_case_35() -> None:
    department = client.departments.list(
        limit="limit",
        after_id="dpt_1234",
        before_id="dpt_1234",
    )


def _smoke_case_36() -> None:
    department = client.departments.create(
        name="x",
    )


def _smoke_case_37() -> None:
    department = client.departments.update(
        id="dpt_1234",
    )


def _smoke_case_38() -> None:
    department = client.departments.update(
        id="dpt_1234",
        name="",
    )


def _smoke_case_39() -> None:
    i9_verification = client.i9_verifications.list(
        limit="limit",
    )


def _smoke_case_40() -> None:
    i9_verification = client.i9_verifications.list(
        limit="limit",
        after_id="i9v_1234",
        before_id="i9v_1234",
        worker_ids=["wrk_1234"],
        statuses=["not_started"],
    )


def _smoke_case_41() -> None:
    i9_verification = client.i9_verifications.get(
        id="i9v_1234",
    )


def _smoke_case_42() -> None:
    bank_account = client.bank_accounts.list(
        limit="limit",
    )


def _smoke_case_43() -> None:
    bank_account = client.bank_accounts.list(
        limit="limit",
        after_id="bank_1234",
        before_id="bank_1234",
        worker_ids=["wrk_1234"],
        statuses=["verified"],
    )


def _smoke_case_44() -> None:
    bank_account = client.bank_accounts.get(
        id="bank_1234",
    )


def _smoke_case_45() -> None:
    level = client.levels.list()


def _smoke_case_46() -> None:
    offer = client.offers.list(
        limit="limit",
    )


def _smoke_case_47() -> None:
    offer = client.offers.list(
        limit="limit",
        after_id="offr_1234",
        before_id="offr_1234",
        statuses=["draft"],
        worker_types=["employee"],
        candidate_email="john@joinwarp.com",
    )


def _smoke_case_48() -> None:
    offer = client.offers.create(
        candidate={"first_name": "x", "last_name": "x", "email": "john@joinwarp.com"},
        position={"title": "x", "start_date": ""},
        worker_type="employee",
        compensation={"pay_basis": "year", "pay_currency": "USD", "pay_rate": 1},
    )


def _smoke_case_49() -> None:
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


def _smoke_case_50() -> None:
    offer = client.offers.void(
        id="offr_1234",
        void_reason="candidate_declined",
    )


def _smoke_case_51() -> None:
    offer = client.offers.void(
        id="offr_1234",
        void_reason="candidate_declined",
        void_notes="",
    )


def _smoke_case_52() -> None:
    offer = client.offers.extend_deadline(
        id="offr_1234",
        expiration_time="",
    )


def _smoke_case_53() -> None:
    offer = client.offers.resend(
        id="offr_1234",
    )


def _smoke_case_54() -> None:
    pay_rate = client.pay_rates.list(
        limit="limit",
    )


def _smoke_case_55() -> None:
    pay_rate = client.pay_rates.list(
        limit="limit",
        after_id="pyr_1234",
        before_id="pyr_1234",
        worker_id="wrk_1234",
        effective_on_or_after="effective_on_or_after",
        effective_before="effective_before",
        type="regular",
    )


def _smoke_case_56() -> None:
    pay_rate = client.pay_rates.get(
        id="pyr_1234",
    )


def _smoke_case_57() -> None:
    regular = client.pay_rates.regular.create(
        worker_id="wrk_khac8380c2Lm",
        type="salary",
        currency="USD",
        effective_date="",
    )


def _smoke_case_58() -> None:
    regular = client.pay_rates.regular.create(
        worker_id="wrk_khac8380c2Lm",
        type="salary",
        amount=12500000,
        currency="USD",
        effective_date="",
        require_hours_submission=False,
        description="",
        notes="",
    )


def _smoke_case_59() -> None:
    client.pay_rates.regular.delete(
        worker_id="wrk_khac8380c2Lm",
        effective_date="",
    )


def _smoke_case_60() -> None:
    pay_split = client.pay_splits.list(
        limit="limit",
        statuses=["active"],
    )


def _smoke_case_61() -> None:
    pay_split = client.pay_splits.list(
        limit="limit",
        after_id="nps_1234",
        before_id="nps_1234",
        worker_ids=["wrk_1234"],
        types=["percentage"],
        statuses=["active"],
    )


def _smoke_case_62() -> None:
    pay_split = client.pay_splits.get(
        id="nps_1234",
    )


def _smoke_case_63() -> None:
    payroll = client.payroll.list(
        limit="limit",
    )


def _smoke_case_64() -> None:
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


def _smoke_case_65() -> None:
    payroll = client.payroll.get(
        id="pay_1234",
    )


def _smoke_case_66() -> None:
    payroll = client.payroll.list_paychecks(
        limit="limit",
    )


def _smoke_case_67() -> None:
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


def _smoke_case_68() -> None:
    payroll = client.payroll.get_paycheck(
        id="pyc_1234",
    )


def _smoke_case_69() -> None:
    time_off = client.time_off.list_assignments(
        limit="limit",
    )


def _smoke_case_70() -> None:
    time_off = client.time_off.list_assignments(
        limit="limit",
        after_id="wrkasn_1234",
        before_id="wrkasn_1234",
        policy_ids=["top_1234"],
        worker_ids=["wrk_1234"],
    )


def _smoke_case_71() -> None:
    time_off = client.time_off.list_balances(
        limit="limit",
    )


def _smoke_case_72() -> None:
    time_off = client.time_off.list_balances(
        limit="limit",
        after_id="wrkasn_1234",
        before_id="wrkasn_1234",
        policy_ids=["top_1234"],
        worker_ids=["wrk_1234"],
        start_date="start_date",
        end_date="end_date",
    )


def _smoke_case_73() -> None:
    time_off = client.time_off.list_requests(
        limit="limit",
    )


def _smoke_case_74() -> None:
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


def _smoke_case_75() -> None:
    policy = client.time_off.policies.list(
        limit="limit",
    )


def _smoke_case_76() -> None:
    policy = client.time_off.policies.list(
        limit="limit",
        after_id="top_1234",
        before_id="top_1234",
    )


def _smoke_case_77() -> None:
    policy = client.time_off.policies.get(
        id="top_1234",
    )


def _smoke_case_78() -> None:
    worker = client.workers.update(
        id="wrk_1234",
    )


def _smoke_case_79() -> None:
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


def _smoke_case_80() -> None:
    worker = client.workers.get(
        id="wrk_1234",
    )


def _smoke_case_81() -> None:
    client.workers.delete(
        id="wrk_1234",
    )


def _smoke_case_82() -> None:
    worker = client.workers.reveal_ssn(
        worker_ids=["wrk_khac8380c2Lm", "wrk_q7Vm2pR9xK4c"],
    )


def _smoke_case_83() -> None:
    worker = client.workers.list(
        limit="limit",
    )


def _smoke_case_84() -> None:
    worker = client.workers.list(
        limit="limit",
        after_id="wrk_1234",
        before_id="wrk_1234",
        statuses=["draft"],
        types=["employee"],
        work_email="work_email",
    )


def _smoke_case_85() -> None:
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


def _smoke_case_86() -> None:
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


def _smoke_case_87() -> None:
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


def _smoke_case_88() -> None:
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


def _smoke_case_89() -> None:
    worker = client.workers.invite(
        id="wrk_1234",
    )


def _smoke_case_90() -> None:
    workplace = client.workplaces.list(
        limit="limit",
    )


def _smoke_case_91() -> None:
    workplace = client.workplaces.list(
        limit="limit",
        after_id="wkp_1234",
        before_id="wkp_1234",
    )


def _smoke_case_92() -> None:
    workplace = client.workplaces.create(
        name="x",
        type="remote",
        address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
    )


def _smoke_case_93() -> None:
    workplace = client.workplaces.create(
        name="x",
        type="remote",
        address={"line1": "x", "line2": "", "city": "", "postal_code": "", "state": "AL", "country": "US"},
    )


def _smoke_case_94() -> None:
    workplace = client.workplaces.update(
        id="wkp_1234",
    )


def _smoke_case_95() -> None:
    workplace = client.workplaces.update(
        id="wkp_1234",
        name="",
    )


cases: list[SmokeCase] = [
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/health_plans",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/health_plans",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/benefits/health_plans/{id}",
        "run": _smoke_case_2,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/retirement_plans",
        "label": "required params",
        "run": _smoke_case_3,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/retirement_plans",
        "label": "all params",
        "run": _smoke_case_4,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/benefits/retirement_plans",
        "run": _smoke_case_5,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/benefits/retirement_plans/{id}",
        "run": _smoke_case_6,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/benefits/retirement_plans/{id}",
        "label": "required params",
        "run": _smoke_case_7,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/benefits/retirement_plans/{id}",
        "label": "all params",
        "run": _smoke_case_8,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/deductions",
        "label": "required params",
        "run": _smoke_case_9,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/benefits/deductions",
        "label": "all params",
        "run": _smoke_case_10,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/benefits/deductions",
        "label": "required params",
        "run": _smoke_case_11,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/benefits/deductions",
        "label": "all params",
        "run": _smoke_case_12,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/benefits/deductions/{id}",
        "run": _smoke_case_13,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/benefits/deductions/{id}",
        "label": "required params",
        "run": _smoke_case_14,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/benefits/deductions/{id}",
        "label": "all params",
        "run": _smoke_case_15,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/company",
        "run": _smoke_case_16,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/custom_fields",
        "run": _smoke_case_17,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/custom_fields",
        "label": "required params",
        "run": _smoke_case_18,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/custom_fields",
        "label": "all params",
        "run": _smoke_case_19,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/custom_fields/{id}",
        "run": _smoke_case_20,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/custom_fields/{id}",
        "label": "required params",
        "run": _smoke_case_21,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/custom_fields/{id}",
        "label": "all params",
        "run": _smoke_case_22,
    },
    {
        "operation": "archive",
        "method": "POST",
        "path": "/v1/custom_fields/{id}/archive",
        "run": _smoke_case_23,
    },
    {
        "operation": "createOption",
        "method": "POST",
        "path": "/v1/custom_fields/{id}/options",
        "label": "required params",
        "run": _smoke_case_24,
    },
    {
        "operation": "createOption",
        "method": "POST",
        "path": "/v1/custom_fields/{id}/options",
        "label": "all params",
        "run": _smoke_case_25,
    },
    {
        "operation": "updateOption",
        "method": "PATCH",
        "path": "/v1/custom_field_options/{id}",
        "label": "required params",
        "run": _smoke_case_26,
    },
    {
        "operation": "updateOption",
        "method": "PATCH",
        "path": "/v1/custom_field_options/{id}",
        "label": "all params",
        "run": _smoke_case_27,
    },
    {
        "operation": "deleteOption",
        "method": "DELETE",
        "path": "/v1/custom_field_options/{id}",
        "run": _smoke_case_28,
    },
    {
        "operation": "archiveOption",
        "method": "POST",
        "path": "/v1/custom_field_options/{id}/archive",
        "run": _smoke_case_29,
    },
    {
        "operation": "listValues",
        "method": "GET",
        "path": "/v1/custom_field_values",
        "label": "required params",
        "run": _smoke_case_30,
    },
    {
        "operation": "listValues",
        "method": "GET",
        "path": "/v1/custom_field_values",
        "label": "all params",
        "run": _smoke_case_31,
    },
    {
        "operation": "upsertValue",
        "method": "PUT",
        "path": "/v1/custom_field_values",
        "run": _smoke_case_32,
    },
    {
        "operation": "clearValue",
        "method": "DELETE",
        "path": "/v1/custom_field_values",
        "run": _smoke_case_33,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/departments",
        "label": "required params",
        "run": _smoke_case_34,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/departments",
        "label": "all params",
        "run": _smoke_case_35,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/departments",
        "run": _smoke_case_36,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/departments/{id}",
        "label": "required params",
        "run": _smoke_case_37,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/departments/{id}",
        "label": "all params",
        "run": _smoke_case_38,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/i9_verifications",
        "label": "required params",
        "run": _smoke_case_39,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/i9_verifications",
        "label": "all params",
        "run": _smoke_case_40,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/i9_verifications/{id}",
        "run": _smoke_case_41,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/bank_accounts",
        "label": "required params",
        "run": _smoke_case_42,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/bank_accounts",
        "label": "all params",
        "run": _smoke_case_43,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/bank_accounts/{id}",
        "run": _smoke_case_44,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/levels",
        "run": _smoke_case_45,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/offers",
        "label": "required params",
        "run": _smoke_case_46,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/offers",
        "label": "all params",
        "run": _smoke_case_47,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/offers",
        "label": "required params",
        "run": _smoke_case_48,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/offers",
        "label": "all params",
        "run": _smoke_case_49,
    },
    {
        "operation": "void",
        "method": "POST",
        "path": "/v1/offers/{id}/void",
        "label": "required params",
        "run": _smoke_case_50,
    },
    {
        "operation": "void",
        "method": "POST",
        "path": "/v1/offers/{id}/void",
        "label": "all params",
        "run": _smoke_case_51,
    },
    {
        "operation": "extendDeadline",
        "method": "POST",
        "path": "/v1/offers/{id}/extend-deadline",
        "run": _smoke_case_52,
    },
    {
        "operation": "resend",
        "method": "POST",
        "path": "/v1/offers/{id}/resend",
        "run": _smoke_case_53,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pay_rates",
        "label": "required params",
        "run": _smoke_case_54,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pay_rates",
        "label": "all params",
        "run": _smoke_case_55,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/pay_rates/{id}",
        "run": _smoke_case_56,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/pay_rates/regular",
        "label": "required params",
        "run": _smoke_case_57,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/pay_rates/regular",
        "label": "all params",
        "run": _smoke_case_58,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/pay_rates/regular",
        "run": _smoke_case_59,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pay_splits",
        "label": "required params",
        "run": _smoke_case_60,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/pay_splits",
        "label": "all params",
        "run": _smoke_case_61,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/pay_splits/{id}",
        "run": _smoke_case_62,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/payrolls",
        "label": "required params",
        "run": _smoke_case_63,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/payrolls",
        "label": "all params",
        "run": _smoke_case_64,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/payrolls/{id}",
        "run": _smoke_case_65,
    },
    {
        "operation": "listPaychecks",
        "method": "GET",
        "path": "/v1/paychecks",
        "label": "required params",
        "run": _smoke_case_66,
    },
    {
        "operation": "listPaychecks",
        "method": "GET",
        "path": "/v1/paychecks",
        "label": "all params",
        "run": _smoke_case_67,
    },
    {
        "operation": "getPaycheck",
        "method": "GET",
        "path": "/v1/paychecks/{id}",
        "run": _smoke_case_68,
    },
    {
        "operation": "listAssignments",
        "method": "GET",
        "path": "/v1/time_off/assignments",
        "label": "required params",
        "run": _smoke_case_69,
    },
    {
        "operation": "listAssignments",
        "method": "GET",
        "path": "/v1/time_off/assignments",
        "label": "all params",
        "run": _smoke_case_70,
    },
    {
        "operation": "listBalances",
        "method": "GET",
        "path": "/v1/time_off/balances",
        "label": "required params",
        "run": _smoke_case_71,
    },
    {
        "operation": "listBalances",
        "method": "GET",
        "path": "/v1/time_off/balances",
        "label": "all params",
        "run": _smoke_case_72,
    },
    {
        "operation": "listRequests",
        "method": "GET",
        "path": "/v1/time_off/requests",
        "label": "required params",
        "run": _smoke_case_73,
    },
    {
        "operation": "listRequests",
        "method": "GET",
        "path": "/v1/time_off/requests",
        "label": "all params",
        "run": _smoke_case_74,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/time_off/policies",
        "label": "required params",
        "run": _smoke_case_75,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/time_off/policies",
        "label": "all params",
        "run": _smoke_case_76,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/time_off/policies/{id}",
        "run": _smoke_case_77,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/workers/{id}",
        "label": "required params",
        "run": _smoke_case_78,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/workers/{id}",
        "label": "all params",
        "run": _smoke_case_79,
    },
    {
        "operation": "get",
        "method": "GET",
        "path": "/v1/workers/{id}",
        "run": _smoke_case_80,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/workers/{id}",
        "run": _smoke_case_81,
    },
    {
        "operation": "revealSsn",
        "method": "POST",
        "path": "/v1/workers/reveal_ssn",
        "run": _smoke_case_82,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workers",
        "label": "required params",
        "run": _smoke_case_83,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workers",
        "label": "all params",
        "run": _smoke_case_84,
    },
    {
        "operation": "createEmployee",
        "method": "POST",
        "path": "/v1/workers/employee",
        "label": "required params",
        "run": _smoke_case_85,
    },
    {
        "operation": "createEmployee",
        "method": "POST",
        "path": "/v1/workers/employee",
        "label": "all params",
        "run": _smoke_case_86,
    },
    {
        "operation": "createContractor",
        "method": "POST",
        "path": "/v1/workers/contractor",
        "label": "required params",
        "run": _smoke_case_87,
    },
    {
        "operation": "createContractor",
        "method": "POST",
        "path": "/v1/workers/contractor",
        "label": "all params",
        "run": _smoke_case_88,
    },
    {
        "operation": "invite",
        "method": "POST",
        "path": "/v1/workers/{id}/invite",
        "run": _smoke_case_89,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workplaces",
        "label": "required params",
        "run": _smoke_case_90,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workplaces",
        "label": "all params",
        "run": _smoke_case_91,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/workplaces",
        "label": "required params",
        "run": _smoke_case_92,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/workplaces",
        "label": "all params",
        "run": _smoke_case_93,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/workplaces/{id}",
        "label": "required params",
        "run": _smoke_case_94,
    },
    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/workplaces/{id}",
        "label": "all params",
        "run": _smoke_case_95,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
