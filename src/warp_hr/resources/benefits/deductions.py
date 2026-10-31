# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal
from ..._types import SequenceNotStr

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.benefits.deduction_list_response import DeductionListResponse
from ...types.benefits.public_benefit_deduction_category import PublicBenefitDeductionCategory
from ...types.benefits.public_benefit_deduction_status import PublicBenefitDeductionStatus
from ...types.benefits import deduction_list_params, deduction_create_params, deduction_update_params
from ...types.benefits.public_benefit_deduction_1 import PublicBenefitDeduction1
from ...types.benefits.public_benefit_deduction import PublicBenefitDeduction

__all__ = ["DeductionsResource", "AsyncDeductionsResource"]


class DeductionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeductionsResourceWithRawResponse:
        return DeductionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeductionsResourceWithStreamingResponse:
        return DeductionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        categories: Optional[List[PublicBenefitDeductionCategory]] | Omit = omit,
        types: Optional[
            List[
                Literal[
                    "medical",
                    "dental",
                    "vision",
                    "life",
                    "short_term_disability",
                    "long_term_disability",
                    "401k",
                    "roth_401k",
                    "403b",
                    "roth_403b",
                    "457",
                    "roth_457",
                    "hsa",
                    "fsa_medical",
                    "fsa_dependent_care",
                    "transit",
                    "parking",
                    "accident",
                    "cancer",
                    "critical_illness",
                    "hospital",
                    "medical_other",
                    "simple_ira",
                    "roth_simple_ira",
                    "nqdc",
                    "nontaxable_fringe",
                    "pucc",
                    "voluntary",
                    "post_tax",
                    "other",
                ]
            ]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicBenefitDeductionStatus]],
        health_plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        retirement_plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeductionListResponse:
        """
        List current payroll benefit deductions. Defaults to active deductions. A deduction whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The version-group tag of a payroll benefit deduction. Stable across edits.
            before_id: The version-group tag of a payroll benefit deduction. Stable across edits.
            worker_ids: Query parameter.
            categories: Query parameter.
            types: Query parameter.
            statuses: Query parameter.
            health_plan_ids: Query parameter.
            retirement_plan_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DeductionListResponse: Success

        Example:
            ```python
            deduction = client.benefits.deductions.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return self._get(
            "/v1/benefits/deductions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after_id": after_id,
                        "before_id": before_id,
                        "worker_ids": worker_ids,
                        "categories": categories,
                        "types": types,
                        "statuses": statuses,
                        "health_plan_ids": health_plan_ids,
                        "retirement_plan_ids": retirement_plan_ids,
                    },
                    deduction_list_params.DeductionListParams,
                ),
            ),
            cast_to=DeductionListResponse,
        )

    def create(
        self,
        *,
        worker_id: str,
        type: Literal[
            "medical",
            "dental",
            "vision",
            "life",
            "short_term_disability",
            "long_term_disability",
            "401k",
            "roth_401k",
            "403b",
            "roth_403b",
            "457",
            "roth_457",
            "simple_ira",
            "roth_simple_ira",
            "hsa",
            "fsa_medical",
            "fsa_dependent_care",
            "transit",
            "parking",
            "accident",
            "cancer",
            "critical_illness",
            "hospital",
            "medical_other",
            "nqdc",
            "nontaxable_fringe",
        ],
        plan: Optional[deduction_create_params.Plan] | Omit = omit,
        name: Optional[str] | Omit = omit,
        calculation: deduction_create_params.Calculation,
        recurrence: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        effective_start_date: str,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction1:
        """
        Create a benefit deduction for a worker.

        Args:
            worker_id: The id of the worker.
            type: The payroll deduction type to create.
            plan: A matching company plan, or null for a planless deduction.
            name: Body parameter.
            calculation: Both contributions must be supplied.
            recurrence: Body parameter.
            effective_start_date: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction1

        Example:
            ```python
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
            ```
        """
        return self._post(
            "/v1/benefits/deductions",
            body=maybe_transform(
                {
                    "worker_id": worker_id,
                    "type": type,
                    "plan": plan,
                    "name": name,
                    "calculation": calculation,
                    "recurrence": recurrence,
                    "effective_start_date": effective_start_date,
                    "effective_end_date": effective_end_date,
                },
                deduction_create_params.DeductionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction1,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction:
        """
        Get the current version of a company benefit deduction by id.

        Args:
            id: The version-group tag of a payroll benefit deduction. Stable across edits.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction

        Example:
            ```python
            deduction = client.benefits.deductions.get(
                id="pbdg_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/benefits/deductions/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction,
        )

    def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        calculation: Optional[deduction_update_params.Calculation] | Omit = omit,
        recurrence: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        status: Optional[Literal["active", "terminated"]] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction:
        """
        Update a benefit deduction. The calculation type cannot change.

        Args:
            id: The version-group tag of a payroll benefit deduction. Stable across edits.
            name: Body parameter.
            calculation: Both contributions must be supplied.
            recurrence: Body parameter.
            status: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction

        Example:
            ```python
            deduction = client.benefits.deductions.update(
                id="pbdg_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/benefits/deductions/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "calculation": calculation,
                    "recurrence": recurrence,
                    "status": status,
                    "effective_end_date": effective_end_date,
                },
                deduction_update_params.DeductionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction,
        )


class AsyncDeductionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeductionsResourceWithRawResponse:
        return AsyncDeductionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeductionsResourceWithStreamingResponse:
        return AsyncDeductionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        categories: Optional[List[PublicBenefitDeductionCategory]] | Omit = omit,
        types: Optional[
            List[
                Literal[
                    "medical",
                    "dental",
                    "vision",
                    "life",
                    "short_term_disability",
                    "long_term_disability",
                    "401k",
                    "roth_401k",
                    "403b",
                    "roth_403b",
                    "457",
                    "roth_457",
                    "hsa",
                    "fsa_medical",
                    "fsa_dependent_care",
                    "transit",
                    "parking",
                    "accident",
                    "cancer",
                    "critical_illness",
                    "hospital",
                    "medical_other",
                    "simple_ira",
                    "roth_simple_ira",
                    "nqdc",
                    "nontaxable_fringe",
                    "pucc",
                    "voluntary",
                    "post_tax",
                    "other",
                ]
            ]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicBenefitDeductionStatus]],
        health_plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        retirement_plan_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeductionListResponse:
        """
        List current payroll benefit deductions. Defaults to active deductions. A deduction whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The version-group tag of a payroll benefit deduction. Stable across edits.
            before_id: The version-group tag of a payroll benefit deduction. Stable across edits.
            worker_ids: Query parameter.
            categories: Query parameter.
            types: Query parameter.
            statuses: Query parameter.
            health_plan_ids: Query parameter.
            retirement_plan_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            DeductionListResponse: Success

        Example:
            ```python
            deduction = await client.benefits.deductions.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return await self._get(
            "/v1/benefits/deductions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "after_id": after_id,
                        "before_id": before_id,
                        "worker_ids": worker_ids,
                        "categories": categories,
                        "types": types,
                        "statuses": statuses,
                        "health_plan_ids": health_plan_ids,
                        "retirement_plan_ids": retirement_plan_ids,
                    },
                    deduction_list_params.DeductionListParams,
                ),
            ),
            cast_to=DeductionListResponse,
        )

    async def create(
        self,
        *,
        worker_id: str,
        type: Literal[
            "medical",
            "dental",
            "vision",
            "life",
            "short_term_disability",
            "long_term_disability",
            "401k",
            "roth_401k",
            "403b",
            "roth_403b",
            "457",
            "roth_457",
            "simple_ira",
            "roth_simple_ira",
            "hsa",
            "fsa_medical",
            "fsa_dependent_care",
            "transit",
            "parking",
            "accident",
            "cancer",
            "critical_illness",
            "hospital",
            "medical_other",
            "nqdc",
            "nontaxable_fringe",
        ],
        plan: Optional[deduction_create_params.Plan] | Omit = omit,
        name: Optional[str] | Omit = omit,
        calculation: deduction_create_params.Calculation,
        recurrence: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        effective_start_date: str,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction1:
        """
        Create a benefit deduction for a worker.

        Args:
            worker_id: The id of the worker.
            type: The payroll deduction type to create.
            plan: A matching company plan, or null for a planless deduction.
            name: Body parameter.
            calculation: Both contributions must be supplied.
            recurrence: Body parameter.
            effective_start_date: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction1

        Example:
            ```python
            deduction = await client.benefits.deductions.create(
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
            ```
        """
        return await self._post(
            "/v1/benefits/deductions",
            body=await async_maybe_transform(
                {
                    "worker_id": worker_id,
                    "type": type,
                    "plan": plan,
                    "name": name,
                    "calculation": calculation,
                    "recurrence": recurrence,
                    "effective_start_date": effective_start_date,
                    "effective_end_date": effective_end_date,
                },
                deduction_create_params.DeductionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction1,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction:
        """
        Get the current version of a company benefit deduction by id.

        Args:
            id: The version-group tag of a payroll benefit deduction. Stable across edits.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction

        Example:
            ```python
            deduction = await client.benefits.deductions.get(
                id="pbdg_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/benefits/deductions/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction,
        )

    async def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        calculation: Optional[deduction_update_params.Calculation] | Omit = omit,
        recurrence: Optional[Literal["recurring", "one_time"]] | Omit = omit,
        status: Optional[Literal["active", "terminated"]] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicBenefitDeduction:
        """
        Update a benefit deduction. The calculation type cannot change.

        Args:
            id: The version-group tag of a payroll benefit deduction. Stable across edits.
            name: Body parameter.
            calculation: Both contributions must be supplied.
            recurrence: Body parameter.
            status: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBenefitDeduction

        Example:
            ```python
            deduction = await client.benefits.deductions.update(
                id="pbdg_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/benefits/deductions/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "calculation": calculation,
                    "recurrence": recurrence,
                    "status": status,
                    "effective_end_date": effective_end_date,
                },
                deduction_update_params.DeductionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBenefitDeduction,
        )


