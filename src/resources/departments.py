# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ..types.department_list_response import DepartmentListResponse, Data
from ..types import department_list_params, department_create_params, department_update_params
from ..types.department_create_response import DepartmentCreateResponse
from ..types.department_update_response import DepartmentUpdateResponse

__all__ = ["DepartmentsResource", "AsyncDepartmentsResource"]


class DepartmentsResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> DepartmentsResourceWithRawResponse:
        return DepartmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DepartmentsResourceWithStreamingResponse:
        return DepartmentsResourceWithStreamingResponse(self)

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
    ) -> DepartmentListResponse:
        """
        List all departments for your company.
        
        Args:
            limit: a number less than or equal to 100
            after_id: The unique public id of the department
            before_id: The unique public id of the department
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentListResponse: Success
        
        Example:
            ```python
            department = client.departments.list()
            ```
        """
        return self._get(
            "/v1/departments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, department_list_params.DepartmentListParams)),
            cast_to=DepartmentListResponse,
        )

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepartmentCreateResponse:
        """
        Create a new department.
        
        Args:
            name: a non empty string
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentCreateResponse: Success
        
        Example:
            ```python
            department = client.departments.create(
                name="",
            )
            ```
        """
        return self._post(
            "/v1/departments",
            body=maybe_transform(
            {"name": name},
            department_create_params.DepartmentCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DepartmentCreateResponse,
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
    ) -> DepartmentUpdateResponse:
        """
        Update an existing department.
        
        Args:
            id: The unique public id of the department
            name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentUpdateResponse: Success
        
        Example:
            ```python
            department = client.departments.update(
                id="dpt_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/departments/{id}", **{"id": id}),
            body=maybe_transform(
            {"name": name},
            department_update_params.DepartmentUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DepartmentUpdateResponse,
        )


class AsyncDepartmentsResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncDepartmentsResourceWithRawResponse:
        return AsyncDepartmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDepartmentsResourceWithStreamingResponse:
        return AsyncDepartmentsResourceWithStreamingResponse(self)

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
    ) -> DepartmentListResponse:
        """
        List all departments for your company.
        
        Args:
            limit: a number less than or equal to 100
            after_id: The unique public id of the department
            before_id: The unique public id of the department
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentListResponse: Success
        
        Example:
            ```python
            department = await client.departments.list()
            ```
        """
        return await self._get(
            "/v1/departments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id}, department_list_params.DepartmentListParams)),
            cast_to=DepartmentListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DepartmentCreateResponse:
        """
        Create a new department.
        
        Args:
            name: a non empty string
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentCreateResponse: Success
        
        Example:
            ```python
            department = await client.departments.create(
                name="",
            )
            ```
        """
        return await self._post(
            "/v1/departments",
            body=await async_maybe_transform(
            {"name": name},
            department_create_params.DepartmentCreateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DepartmentCreateResponse,
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
    ) -> DepartmentUpdateResponse:
        """
        Update an existing department.
        
        Args:
            id: The unique public id of the department
            name: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            DepartmentUpdateResponse: Success
        
        Example:
            ```python
            department = await client.departments.update(
                id="dpt_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/departments/{id}", **{"id": id}),
            body=await async_maybe_transform(
            {"name": name},
            department_update_params.DepartmentUpdateParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DepartmentUpdateResponse,
        )


class DepartmentsResourceWithRawResponse:
    def __init__(self, departments: DepartmentsResource) -> None:
        self._departments = departments

        self.list = to_raw_response_wrapper(
            departments.list,
        )
        self.create = to_raw_response_wrapper(
            departments.create,
        )
        self.update = to_raw_response_wrapper(
            departments.update,
        )


class AsyncDepartmentsResourceWithRawResponse:
    def __init__(self, departments: AsyncDepartmentsResource) -> None:
        self._departments = departments

        self.list = async_to_raw_response_wrapper(
            departments.list,
        )
        self.create = async_to_raw_response_wrapper(
            departments.create,
        )
        self.update = async_to_raw_response_wrapper(
            departments.update,
        )


class DepartmentsResourceWithStreamingResponse:
    def __init__(self, departments: DepartmentsResource) -> None:
        self._departments = departments

        self.list = to_streamed_response_wrapper(
            departments.list,
        )
        self.create = to_streamed_response_wrapper(
            departments.create,
        )
        self.update = to_streamed_response_wrapper(
            departments.update,
        )


class AsyncDepartmentsResourceWithStreamingResponse:
    def __init__(self, departments: AsyncDepartmentsResource) -> None:
        self._departments = departments

        self.list = async_to_streamed_response_wrapper(
            departments.list,
        )
        self.create = async_to_streamed_response_wrapper(
            departments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            departments.update,
        )
