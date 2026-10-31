# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.pay_rates.public_create_regular_pay_rate_response import PublicCreateRegularPayRateResponse
from ...types.pay_rates import regular_create_params, regular_delete_params

__all__ = ["RegularResource", "AsyncRegularResource"]


class RegularResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegularResourceWithRawResponse:
        return RegularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegularResourceWithStreamingResponse:
        return RegularResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        worker_id: str,
        type: Literal["salary", "monthly", "weekly", "hourly", "variable"],
        amount: Optional[int] | Omit = omit,
        currency: Literal[
            "USD",
            "AUD",
            "BGN",
            "BRL",
            "CAD",
            "CHF",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HUF",
            "IDR",
            "INR",
            "MYR",
            "NOK",
            "NZD",
            "CNY",
            "PLN",
            "RON",
            "TRY",
            "SEK",
            "SGD",
            "AED",
            "ARS",
            "BDT",
            "BWP",
            "COP",
            "CRC",
            "EGP",
            "FJD",
            "GEL",
            "GHS",
            "ILS",
            "KES",
            "LKR",
            "MAD",
            "MXN",
            "NPR",
            "PHP",
            "PKR",
            "THB",
            "UAH",
            "UYU",
            "ZAR",
            "ZMW",
            "NGN",
            "RSD",
            "TWD",
            "GTQ",
            "HNL",
            "DOP",
            "SAR",
            "PEN",
        ],
        effective_date: str,
        require_hours_submission: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCreateRegularPayRateResponse:
        """
        Create an effective-dated regular pay rate for a worker. The API key must have the compensation write scope corresponding to the worker classification. Fixed rates require a nonnegative integer amount in minor currency units, and writes accept only currencies with exactly two ISO 4217 minor-unit digits. Amount is required except for variable pay, and requireHoursSubmission is required for hourly pay. An inactive worker’s rate must start on the worker start date; an active worker’s rate must start on or after that date. An existing future rate blocks creation except for a same-start-date replacement. Currency changes must begin at the current pay-period start, or at the worker start date when the worker is inactive, is a pay-as-you-go contractor, or has a future start date. Variable pay returns a null id and stores no fixed pay-rate row. Replacing a fixed row on the same date emits separate deleted and created webhooks; delivery order is not guaranteed. Creating a fixed rate over variable pay emits only the created webhook because no fixed row existed to delete. There is no pay-rate update event.

        Args:
            worker_id: The worker whose regular pay rate will be created.
            type: How the regular pay rate is measured. Salary represents an annual rate. Variable pay creates a dated boundary without a fixed pay-rate row and returns a null id.
            amount: minor units — cents, e.g. 2345 for $23.45
            currency: The two-decimal ISO 4217 payout currency of the pay rate.
            effective_date: Body parameter.
            require_hours_submission: Whether the worker must submit hours. Required when type is hourly.
            description: A human-readable label for the pay rate.
            notes: Optional internal notes about the pay rate change.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicCreateRegularPayRateResponse: PublicCreateRegularPayRateResponse

        Example:
            ```python
            regular = client.pay_rates.regular.create(
                worker_id="wrk_khac8380c2Lm",
                type="salary",
                currency="USD",
                effective_date="",
            )
            ```
        """
        return self._post(
            "/v1/pay_rates/regular",
            body=maybe_transform(
                {
                    "worker_id": worker_id,
                    "type": type,
                    "amount": amount,
                    "currency": currency,
                    "effective_date": effective_date,
                    "require_hours_submission": require_hours_submission,
                    "description": description,
                    "notes": notes,
                },
                regular_create_params.RegularCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCreateRegularPayRateResponse,
        )

    def delete(
        self,
        *,
        worker_id: str,
        effective_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a regular pay rate or variable-pay boundary identified by worker and effective date. The effective date must be strictly after the current UTC date. The API key must have the compensation write scope corresponding to the worker classification. Deletion reopens the predecessor through the deleted range, including when deleting a variable-pay boundary. There is no public PATCH or PUT pay-rate update operation; replace a same-date rate by creating its replacement.

        Args:
            worker_id: The worker whose future regular pay rate will be deleted.
            effective_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            client.pay_rates.regular.delete(
                worker_id="wrk_khac8380c2Lm",
                effective_date="",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v1/pay_rates/regular",
            body=maybe_transform(
                {
                    "worker_id": worker_id,
                    "effective_date": effective_date,
                },
                regular_delete_params.RegularDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRegularResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegularResourceWithRawResponse:
        return AsyncRegularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegularResourceWithStreamingResponse:
        return AsyncRegularResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        worker_id: str,
        type: Literal["salary", "monthly", "weekly", "hourly", "variable"],
        amount: Optional[int] | Omit = omit,
        currency: Literal[
            "USD",
            "AUD",
            "BGN",
            "BRL",
            "CAD",
            "CHF",
            "CZK",
            "DKK",
            "EUR",
            "GBP",
            "HKD",
            "HUF",
            "IDR",
            "INR",
            "MYR",
            "NOK",
            "NZD",
            "CNY",
            "PLN",
            "RON",
            "TRY",
            "SEK",
            "SGD",
            "AED",
            "ARS",
            "BDT",
            "BWP",
            "COP",
            "CRC",
            "EGP",
            "FJD",
            "GEL",
            "GHS",
            "ILS",
            "KES",
            "LKR",
            "MAD",
            "MXN",
            "NPR",
            "PHP",
            "PKR",
            "THB",
            "UAH",
            "UYU",
            "ZAR",
            "ZMW",
            "NGN",
            "RSD",
            "TWD",
            "GTQ",
            "HNL",
            "DOP",
            "SAR",
            "PEN",
        ],
        effective_date: str,
        require_hours_submission: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicCreateRegularPayRateResponse:
        """
        Create an effective-dated regular pay rate for a worker. The API key must have the compensation write scope corresponding to the worker classification. Fixed rates require a nonnegative integer amount in minor currency units, and writes accept only currencies with exactly two ISO 4217 minor-unit digits. Amount is required except for variable pay, and requireHoursSubmission is required for hourly pay. An inactive worker’s rate must start on the worker start date; an active worker’s rate must start on or after that date. An existing future rate blocks creation except for a same-start-date replacement. Currency changes must begin at the current pay-period start, or at the worker start date when the worker is inactive, is a pay-as-you-go contractor, or has a future start date. Variable pay returns a null id and stores no fixed pay-rate row. Replacing a fixed row on the same date emits separate deleted and created webhooks; delivery order is not guaranteed. Creating a fixed rate over variable pay emits only the created webhook because no fixed row existed to delete. There is no pay-rate update event.

        Args:
            worker_id: The worker whose regular pay rate will be created.
            type: How the regular pay rate is measured. Salary represents an annual rate. Variable pay creates a dated boundary without a fixed pay-rate row and returns a null id.
            amount: minor units — cents, e.g. 2345 for $23.45
            currency: The two-decimal ISO 4217 payout currency of the pay rate.
            effective_date: Body parameter.
            require_hours_submission: Whether the worker must submit hours. Required when type is hourly.
            description: A human-readable label for the pay rate.
            notes: Optional internal notes about the pay rate change.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicCreateRegularPayRateResponse: PublicCreateRegularPayRateResponse

        Example:
            ```python
            regular = await client.pay_rates.regular.create(
                worker_id="wrk_khac8380c2Lm",
                type="salary",
                currency="USD",
                effective_date="",
            )
            ```
        """
        return await self._post(
            "/v1/pay_rates/regular",
            body=await async_maybe_transform(
                {
                    "worker_id": worker_id,
                    "type": type,
                    "amount": amount,
                    "currency": currency,
                    "effective_date": effective_date,
                    "require_hours_submission": require_hours_submission,
                    "description": description,
                    "notes": notes,
                },
                regular_create_params.RegularCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicCreateRegularPayRateResponse,
        )

    async def delete(
        self,
        *,
        worker_id: str,
        effective_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a regular pay rate or variable-pay boundary identified by worker and effective date. The effective date must be strictly after the current UTC date. The API key must have the compensation write scope corresponding to the worker classification. Deletion reopens the predecessor through the deleted range, including when deleting a variable-pay boundary. There is no public PATCH or PUT pay-rate update operation; replace a same-date rate by creating its replacement.

        Args:
            worker_id: The worker whose future regular pay rate will be deleted.
            effective_date: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            await client.pay_rates.regular.delete(
                worker_id="wrk_khac8380c2Lm",
                effective_date="",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v1/pay_rates/regular",
            body=await async_maybe_transform(
                {
                    "worker_id": worker_id,
                    "effective_date": effective_date,
                },
                regular_delete_params.RegularDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RegularResourceWithRawResponse:
    def __init__(self, regular: RegularResource) -> None:
        self._regular = regular

        self.create = to_raw_response_wrapper(
            regular.create,
        )
        self.delete = to_raw_response_wrapper(
            regular.delete,
        )


class AsyncRegularResourceWithRawResponse:
    def __init__(self, regular: AsyncRegularResource) -> None:
        self._regular = regular

        self.create = async_to_raw_response_wrapper(
            regular.create,
        )
        self.delete = async_to_raw_response_wrapper(
            regular.delete,
        )


class RegularResourceWithStreamingResponse:
    def __init__(self, regular: RegularResource) -> None:
        self._regular = regular

        self.create = to_streamed_response_wrapper(
            regular.create,
        )
        self.delete = to_streamed_response_wrapper(
            regular.delete,
        )


class AsyncRegularResourceWithStreamingResponse:
    def __init__(self, regular: AsyncRegularResource) -> None:
        self._regular = regular

        self.create = async_to_streamed_response_wrapper(
            regular.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            regular.delete,
        )