class DeductionsResourceWithRawResponse:
    def __init__(self, deductions: DeductionsResource) -> None:
        self._deductions = deductions

        self.list = to_raw_response_wrapper(
            deductions.list,
        )
        self.create = to_raw_response_wrapper(
            deductions.create,
        )
        self.get = to_raw_response_wrapper(
            deductions.get,
        )
        self.update = to_raw_response_wrapper(
            deductions.update,
        )


class AsyncDeductionsResourceWithRawResponse:
    def __init__(self, deductions: AsyncDeductionsResource) -> None:
        self._deductions = deductions

        self.list = async_to_raw_response_wrapper(
            deductions.list,
        )
        self.create = async_to_raw_response_wrapper(
            deductions.create,
        )
        self.get = async_to_raw_response_wrapper(
            deductions.get,
        )
        self.update = async_to_raw_response_wrapper(
            deductions.update,
        )


class DeductionsResourceWithStreamingResponse:
    def __init__(self, deductions: DeductionsResource) -> None:
        self._deductions = deductions

        self.list = to_streamed_response_wrapper(
            deductions.list,
        )
        self.create = to_streamed_response_wrapper(
            deductions.create,
        )
        self.get = to_streamed_response_wrapper(
            deductions.get,
        )
        self.update = to_streamed_response_wrapper(
            deductions.update,
        )


class AsyncDeductionsResourceWithStreamingResponse:
    def __init__(self, deductions: AsyncDeductionsResource) -> None:
        self._deductions = deductions

        self.list = async_to_streamed_response_wrapper(
            deductions.list,
        )
        self.create = async_to_streamed_response_wrapper(
            deductions.create,
        )
        self.get = async_to_streamed_response_wrapper(
            deductions.get,
        )
        self.update = async_to_streamed_response_wrapper(
            deductions.update,
        )
