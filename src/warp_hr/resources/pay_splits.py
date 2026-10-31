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
from ..types.pay_split_list_response import PaySplitListResponse
from ..types.public_pay_split_status import PublicPaySplitStatus
from ..types import pay_split_list_params
from ..types.pay_split_get_response import PaySplitGetResponse

__all__ = ["PaySplitsResource", "AsyncPaySplitsResource"]


class PaySplitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaySplitsResourceWithRawResponse:
        return PaySplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaySplitsResourceWithStreamingResponse:
        return PaySplitsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        types: Optional[List[Literal["percentage", "amount"]]] | Omit = omit,
        statuses: Optional[List[PublicPaySplitStatus]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaySplitListResponse:
        """
        List stored pay-split configurations, newest first. Defaults to active. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

        Args:
            limit: Query parameter.
            after_id: The tag of the bank account pay split.
            before_id: The tag of the bank account pay split.
            worker_ids: Worker IDs as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            types: Configuration types as repeated parameters. Omit for all types.
            statuses: Statuses as repeated parameters. Defaults to active; explicitly request inactive or both to include retained configurations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaySplitListResponse: Success

        Example:
            ```python
            pay_split = client.pay_splits.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return self._get(
            "/v1/pay_splits",
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
                        "types": types,
                        "statuses": statuses,
                    },
                    pay_split_list_params.PaySplitListParams,
                ),
            ),
            cast_to=PaySplitListResponse,
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
    ) -> PaySplitGetResponse:
        """
        Get a stored pay-split configuration, including retained inactive configurations. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

        Args:
            id: The tag of the bank account pay split.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaySplitGetResponse

        Example:
            ```python
            pay_split = client.pay_splits.get(
                id="nps_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/pay_splits/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaySplitGetResponse,
        )


class AsyncPaySplitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaySplitsResourceWithRawResponse:
        return AsyncPaySplitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaySplitsResourceWithStreamingResponse:
        return AsyncPaySplitsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        types: Optional[List[Literal["percentage", "amount"]]] | Omit = omit,
        statuses: Optional[List[PublicPaySplitStatus]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaySplitListResponse:
        """
        List stored pay-split configurations, newest first. Defaults to active. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

        Args:
            limit: Query parameter.
            after_id: The tag of the bank account pay split.
            before_id: The tag of the bank account pay split.
            worker_ids: Worker IDs as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            types: Configuration types as repeated parameters. Omit for all types.
            statuses: Statuses as repeated parameters. Defaults to active; explicitly request inactive or both to include retained configurations.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaySplitListResponse: Success

        Example:
            ```python
            pay_split = await client.pay_splits.list(
                limit="limit",
                statuses=["active"],
            )
            ```
        """
        return await self._get(
            "/v1/pay_splits",
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
                        "types": types,
                        "statuses": statuses,
                    },
                    pay_split_list_params.PaySplitListParams,
                ),
            ),
            cast_to=PaySplitListResponse,
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
    ) -> PaySplitGetResponse:
        """
        Get a stored pay-split configuration, including retained inactive configurations. Requires workers banking and profile read scopes plus the applicable US or global compensation read scope.

        Args:
            id: The tag of the bank account pay split.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaySplitGetResponse

        Example:
            ```python
            pay_split = await client.pay_splits.get(
                id="nps_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/pay_splits/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaySplitGetResponse,
        )


class PaySplitsResourceWithRawResponse:
    def __init__(self, pay_splits: PaySplitsResource) -> None:
        self._pay_splits = pay_splits

        self.list = to_raw_response_wrapper(
            pay_splits.list,
        )
        self.get = to_raw_response_wrapper(
            pay_splits.get,
        )


class AsyncPaySplitsResourceWithRawResponse:
    def __init__(self, pay_splits: AsyncPaySplitsResource) -> None:
        self._pay_splits = pay_splits

        self.list = async_to_raw_response_wrapper(
            pay_splits.list,
        )
        self.get = async_to_raw_response_wrapper(
            pay_splits.get,
        )


class PaySplitsResourceWithStreamingResponse:
    def __init__(self, pay_splits: PaySplitsResource) -> None:
        self._pay_splits = pay_splits

        self.list = to_streamed_response_wrapper(
            pay_splits.list,
        )
        self.get = to_streamed_response_wrapper(
            pay_splits.get,
        )


class AsyncPaySplitsResourceWithStreamingResponse:
    def __init__(self, pay_splits: AsyncPaySplitsResource) -> None:
        self._pay_splits = pay_splits

        self.list = async_to_streamed_response_wrapper(
            pay_splits.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pay_splits.get,
        )
