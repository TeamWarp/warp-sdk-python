# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.level_list_response import LevelListResponse

__all__ = ["LevelsResource", "AsyncLevelsResource"]


class LevelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LevelsResourceWithRawResponse:
        return LevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LevelsResourceWithStreamingResponse:
        return LevelsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LevelListResponse:
        """
        List the active standard job levels available to your company.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LevelListResponse: Success

        Example:
            ```python
            level = client.levels.list()
            ```
        """
        return self._get(
            "/v1/levels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LevelListResponse,
        )


class AsyncLevelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLevelsResourceWithRawResponse:
        return AsyncLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLevelsResourceWithStreamingResponse:
        return AsyncLevelsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LevelListResponse:
        """
        List the active standard job levels available to your company.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LevelListResponse: Success

        Example:
            ```python
            level = await client.levels.list()
            ```
        """
        return await self._get(
            "/v1/levels",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LevelListResponse,
        )


class LevelsResourceWithRawResponse:
    def __init__(self, levels: LevelsResource) -> None:
        self._levels = levels

        self.list = to_raw_response_wrapper(
            levels.list,
        )


class AsyncLevelsResourceWithRawResponse:
    def __init__(self, levels: AsyncLevelsResource) -> None:
        self._levels = levels

        self.list = async_to_raw_response_wrapper(
            levels.list,
        )


class LevelsResourceWithStreamingResponse:
    def __init__(self, levels: LevelsResource) -> None:
        self._levels = levels

        self.list = to_streamed_response_wrapper(
            levels.list,
        )


class AsyncLevelsResourceWithStreamingResponse:
    def __init__(self, levels: AsyncLevelsResource) -> None:
        self._levels = levels

        self.list = async_to_streamed_response_wrapper(
            levels.list,
        )
