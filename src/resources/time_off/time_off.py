# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable
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
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ...types.time_off_list_assignments_response import TimeOffListAssignmentsResponse, Data
from ...types import time_off_list_assignments_params, time_off_list_balances_params, time_off_list_requests_params
from ...types.time_off_list_balances_response import TimeOffListBalancesResponse, Data
from ...types.time_off_list_requests_response import TimeOffListRequestsResponse, Data

__all__ = ["TimeOffResource", "AsyncTimeOffResource"]


class TimeOffResource(SyncAPIResource):

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TimeOffResourceWithRawResponse:
        return TimeOffResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeOffResourceWithStreamingResponse:
        return TimeOffResourceWithStreamingResponse(self)

    def list_assignments(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListAssignmentsResponse:
        """
        Time off assignments are mappings between workers and time off policies. Useful for finding out which policies a worker is assigned to, or which workers are assigned to a given policy.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListAssignmentsResponse: Success
        
        Example:
            ```python
            time_off = client.time_off.list_assignments()
            ```
        """
        return self._get(
            "/v1/time_off/assignments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "policy_ids": policy_ids, "worker_ids": worker_ids}, time_off_list_assignments_params.TimeOffListAssignmentsParams)),
            cast_to=TimeOffListAssignmentsResponse,
        )

    def list_balances(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        end_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListBalancesResponse:
        """
        Get worker remaining time-off balances.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            start_date: a string to be decoded into a Date
            end_date: a string to be decoded into a Date
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListBalancesResponse: Success
        
        Example:
            ```python
            time_off = client.time_off.list_balances()
            ```
        """
        return self._get(
            "/v1/time_off/balances",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "policy_ids": policy_ids, "worker_ids": worker_ids, "start_date": start_date, "end_date": end_date}, time_off_list_balances_params.TimeOffListBalancesParams)),
            cast_to=TimeOffListBalancesResponse,
        )

    def list_requests(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        statuses: Iterable[Literal["pending", "approved", "denied"]] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        starts_on_or_after: str | Omit = omit,
        starts_before: str | Omit = omit,
        ends_on_or_after: str | Omit = omit,
        ends_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListRequestsResponse:
        """
        Get the time off requests that workers in your company have made.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            statuses: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            starts_on_or_after: a string to be decoded into a Date
            starts_before: a string to be decoded into a Date
            ends_on_or_after: a string to be decoded into a Date
            ends_before: a string to be decoded into a Date
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListRequestsResponse: Success
        
        Example:
            ```python
            time_off = client.time_off.list_requests()
            ```
        """
        return self._get(
            "/v1/time_off/requests",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "statuses": statuses, "policy_ids": policy_ids, "worker_ids": worker_ids, "starts_on_or_after": starts_on_or_after, "starts_before": starts_before, "ends_on_or_after": ends_on_or_after, "ends_before": ends_before}, time_off_list_requests_params.TimeOffListRequestsParams)),
            cast_to=TimeOffListRequestsResponse,
        )


class AsyncTimeOffResource(AsyncAPIResource):

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTimeOffResourceWithRawResponse:
        return AsyncTimeOffResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeOffResourceWithStreamingResponse:
        return AsyncTimeOffResourceWithStreamingResponse(self)

    async def list_assignments(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListAssignmentsResponse:
        """
        Time off assignments are mappings between workers and time off policies. Useful for finding out which policies a worker is assigned to, or which workers are assigned to a given policy.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListAssignmentsResponse: Success
        
        Example:
            ```python
            time_off = await client.time_off.list_assignments()
            ```
        """
        return await self._get(
            "/v1/time_off/assignments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "policy_ids": policy_ids, "worker_ids": worker_ids}, time_off_list_assignments_params.TimeOffListAssignmentsParams)),
            cast_to=TimeOffListAssignmentsResponse,
        )

    async def list_balances(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        end_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListBalancesResponse:
        """
        Get worker remaining time-off balances.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            start_date: a string to be decoded into a Date
            end_date: a string to be decoded into a Date
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListBalancesResponse: Success
        
        Example:
            ```python
            time_off = await client.time_off.list_balances()
            ```
        """
        return await self._get(
            "/v1/time_off/balances",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "policy_ids": policy_ids, "worker_ids": worker_ids, "start_date": start_date, "end_date": end_date}, time_off_list_balances_params.TimeOffListBalancesParams)),
            cast_to=TimeOffListBalancesResponse,
        )

    async def list_requests(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        statuses: Iterable[Literal["pending", "approved", "denied"]] | Omit = omit,
        policy_ids: SequenceNotStr[str] | Omit = omit,
        worker_ids: SequenceNotStr[str] | Omit = omit,
        starts_on_or_after: str | Omit = omit,
        starts_before: str | Omit = omit,
        ends_on_or_after: str | Omit = omit,
        ends_before: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeOffListRequestsResponse:
        """
        Get the time off requests that workers in your company have made.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Query parameter.
            before_id: Query parameter.
            statuses: Query parameter.
            policy_ids: Query parameter.
            worker_ids: Query parameter.
            starts_on_or_after: a string to be decoded into a Date
            starts_before: a string to be decoded into a Date
            ends_on_or_after: a string to be decoded into a Date
            ends_before: a string to be decoded into a Date
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            TimeOffListRequestsResponse: Success
        
        Example:
            ```python
            time_off = await client.time_off.list_requests()
            ```
        """
        return await self._get(
            "/v1/time_off/requests",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "statuses": statuses, "policy_ids": policy_ids, "worker_ids": worker_ids, "starts_on_or_after": starts_on_or_after, "starts_before": starts_before, "ends_on_or_after": ends_on_or_after, "ends_before": ends_before}, time_off_list_requests_params.TimeOffListRequestsParams)),
            cast_to=TimeOffListRequestsResponse,
        )


class TimeOffResourceWithRawResponse:
    def __init__(self, time_off: TimeOffResource) -> None:
        self._time_off = time_off

        self.list_assignments = to_raw_response_wrapper(
            time_off.list_assignments,
        )
        self.list_balances = to_raw_response_wrapper(
            time_off.list_balances,
        )
        self.list_requests = to_raw_response_wrapper(
            time_off.list_requests,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._time_off.policies)


class AsyncTimeOffResourceWithRawResponse:
    def __init__(self, time_off: AsyncTimeOffResource) -> None:
        self._time_off = time_off

        self.list_assignments = async_to_raw_response_wrapper(
            time_off.list_assignments,
        )
        self.list_balances = async_to_raw_response_wrapper(
            time_off.list_balances,
        )
        self.list_requests = async_to_raw_response_wrapper(
            time_off.list_requests,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._time_off.policies)


class TimeOffResourceWithStreamingResponse:
    def __init__(self, time_off: TimeOffResource) -> None:
        self._time_off = time_off

        self.list_assignments = to_streamed_response_wrapper(
            time_off.list_assignments,
        )
        self.list_balances = to_streamed_response_wrapper(
            time_off.list_balances,
        )
        self.list_requests = to_streamed_response_wrapper(
            time_off.list_requests,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._time_off.policies)


class AsyncTimeOffResourceWithStreamingResponse:
    def __init__(self, time_off: AsyncTimeOffResource) -> None:
        self._time_off = time_off

        self.list_assignments = async_to_streamed_response_wrapper(
            time_off.list_assignments,
        )
        self.list_balances = async_to_streamed_response_wrapper(
            time_off.list_balances,
        )
        self.list_requests = async_to_streamed_response_wrapper(
            time_off.list_requests,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._time_off.policies)
