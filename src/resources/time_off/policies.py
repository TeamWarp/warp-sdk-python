# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.time_off.policy_list_response import PolicyListResponse, Data
from ...types.time_off import policy_list_params
from ...types.time_off.policy_retrieve_response import PolicyRetrieveResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListResponse:
        """
        Get the time off policies for your company
        
        Args:
            limit: a number less than or equal to 100
            after_id: a string starting with "top_"
            before_id: a string starting with "top_"
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PolicyListResponse: Success
        
        Example:
            ```python
            policy = client.time_off.policies.list()
            ```
        """
        return self._get(
            "/v1/time_off/policies",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, policy_list_params.PolicyListParams)),
            cast_to=PolicyListResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRetrieveResponse:
        """
        Get a specific time off policy by id
        
        Args:
            id: a string starting with "top_"
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PolicyRetrieveResponse: Success
        
        Example:
            ```python
            policy = client.time_off.policies.retrieve(
                id="top_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/time_off/policies/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PolicyRetrieveResponse,
        )


class AsyncPoliciesResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListResponse:
        """
        Get the time off policies for your company
        
        Args:
            limit: a number less than or equal to 100
            after_id: a string starting with "top_"
            before_id: a string starting with "top_"
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PolicyListResponse: Success
        
        Example:
            ```python
            policy = await client.time_off.policies.list()
            ```
        """
        return await self._get(
            "/v1/time_off/policies",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, policy_list_params.PolicyListParams)),
            cast_to=PolicyListResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyRetrieveResponse:
        """
        Get a specific time off policy by id
        
        Args:
            id: a string starting with "top_"
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            PolicyRetrieveResponse: Success
        
        Example:
            ```python
            policy = await client.time_off.policies.retrieve(
                id="top_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/time_off/policies/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PolicyRetrieveResponse,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.retrieve = to_raw_response_wrapper(
            policies.retrieve,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            policies.retrieve,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            policies.retrieve,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            policies.retrieve,
        )
