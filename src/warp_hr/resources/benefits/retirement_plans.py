# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

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
from ...types.benefits.retirement_plan_list_response import RetirementPlanListResponse
from ...types.benefits.public_retirement_plan_status import PublicRetirementPlanStatus
from ...types.benefits import retirement_plan_list_params, retirement_plan_create_params, retirement_plan_update_params
from ...types.benefits.public_retirement_plan_1 import PublicRetirementPlan1
from ...types.benefits.public_retirement_plan import PublicRetirementPlan

__all__ = ["RetirementPlansResource", "AsyncRetirementPlansResource"]


class RetirementPlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetirementPlansResourceWithRawResponse:
        return RetirementPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetirementPlansResourceWithStreamingResponse:
        return RetirementPlansResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[
            List[Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"]]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicRetirementPlanStatus]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetirementPlanListResponse:
        """
        List company retirement plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The tag of a company retirement plan.
            before_id: The tag of a company retirement plan.
            types: Query parameter.
            statuses: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RetirementPlanListResponse: Success

        Example:
            ```python
            retirement_plan = client.benefits.retirement_plans.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return self._get(
            "/v1/benefits/retirement_plans",
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
                    },
                    retirement_plan_list_params.RetirementPlanListParams,
                ),
            ),
            cast_to=RetirementPlanListResponse,
        )

    def create(
        self,
        *,
        type: Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"],
        name: str,
        effective_start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicRetirementPlan1:
        """
        Create a retirement plan for a company on the manual retirement channel.

        Args:
            type: Body parameter.
            name: Body parameter.
            effective_start_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan1

        Example:
            ```python
            retirement_plan = client.benefits.retirement_plans.create(
                type="401k",
                name="x",
                effective_start_date="",
            )
            ```
        """
        return self._post(
            "/v1/benefits/retirement_plans",
            body=maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "effective_start_date": effective_start_date,
                },
                retirement_plan_create_params.RetirementPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan1,
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
    ) -> PublicRetirementPlan:
        """
        Get a company retirement plan by id, regardless of status.

        Args:
            id: The tag of a company retirement plan.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan

        Example:
            ```python
            retirement_plan = client.benefits.retirement_plans.get(
                id="crpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/benefits/retirement_plans/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan,
        )

    def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        effective_start_date: Optional[str] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicRetirementPlan:
        """
        Update a retirement plan for a company on the manual retirement channel.

        Args:
            id: The tag of a company retirement plan.
            name: Body parameter.
            effective_start_date: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan

        Example:
            ```python
            retirement_plan = client.benefits.retirement_plans.update(
                id="crpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/benefits/retirement_plans/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "effective_start_date": effective_start_date,
                    "effective_end_date": effective_end_date,
                },
                retirement_plan_update_params.RetirementPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan,
        )


class AsyncRetirementPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetirementPlansResourceWithRawResponse:
        return AsyncRetirementPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetirementPlansResourceWithStreamingResponse:
        return AsyncRetirementPlansResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[
            List[Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"]]
        ]
        | Omit = omit,
        statuses: Optional[List[PublicRetirementPlanStatus]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetirementPlanListResponse:
        """
        List company retirement plans. Defaults to active plans. A plan whose effectiveEndDate has elapsed is reported and filtered as terminated.

        Args:
            limit: Query parameter.
            after_id: The tag of a company retirement plan.
            before_id: The tag of a company retirement plan.
            types: Query parameter.
            statuses: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RetirementPlanListResponse: Success

        Example:
            ```python
            retirement_plan = await client.benefits.retirement_plans.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return await self._get(
            "/v1/benefits/retirement_plans",
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
                    },
                    retirement_plan_list_params.RetirementPlanListParams,
                ),
            ),
            cast_to=RetirementPlanListResponse,
        )

    async def create(
        self,
        *,
        type: Literal["401k", "roth_401k", "403b", "roth_403b", "457", "roth_457", "simple_ira", "roth_simple_ira"],
        name: str,
        effective_start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicRetirementPlan1:
        """
        Create a retirement plan for a company on the manual retirement channel.

        Args:
            type: Body parameter.
            name: Body parameter.
            effective_start_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan1

        Example:
            ```python
            retirement_plan = await client.benefits.retirement_plans.create(
                type="401k",
                name="x",
                effective_start_date="",
            )
            ```
        """
        return await self._post(
            "/v1/benefits/retirement_plans",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "effective_start_date": effective_start_date,
                },
                retirement_plan_create_params.RetirementPlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan1,
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
    ) -> PublicRetirementPlan:
        """
        Get a company retirement plan by id, regardless of status.

        Args:
            id: The tag of a company retirement plan.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan

        Example:
            ```python
            retirement_plan = await client.benefits.retirement_plans.get(
                id="crpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/benefits/retirement_plans/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan,
        )

    async def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        effective_start_date: Optional[str] | Omit = omit,
        effective_end_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicRetirementPlan:
        """
        Update a retirement plan for a company on the manual retirement channel.

        Args:
            id: The tag of a company retirement plan.
            name: Body parameter.
            effective_start_date: Body parameter.
            effective_end_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicRetirementPlan

        Example:
            ```python
            retirement_plan = await client.benefits.retirement_plans.update(
                id="crpl_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/benefits/retirement_plans/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "effective_start_date": effective_start_date,
                    "effective_end_date": effective_end_date,
                },
                retirement_plan_update_params.RetirementPlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicRetirementPlan,
        )


class RetirementPlansResourceWithRawResponse:
    def __init__(self, retirement_plans: RetirementPlansResource) -> None:
        self._retirement_plans = retirement_plans

        self.list = to_raw_response_wrapper(
            retirement_plans.list,
        )
        self.create = to_raw_response_wrapper(
            retirement_plans.create,
        )
        self.get = to_raw_response_wrapper(
            retirement_plans.get,
        )
        self.update = to_raw_response_wrapper(
            retirement_plans.update,
        )


class AsyncRetirementPlansResourceWithRawResponse:
    def __init__(self, retirement_plans: AsyncRetirementPlansResource) -> None:
        self._retirement_plans = retirement_plans

        self.list = async_to_raw_response_wrapper(
            retirement_plans.list,
        )
        self.create = async_to_raw_response_wrapper(
            retirement_plans.create,
        )
        self.get = async_to_raw_response_wrapper(
            retirement_plans.get,
        )
        self.update = async_to_raw_response_wrapper(
            retirement_plans.update,
        )


class RetirementPlansResourceWithStreamingResponse:
    def __init__(self, retirement_plans: RetirementPlansResource) -> None:
        self._retirement_plans = retirement_plans

        self.list = to_streamed_response_wrapper(
            retirement_plans.list,
        )
        self.create = to_streamed_response_wrapper(
            retirement_plans.create,
        )
        self.get = to_streamed_response_wrapper(
            retirement_plans.get,
        )
        self.update = to_streamed_response_wrapper(
            retirement_plans.update,
        )


class AsyncRetirementPlansResourceWithStreamingResponse:
    def __init__(self, retirement_plans: AsyncRetirementPlansResource) -> None:
        self._retirement_plans = retirement_plans

        self.list = async_to_streamed_response_wrapper(
            retirement_plans.list,
        )
        self.create = async_to_streamed_response_wrapper(
            retirement_plans.create,
        )
        self.get = async_to_streamed_response_wrapper(
            retirement_plans.get,
        )
        self.update = async_to_streamed_response_wrapper(
            retirement_plans.update,
        )
