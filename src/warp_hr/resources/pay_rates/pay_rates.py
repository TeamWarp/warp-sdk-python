# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional

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
from .regular import (
    RegularResource,
    AsyncRegularResource,
    RegularResourceWithRawResponse,
    AsyncRegularResourceWithRawResponse,
    RegularResourceWithStreamingResponse,
    AsyncRegularResourceWithStreamingResponse,
)
from ...types.pay_rate_list_response import PayRateListResponse
from ...types.public_pay_rate_type import PublicPayRateType
from ...types import pay_rate_list_params
from ...types.public_pay_rate import PublicPayRate

__all__ = ["PayRatesResource", "AsyncPayRatesResource"]


class PayRatesResource(SyncAPIResource):
    @cached_property
    def regular(self) -> RegularResource:
        return RegularResource(self._client)

    @cached_property
    def with_raw_response(self) -> PayRatesResourceWithRawResponse:
        return PayRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayRatesResourceWithStreamingResponse:
        return PayRatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_id: Optional[str] | Omit = omit,
        effective_on_or_after: Optional[str] | Omit = omit,
        effective_before: Optional[str] | Omit = omit,
        type: Optional[PublicPayRateType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayRateListResponse:
        """
        List pay rates visible to the API key. Results may be filtered by worker, effective start date, or regular/additional type. US and global worker rates require their corresponding compensation read scopes.

        Args:
            limit: Query parameter.
            after_id: The tag of the pay rate.
            before_id: The tag of the pay rate.
            worker_id: Only return pay rates assigned to this worker.
            effective_on_or_after: Only return pay rates whose effective start date is on or after this date.
            effective_before: Only return pay rates whose effective start date is before this date.
            type: Only return regular or additional pay rates of this type.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PayRateListResponse: Success

        Example:
            ```python
            pay_rate = client.pay_rates.list(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/pay_rates",
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
                        "worker_id": worker_id,
                        "effective_on_or_after": effective_on_or_after,
                        "effective_before": effective_before,
                        "type": type,
                    },
                    pay_rate_list_params.PayRateListParams,
                ),
            ),
            cast_to=PayRateListResponse,
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
    ) -> PublicPayRate:
        """
        Get a specific pay rate by id. The API key must have the compensation read scope corresponding to the worker.

        Args:
            id: The tag of the pay rate.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayRate

        Example:
            ```python
            pay_rate = client.pay_rates.get(
                id="pyr_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/pay_rates/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPayRate,
        )


class AsyncPayRatesResource(AsyncAPIResource):
    @cached_property
    def regular(self) -> AsyncRegularResource:
        return AsyncRegularResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPayRatesResourceWithRawResponse:
        return AsyncPayRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayRatesResourceWithStreamingResponse:
        return AsyncPayRatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_id: Optional[str] | Omit = omit,
        effective_on_or_after: Optional[str] | Omit = omit,
        effective_before: Optional[str] | Omit = omit,
        type: Optional[PublicPayRateType] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayRateListResponse:
        """
        List pay rates visible to the API key. Results may be filtered by worker, effective start date, or regular/additional type. US and global worker rates require their corresponding compensation read scopes.

        Args:
            limit: Query parameter.
            after_id: The tag of the pay rate.
            before_id: The tag of the pay rate.
            worker_id: Only return pay rates assigned to this worker.
            effective_on_or_after: Only return pay rates whose effective start date is on or after this date.
            effective_before: Only return pay rates whose effective start date is before this date.
            type: Only return regular or additional pay rates of this type.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PayRateListResponse: Success

        Example:
            ```python
            pay_rate = await client.pay_rates.list(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/pay_rates",
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
                        "worker_id": worker_id,
                        "effective_on_or_after": effective_on_or_after,
                        "effective_before": effective_before,
                        "type": type,
                    },
                    pay_rate_list_params.PayRateListParams,
                ),
            ),
            cast_to=PayRateListResponse,
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
    ) -> PublicPayRate:
        """
        Get a specific pay rate by id. The API key must have the compensation read scope corresponding to the worker.

        Args:
            id: The tag of the pay rate.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayRate

        Example:
            ```python
            pay_rate = await client.pay_rates.get(
                id="pyr_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/pay_rates/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPayRate,
        )


class PayRatesResourceWithRawResponse:
    def __init__(self, pay_rates: PayRatesResource) -> None:
        self._pay_rates = pay_rates

        self.list = to_raw_response_wrapper(
            pay_rates.list,
        )
        self.get = to_raw_response_wrapper(
            pay_rates.get,
        )

    @cached_property
    def regular(self) -> RegularResourceWithRawResponse:
        return RegularResourceWithRawResponse(self._pay_rates.regular)


class AsyncPayRatesResourceWithRawResponse:
    def __init__(self, pay_rates: AsyncPayRatesResource) -> None:
        self._pay_rates = pay_rates

        self.list = async_to_raw_response_wrapper(
            pay_rates.list,
        )
        self.get = async_to_raw_response_wrapper(
            pay_rates.get,
        )

    @cached_property
    def regular(self) -> AsyncRegularResourceWithRawResponse:
        return AsyncRegularResourceWithRawResponse(self._pay_rates.regular)


class PayRatesResourceWithStreamingResponse:
    def __init__(self, pay_rates: PayRatesResource) -> None:
        self._pay_rates = pay_rates

        self.list = to_streamed_response_wrapper(
            pay_rates.list,
        )
        self.get = to_streamed_response_wrapper(
            pay_rates.get,
        )

    @cached_property
    def regular(self) -> RegularResourceWithStreamingResponse:
        return RegularResourceWithStreamingResponse(self._pay_rates.regular)


class AsyncPayRatesResourceWithStreamingResponse:
    def __init__(self, pay_rates: AsyncPayRatesResource) -> None:
        self._pay_rates = pay_rates

        self.list = async_to_streamed_response_wrapper(
            pay_rates.list,
        )
        self.get = async_to_streamed_response_wrapper(
            pay_rates.get,
        )

    @cached_property
    def regular(self) -> AsyncRegularResourceWithStreamingResponse:
        return AsyncRegularResourceWithStreamingResponse(self._pay_rates.regular)
