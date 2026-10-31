# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.i9_verification_list_response import I9VerificationListResponse
from ..types import i9_verification_list_params
from ..types.public_i9_verification import PublicI9Verification

__all__ = ["I9VerificationsResource", "AsyncI9VerificationsResource"]


class I9VerificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> I9VerificationsResourceWithRawResponse:
        return I9VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> I9VerificationsResourceWithStreamingResponse:
        return I9VerificationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[Literal["not_started", "awaiting_worker", "awaiting_admin", "verified"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> I9VerificationListResponse:
        """
        List current and retained company I-9 verifications in all workflow states, newest first. The API key must have workers profile and compliance read scope.

        Args:
            limit: Query parameter.
            after_id: The tag of the i9 verification.
            before_id: The tag of the i9 verification.
            worker_ids: Worker IDs to include, supplied as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            statuses: Statuses to include, supplied as repeated parameters. Omit for all workflow states.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            I9VerificationListResponse: Success

        Example:
            ```python
            i9_verification = client.i9_verifications.list(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/i9_verifications",
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
                        "statuses": statuses,
                    },
                    i9_verification_list_params.I9VerificationListParams,
                ),
            ),
            cast_to=I9VerificationListResponse,
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
    ) -> PublicI9Verification:
        """
        Get a specific I-9 verification by its id. The API key must have workers profile and compliance read scope.

        Args:
            id: The tag of the i9 verification.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicI9Verification

        Example:
            ```python
            i9_verification = client.i9_verifications.get(
                id="i9v_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/i9_verifications/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicI9Verification,
        )


class AsyncI9VerificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncI9VerificationsResourceWithRawResponse:
        return AsyncI9VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncI9VerificationsResourceWithStreamingResponse:
        return AsyncI9VerificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[Literal["not_started", "awaiting_worker", "awaiting_admin", "verified"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> I9VerificationListResponse:
        """
        List current and retained company I-9 verifications in all workflow states, newest first. The API key must have workers profile and compliance read scope.

        Args:
            limit: Query parameter.
            after_id: The tag of the i9 verification.
            before_id: The tag of the i9 verification.
            worker_ids: Worker IDs to include, supplied as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            statuses: Statuses to include, supplied as repeated parameters. Omit for all workflow states.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            I9VerificationListResponse: Success

        Example:
            ```python
            i9_verification = await client.i9_verifications.list(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/i9_verifications",
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
                        "statuses": statuses,
                    },
                    i9_verification_list_params.I9VerificationListParams,
                ),
            ),
            cast_to=I9VerificationListResponse,
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
    ) -> PublicI9Verification:
        """
        Get a specific I-9 verification by its id. The API key must have workers profile and compliance read scope.

        Args:
            id: The tag of the i9 verification.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicI9Verification

        Example:
            ```python
            i9_verification = await client.i9_verifications.get(
                id="i9v_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/i9_verifications/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicI9Verification,
        )


class I9VerificationsResourceWithRawResponse:
    def __init__(self, i9_verifications: I9VerificationsResource) -> None:
        self._i9_verifications = i9_verifications

        self.list = to_raw_response_wrapper(
            i9_verifications.list,
        )
        self.get = to_raw_response_wrapper(
            i9_verifications.get,
        )


class AsyncI9VerificationsResourceWithRawResponse:
    def __init__(self, i9_verifications: AsyncI9VerificationsResource) -> None:
        self._i9_verifications = i9_verifications

        self.list = async_to_raw_response_wrapper(
            i9_verifications.list,
        )
        self.get = async_to_raw_response_wrapper(
            i9_verifications.get,
        )


class I9VerificationsResourceWithStreamingResponse:
    def __init__(self, i9_verifications: I9VerificationsResource) -> None:
        self._i9_verifications = i9_verifications

        self.list = to_streamed_response_wrapper(
            i9_verifications.list,
        )
        self.get = to_streamed_response_wrapper(
            i9_verifications.get,
        )


class AsyncI9VerificationsResourceWithStreamingResponse:
    def __init__(self, i9_verifications: AsyncI9VerificationsResource) -> None:
        self._i9_verifications = i9_verifications

        self.list = async_to_streamed_response_wrapper(
            i9_verifications.list,
        )
        self.get = async_to_streamed_response_wrapper(
            i9_verifications.get,
        )
