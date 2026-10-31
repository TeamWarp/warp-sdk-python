# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional
from typing_extensions import Literal

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
from ..types.offer_list_response import OfferListResponse
from ..types import offer_list_params, offer_create_params, offer_void_params, offer_extend_deadline_params
from ..types.offer_create_response import OfferCreateResponse
from ..types.offer_void_response import OfferVoidResponse
from ..types.offer_extend_deadline_response import OfferExtendDeadlineResponse
from ..types.offer_resend_response import OfferResendResponse

__all__ = ["OffersResource", "AsyncOffersResource"]


class OffersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffersResourceWithRawResponse:
        return OffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffersResourceWithStreamingResponse:
        return OffersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        statuses: Optional[List[Literal["draft", "sent", "accepted", "void", "expired"]]] | Omit = omit,
        worker_types: Optional[List[Literal["employee", "us_contractor", "global_contractor"]]] | Omit = omit,
        candidate_email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferListResponse:
        """
        List the candidate offers for your company.

        Args:
            limit: Query parameter.
            after_id: The tag of the offer.
            before_id: The tag of the offer.
            statuses: Query parameter.
            worker_types: Query parameter.
            candidate_email: An email with a reasonably valid regex (based on RFC 5321 atext characters)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferListResponse: Success

        Example:
            ```python
            offer = client.offers.list(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/offers",
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
                        "statuses": statuses,
                        "worker_types": worker_types,
                        "candidate_email": candidate_email,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            cast_to=OfferListResponse,
        )

    def create(
        self,
        *,
        candidate: offer_create_params.Candidate,
        position: offer_create_params.Position,
        department_id: Optional[str] | Omit = omit,
        workplace_id: Optional[str] | Omit = omit,
        manager_id: Optional[str] | Omit = omit,
        level_id: Optional[str] | Omit = omit,
        worker_type: Literal["employee", "us_contractor", "global_contractor"],
        compensation: offer_create_params.Compensation,
        expiration_time: Optional[str] | Omit = omit,
        background_check_work_location: Optional[offer_create_params.BackgroundCheckWorkLocation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferCreateResponse:
        """
        Create and send a candidate offer. The candidate receives an email with a link to the offer portal.

        Args:
            candidate: Body parameter.
            position: Body parameter.
            department_id: The unique public id of the department
            workplace_id: Public workplace identifier
            manager_id: The id of the worker.
            level_id: The unique public id of the job level
            worker_type: Body parameter.
            compensation: Body parameter.
            expiration_time: Body parameter.
            background_check_work_location: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferCreateResponse: Success

        Example:
            ```python
            offer = client.offers.create(
                candidate={"first_name": "x", "last_name": "x", "email": "john@joinwarp.com"},
                position={"title": "x", "start_date": ""},
                worker_type="employee",
                compensation={"pay_basis": "year", "pay_currency": "USD", "pay_rate": 1},
            )
            ```
        """
        return self._post(
            "/v1/offers",
            body=maybe_transform(
                {
                    "candidate": candidate,
                    "position": position,
                    "department_id": department_id,
                    "workplace_id": workplace_id,
                    "manager_id": manager_id,
                    "level_id": level_id,
                    "worker_type": worker_type,
                    "compensation": compensation,
                    "expiration_time": expiration_time,
                    "background_check_work_location": background_check_work_location,
                },
                offer_create_params.OfferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferCreateResponse,
        )

    def void(
        self,
        id: str,
        *,
        void_reason: Literal["candidate_declined", "other"],
        void_notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferVoidResponse:
        """
        Void a previously sent offer. Only sent offers can be voided.

        Args:
            id: The tag of the offer.
            void_reason: Body parameter.
            void_notes: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferVoidResponse: Success

        Example:
            ```python
            offer = client.offers.void(
                id="offr_1234",
                void_reason="candidate_declined",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/offers/{id}/void", **{"id": id}),
            body=maybe_transform(
                {
                    "void_reason": void_reason,
                    "void_notes": void_notes,
                },
                offer_void_params.OfferVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferVoidResponse,
        )

    def extend_deadline(
        self,
        id: str,
        *,
        expiration_time: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferExtendDeadlineResponse:
        """
        Extend the expiration deadline of a sent offer.

        Args:
            id: The tag of the offer.
            expiration_time: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferExtendDeadlineResponse: Success

        Example:
            ```python
            offer = client.offers.extend_deadline(
                id="offr_1234",
                expiration_time="",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/offers/{id}/extend-deadline", **{"id": id}),
            body=maybe_transform(
                {"expiration_time": expiration_time},
                offer_extend_deadline_params.OfferExtendDeadlineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferExtendDeadlineResponse,
        )

    def resend(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferResendResponse:
        """
        Resend the offer email to the candidate for a sent offer.

        Args:
            id: The tag of the offer.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferResendResponse: Success

        Example:
            ```python
            offer = client.offers.resend(
                id="offr_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/offers/{id}/resend", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferResendResponse,
        )


class AsyncOffersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffersResourceWithRawResponse:
        return AsyncOffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffersResourceWithStreamingResponse:
        return AsyncOffersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        statuses: Optional[List[Literal["draft", "sent", "accepted", "void", "expired"]]] | Omit = omit,
        worker_types: Optional[List[Literal["employee", "us_contractor", "global_contractor"]]] | Omit = omit,
        candidate_email: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferListResponse:
        """
        List the candidate offers for your company.

        Args:
            limit: Query parameter.
            after_id: The tag of the offer.
            before_id: The tag of the offer.
            statuses: Query parameter.
            worker_types: Query parameter.
            candidate_email: An email with a reasonably valid regex (based on RFC 5321 atext characters)
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferListResponse: Success

        Example:
            ```python
            offer = await client.offers.list(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/offers",
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
                        "statuses": statuses,
                        "worker_types": worker_types,
                        "candidate_email": candidate_email,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            cast_to=OfferListResponse,
        )

    async def create(
        self,
        *,
        candidate: offer_create_params.Candidate,
        position: offer_create_params.Position,
        department_id: Optional[str] | Omit = omit,
        workplace_id: Optional[str] | Omit = omit,
        manager_id: Optional[str] | Omit = omit,
        level_id: Optional[str] | Omit = omit,
        worker_type: Literal["employee", "us_contractor", "global_contractor"],
        compensation: offer_create_params.Compensation,
        expiration_time: Optional[str] | Omit = omit,
        background_check_work_location: Optional[offer_create_params.BackgroundCheckWorkLocation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferCreateResponse:
        """
        Create and send a candidate offer. The candidate receives an email with a link to the offer portal.

        Args:
            candidate: Body parameter.
            position: Body parameter.
            department_id: The unique public id of the department
            workplace_id: Public workplace identifier
            manager_id: The id of the worker.
            level_id: The unique public id of the job level
            worker_type: Body parameter.
            compensation: Body parameter.
            expiration_time: Body parameter.
            background_check_work_location: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferCreateResponse: Success

        Example:
            ```python
            offer = await client.offers.create(
                candidate={"first_name": "x", "last_name": "x", "email": "john@joinwarp.com"},
                position={"title": "x", "start_date": ""},
                worker_type="employee",
                compensation={"pay_basis": "year", "pay_currency": "USD", "pay_rate": 1},
            )
            ```
        """
        return await self._post(
            "/v1/offers",
            body=await async_maybe_transform(
                {
                    "candidate": candidate,
                    "position": position,
                    "department_id": department_id,
                    "workplace_id": workplace_id,
                    "manager_id": manager_id,
                    "level_id": level_id,
                    "worker_type": worker_type,
                    "compensation": compensation,
                    "expiration_time": expiration_time,
                    "background_check_work_location": background_check_work_location,
                },
                offer_create_params.OfferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferCreateResponse,
        )

    async def void(
        self,
        id: str,
        *,
        void_reason: Literal["candidate_declined", "other"],
        void_notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferVoidResponse:
        """
        Void a previously sent offer. Only sent offers can be voided.

        Args:
            id: The tag of the offer.
            void_reason: Body parameter.
            void_notes: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferVoidResponse: Success

        Example:
            ```python
            offer = await client.offers.void(
                id="offr_1234",
                void_reason="candidate_declined",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/offers/{id}/void", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "void_reason": void_reason,
                    "void_notes": void_notes,
                },
                offer_void_params.OfferVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferVoidResponse,
        )

    async def extend_deadline(
        self,
        id: str,
        *,
        expiration_time: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferExtendDeadlineResponse:
        """
        Extend the expiration deadline of a sent offer.

        Args:
            id: The tag of the offer.
            expiration_time: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferExtendDeadlineResponse: Success

        Example:
            ```python
            offer = await client.offers.extend_deadline(
                id="offr_1234",
                expiration_time="",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/offers/{id}/extend-deadline", **{"id": id}),
            body=await async_maybe_transform(
                {"expiration_time": expiration_time},
                offer_extend_deadline_params.OfferExtendDeadlineParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferExtendDeadlineResponse,
        )

    async def resend(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferResendResponse:
        """
        Resend the offer email to the candidate for a sent offer.

        Args:
            id: The tag of the offer.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OfferResendResponse: Success

        Example:
            ```python
            offer = await client.offers.resend(
                id="offr_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/offers/{id}/resend", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferResendResponse,
        )


class OffersResourceWithRawResponse:
    def __init__(self, offers: OffersResource) -> None:
        self._offers = offers

        self.list = to_raw_response_wrapper(
            offers.list,
        )
        self.create = to_raw_response_wrapper(
            offers.create,
        )
        self.void = to_raw_response_wrapper(
            offers.void,
        )
        self.extend_deadline = to_raw_response_wrapper(
            offers.extend_deadline,
        )
        self.resend = to_raw_response_wrapper(
            offers.resend,
        )


class AsyncOffersResourceWithRawResponse:
    def __init__(self, offers: AsyncOffersResource) -> None:
        self._offers = offers

        self.list = async_to_raw_response_wrapper(
            offers.list,
        )
        self.create = async_to_raw_response_wrapper(
            offers.create,
        )
        self.void = async_to_raw_response_wrapper(
            offers.void,
        )
        self.extend_deadline = async_to_raw_response_wrapper(
            offers.extend_deadline,
        )
        self.resend = async_to_raw_response_wrapper(
            offers.resend,
        )


class OffersResourceWithStreamingResponse:
    def __init__(self, offers: OffersResource) -> None:
        self._offers = offers

        self.list = to_streamed_response_wrapper(
            offers.list,
        )
        self.create = to_streamed_response_wrapper(
            offers.create,
        )
        self.void = to_streamed_response_wrapper(
            offers.void,
        )
        self.extend_deadline = to_streamed_response_wrapper(
            offers.extend_deadline,
        )
        self.resend = to_streamed_response_wrapper(
            offers.resend,
        )


class AsyncOffersResourceWithStreamingResponse:
    def __init__(self, offers: AsyncOffersResource) -> None:
        self._offers = offers

        self.list = async_to_streamed_response_wrapper(
            offers.list,
        )
        self.create = async_to_streamed_response_wrapper(
            offers.create,
        )
        self.void = async_to_streamed_response_wrapper(
            offers.void,
        )
        self.extend_deadline = async_to_streamed_response_wrapper(
            offers.extend_deadline,
        )
        self.resend = async_to_streamed_response_wrapper(
            offers.resend,
        )
