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
from ...types.benefits.health_plan_list_response import HealthPlanListResponse
from ...types.benefits.public_health_plan_status import PublicHealthPlanStatus
from ...types.benefits import health_plan_list_params
from ...types.benefits.public_health_plan import PublicHealthPlan

__all__ = ["HealthPlansResource", "AsyncHealthPlansResource"]


class HealthPlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthPlansResourceWithRawResponse:
        return HealthPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthPlansResourceWithStreamingResponse:
        return HealthPlansResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[
            List[
                Literal[
                    "medical",
                    "dental",
                    "vision",
                    "life",
                    "short_term_disability",
                    "long_term_disability",
                    "accident",
                    "critical_illness",
                    "hospital",
                ]
            ]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicHealthPlanStatus]],
        carrier_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthPlanListResponse:
        """
        List company health plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The tag of a company health plan.
            before_id: The tag of a company health plan.
            types: Query parameter.
            statuses: Query parameter.
            carrier_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            HealthPlanListResponse: Success

        Example:
            ```python
            health_plan = client.benefits.health_plans.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return self._get(
            "/v1/benefits/health_plans",
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
                        "types": types,
                        "statuses": statuses,
                        "carrier_ids": carrier_ids,
                    },
                    health_plan_list_params.HealthPlanListParams,
                ),
            ),
            cast_to=HealthPlanListResponse,
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
    ) -> PublicHealthPlan:
        """
        Get a publicly visible company health plan by id.

        Args:
            id: The tag of a company health plan.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicHealthPlan

        Example:
            ```python
            health_plan = client.benefits.health_plans.get(
                id="chpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/benefits/health_plans/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicHealthPlan,
        )


class AsyncHealthPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthPlansResourceWithRawResponse:
        return AsyncHealthPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthPlansResourceWithStreamingResponse:
        return AsyncHealthPlansResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[
            List[
                Literal[
                    "medical",
                    "dental",
                    "vision",
                    "life",
                    "short_term_disability",
                    "long_term_disability",
                    "accident",
                    "critical_illness",
                    "hospital",
                ]
            ]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicHealthPlanStatus]],
        carrier_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthPlanListResponse:
        """
        List company health plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The tag of a company health plan.
            before_id: The tag of a company health plan.
            types: Query parameter.
            statuses: Query parameter.
            carrier_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            HealthPlanListResponse: Success

        Example:
            ```python
            health_plan = await client.benefits.health_plans.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return await self._get(
            "/v1/benefits/health_plans",
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
                        "types": types,
                        "statuses": statuses,
                        "carrier_ids": carrier_ids,
                    },
                    health_plan_list_params.HealthPlanListParams,
                ),
            ),
            cast_to=HealthPlanListResponse,
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
    ) -> PublicHealthPlan:
        """
        Get a publicly visible company health plan by id.

        Args:
            id: The tag of a company health plan.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicHealthPlan

        Example:
            ```python
            health_plan = await client.benefits.health_plans.get(
                id="chpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/benefits/health_plans/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicHealthPlan,
        )


class HealthPlansResourceWithRawResponse:
    def __init__(self, health_plans: HealthPlansResource) -> None:
        self._health_plans = health_plans

        self.list = to_raw_response_wrapper(
            health_plans.list,
        )
        self.get = to_raw_response_wrapper(
            health_plans.get,
        )


class AsyncHealthPlansResourceWithRawResponse:
    def __init__(self, health_plans: AsyncHealthPlansResource) -> None:
        self._health_plans = health_plans

        self.list = async_to_raw_response_wrapper(
            health_plans.list,
        )
        self.get = async_to_raw_response_wrapper(
            health_plans.get,
        )


class HealthPlansResourceWithStreamingResponse:
    def __init__(self, health_plans: HealthPlansResource) -> None:
        self._health_plans = health_plans

        self.list = to_streamed_response_wrapper(
            health_plans.list,
        )
        self.get = to_streamed_response_wrapper(
            health_plans.get,
        )


class AsyncHealthPlansResourceWithStreamingResponse:
    def __init__(self, health_plans: AsyncHealthPlansResource) -> None:
        self._health_plans = health_plans

        self.list = async_to_streamed_response_wrapper(
            health_plans.list,
        )
        self.get = async_to_streamed_response_wrapper(
            health_plans.get,
        )
