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

from warp import Warp

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = Warp(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    status: str
    durationMs: int
    error: str


class SmokeCase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


def _smoke_case_0() -> None:
    time_off = client.time_off.list_assignments()

def _smoke_case_1() -> None:
    time_off = client.time_off.list_balances()

def _smoke_case_2() -> None:
    time_off = client.time_off.list_requests()

def _smoke_case_3() -> None:
    policy = client.time_off.policies.list()

def _smoke_case_4() -> None:
    policy = client.time_off.policies.retrieve(
        id="top_1234",
    )

def _smoke_case_5() -> None:
    worker = client.workers.list()

def _smoke_case_6() -> None:
    worker = client.workers.retrieve(
        id="wrk_1234",
    )

def _smoke_case_7() -> None:
    client.workers.delete(
        id="wrk_1234",
    )

def _smoke_case_8() -> None:
    worker = client.workers.create_employee(
        first_name="",
        last_name="",
        position="",
        start_date="2000-01-01",
        email="john@joinwarp.com",
        department_id="dpt_1234",
        manager_id="wrk_1234",
        work_location={"type": "office", "workplace_id": "wkp_1234"},
        compensation={"amount": 0, "per": "hour"},
    )

def _smoke_case_9() -> None:
    worker = client.workers.create_contractor(
        entity_type="individual",
        first_name="",
        last_name="",
        position="",
        start_date="2000-01-01",
        email="john@joinwarp.com",
        department_id="dpt_1234",
        manager_id="wrk_1234",
        work_country="AD",
    )

def _smoke_case_10() -> None:
    worker = client.workers.invite(
        id="wrk_1234",
    )

def _smoke_case_11() -> None:
    department = client.departments.list()

def _smoke_case_12() -> None:
    department = client.departments.create(
        name="",
    )

def _smoke_case_13() -> None:
    department = client.departments.update(
        id="dpt_1234",
    )

def _smoke_case_14() -> None:
    workplace = client.workplaces.list()

def _smoke_case_15() -> None:
    workplace = client.workplaces.create(
        name="",
        type="remote",
        address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
    )

def _smoke_case_16() -> None:
    workplace = client.workplaces.update(
        id="wkp_1234",
    )


cases: list[SmokeCase] = [
    {
        "operation": "listAssignments",
        "method": "GET",
        "path": "/v1/time_off/assignments",
        "run": _smoke_case_0,
    },

    {
        "operation": "listBalances",
        "method": "GET",
        "path": "/v1/time_off/balances",
        "run": _smoke_case_1,
    },

    {
        "operation": "listRequests",
        "method": "GET",
        "path": "/v1/time_off/requests",
        "run": _smoke_case_2,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/time_off/policies",
        "run": _smoke_case_3,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/time_off/policies/{id}",
        "run": _smoke_case_4,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workers",
        "run": _smoke_case_5,
    },

    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/workers/{id}",
        "run": _smoke_case_6,
    },

    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/workers/{id}",
        "run": _smoke_case_7,
    },

    {
        "operation": "createEmployee",
        "method": "POST",
        "path": "/v1/workers/employee",
        "run": _smoke_case_8,
    },

    {
        "operation": "createContractor",
        "method": "POST",
        "path": "/v1/workers/contractor",
        "run": _smoke_case_9,
    },

    {
        "operation": "invite",
        "method": "POST",
        "path": "/v1/workers/{id}/invite",
        "run": _smoke_case_10,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/departments",
        "run": _smoke_case_11,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/departments",
        "run": _smoke_case_12,
    },

    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/departments/{id}",
        "run": _smoke_case_13,
    },

    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/workplaces",
        "run": _smoke_case_14,
    },

    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/workplaces",
        "run": _smoke_case_15,
    },

    {
        "operation": "update",
        "method": "PATCH",
        "path": "/v1/workplaces/{id}",
        "run": _smoke_case_16,
    },

]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [
        case
        for case in cases
        if any(needle in case["operation"] or needle in case["path"] for needle in needles)
    ]


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


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    try:
        case["run"]()
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            "operation": case["operation"],
            "method": case["method"],
            "path": case["path"],
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
        Path(report_path).write_text(json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8")
    else:
        for result in results:
            if result["status"] == "passed":
                print(f"PASS {result['operation']} ({result['method']} {result['path']}) {result['durationMs']}ms")
            else:
                print(f"FAIL {result['operation']} ({result['method']} {result['path']})\n{result.get('error', '')}", file=sys.stderr)
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()
