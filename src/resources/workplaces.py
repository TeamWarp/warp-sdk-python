# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ..types.workplace_list_response import WorkplaceListResponse, Data, Address
from ..types import workplace_list_params, workplace_create_params, workplace_update_params
from ..types.workplace_create_response import WorkplaceCreateResponse, Address
from ..types.workplace_update_response import WorkplaceUpdateResponse, Address

__all__ = ["WorkplacesResource", "AsyncWorkplacesResource"]


class WorkplacesResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> WorkplacesResourceWithRawResponse:
        return WorkplacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkplacesResourceWithStreamingResponse:
        return WorkplacesResourceWithStreamingResponse(self)

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
    ) -> WorkplaceListResponse:
        """
        List all workplaces for your company.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Public workplace identifier
            before_id: Public workplace identifier
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceListResponse: Success
        
        Example:
            ```python
            workplace = client.workplaces.list()
            ```
        """
        return self._get(
            "/v1/workplaces",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, workplace_list_params.WorkplaceListParams)),
            cast_to=WorkplaceListResponse,
        )

    def create(
        self,
        *,
        name: str,
        type: Literal["remote", "office"],
        address: workplace_create_params.Address,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkplaceCreateResponse:
        """
        Create a new workplace.
        
        Args:
            name: a non empty string
            type: Body parameter.
            address: A valid US address
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceCreateResponse: Success
        
        Example:
            ```python
            workplace = client.workplaces.create(
                name="",
                type="remote",
                address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
            )
            ```
        """
        return self._post(
            "/v1/workplaces",
            body=maybe_transform(
            {
            "name": name,
            "type": type,
            "address": address,
        },
            workplace_create_params.WorkplaceCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkplaceCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkplaceUpdateResponse:
        """
        Update an existing workplace.
        
        Args:
            id: Public workplace identifier
            name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceUpdateResponse: Success
        
        Example:
            ```python
            workplace = client.workplaces.update(
                id="wkp_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/workplaces/{id}", **{"id": id}),
            body=maybe_transform(
            {"name": name},
            workplace_update_params.WorkplaceUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkplaceUpdateResponse,
        )


class AsyncWorkplacesResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncWorkplacesResourceWithRawResponse:
        return AsyncWorkplacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkplacesResourceWithStreamingResponse:
        return AsyncWorkplacesResourceWithStreamingResponse(self)

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
    ) -> WorkplaceListResponse:
        """
        List all workplaces for your company.
        
        Args:
            limit: a number less than or equal to 100
            after_id: Public workplace identifier
            before_id: Public workplace identifier
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceListResponse: Success
        
        Example:
            ```python
            workplace = await client.workplaces.list()
            ```
        """
        return await self._get(
            "/v1/workplaces",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, workplace_list_params.WorkplaceListParams)),
            cast_to=WorkplaceListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        type: Literal["remote", "office"],
        address: workplace_create_params.Address,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkplaceCreateResponse:
        """
        Create a new workplace.
        
        Args:
            name: a non empty string
            type: Body parameter.
            address: A valid US address
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceCreateResponse: Success
        
        Example:
            ```python
            workplace = await client.workplaces.create(
                name="",
                type="remote",
                address={"line1": "x", "city": "", "postal_code": "", "state": "AL", "country": "US"},
            )
            ```
        """
        return await self._post(
            "/v1/workplaces",
            body=await async_maybe_transform(
            {
            "name": name,
            "type": type,
            "address": address,
        },
            workplace_create_params.WorkplaceCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkplaceCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkplaceUpdateResponse:
        """
        Update an existing workplace.
        
        Args:
            id: Public workplace identifier
            name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkplaceUpdateResponse: Success
        
        Example:
            ```python
            workplace = await client.workplaces.update(
                id="wkp_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/workplaces/{id}", **{"id": id}),
            body=await async_maybe_transform(
            {"name": name},
            workplace_update_params.WorkplaceUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkplaceUpdateResponse,
        )


class WorkplacesResourceWithRawResponse:
    def __init__(self, workplaces: WorkplacesResource) -> None:
        self._workplaces = workplaces

        self.list = to_raw_response_wrapper(
            workplaces.list,
        )
        self.create = to_raw_response_wrapper(
            workplaces.create,
        )
        self.update = to_raw_response_wrapper(
            workplaces.update,
        )


class AsyncWorkplacesResourceWithRawResponse:
    def __init__(self, workplaces: AsyncWorkplacesResource) -> None:
        self._workplaces = workplaces

        self.list = async_to_raw_response_wrapper(
            workplaces.list,
        )
        self.create = async_to_raw_response_wrapper(
            workplaces.create,
        )
        self.update = async_to_raw_response_wrapper(
            workplaces.update,
        )


class WorkplacesResourceWithStreamingResponse:
    def __init__(self, workplaces: WorkplacesResource) -> None:
        self._workplaces = workplaces

        self.list = to_streamed_response_wrapper(
            workplaces.list,
        )
        self.create = to_streamed_response_wrapper(
            workplaces.create,
        )
        self.update = to_streamed_response_wrapper(
            workplaces.update,
        )


class AsyncWorkplacesResourceWithStreamingResponse:
    def __init__(self, workplaces: AsyncWorkplacesResource) -> None:
        self._workplaces = workplaces

        self.list = async_to_streamed_response_wrapper(
            workplaces.list,
        )
        self.create = async_to_streamed_response_wrapper(
            workplaces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            workplaces.update,
        )
