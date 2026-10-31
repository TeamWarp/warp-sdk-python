# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union
from typing_extensions import Literal
from .._types import SequenceNotStr

from .._types import Body, Omit, Query, Headers, NotGiven, NoneType, omit, not_given
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
from ..types.custom_field_list_response import CustomFieldListResponse
from ..types.custom_field_create_response import CustomFieldCreateResponse
from ..types import (
    custom_field_create_params,
    custom_field_update_params,
    custom_field_create_option_params,
    custom_field_update_option_params,
    custom_field_list_values_params,
    custom_field_upsert_value_params,
    custom_field_clear_value_params,
)
from ..types.custom_field_get_response import CustomFieldGetResponse
from ..types.custom_field_update_response import CustomFieldUpdateResponse
from ..types.custom_field_archive_response import CustomFieldArchiveResponse
from ..types.custom_field_create_option_response import CustomFieldCreateOptionResponse
from ..types.custom_field_update_option_response import CustomFieldUpdateOptionResponse
from ..types.custom_field_archive_option_response import CustomFieldArchiveOptionResponse
from ..types.custom_field_list_values_response import CustomFieldListValuesResponse
from ..types.custom_field_upsert_value_response import CustomFieldUpsertValueResponse

__all__ = ["CustomFieldsResource", "AsyncCustomFieldsResource"]


class CustomFieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomFieldsResourceWithRawResponse:
        return CustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldsResourceWithStreamingResponse:
        return CustomFieldsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldListResponse:
        """
        List the custom worker field definitions your API key can read. Each field belongs to a worker-data category; fields whose category your key cannot read are omitted unless the key holds workers:custom_fields.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldListResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.list()
            ```
        """
        return self._get(
            "/v1/custom_fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldListResponse,
        )

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["text", "number", "date", "boolean", "currency", "percentage", "select", "multi_select"],
        config: Optional[object] | Omit = omit,
        category: Literal["info", "pii", "compensation", "banking", "it", "compliance"],
        access_level: Optional[Literal["admins", "manager", "worker"]] | Omit = omit,
        input_by: Optional[Literal["admin", "worker"]] | Omit = omit,
        required: Optional[bool] | Omit = omit,
        options: Optional[Iterable[custom_field_create_params.Option]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldCreateResponse:
        """
        Create a custom worker field definition. The field type is immutable after creation. Select and multi_select fields can include their initial options. Access to values derives from the field category; requires the workers:custom_fields permission.

        Args:
            name: Body parameter.
            description: Body parameter.
            type: Body parameter.
            config: Body parameter.
            category: Body parameter.
            access_level: Body parameter.
            input_by: Body parameter.
            required: Body parameter.
            options: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldCreateResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.create(
                name="x",
                type="text",
                category="info",
            )
            ```
        """
        return self._post(
            "/v1/custom_fields",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "type": type,
                    "config": config,
                    "category": category,
                    "access_level": access_level,
                    "input_by": input_by,
                    "required": required,
                    "options": options,
                },
                custom_field_create_params.CustomFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldCreateResponse,
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
    ) -> CustomFieldGetResponse:
        """
        Get a custom worker field definition, including its select options. Archived options may appear on existing worker values but cannot be newly selected.

        Args:
            id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldGetResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.get(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/custom_fields/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldGetResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        config: Optional[object] | Omit = omit,
        category: Optional[Literal["info", "pii", "compensation", "banking", "it", "compliance"]] | Omit = omit,
        access_level: Optional[Literal["admins", "manager", "worker"]] | Omit = omit,
        input_by: Optional[Literal["admin", "worker"]] | Omit = omit,
        required: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpdateResponse:
        """
        Update a custom worker field definition. The field type cannot be changed; create a new field instead. Requires the workers:custom_fields permission; changing the category, access level, or input source requires the manage level.

        Args:
            id: The tag of a company custom worker field.
            name: Body parameter.
            description: Body parameter.
            config: Body parameter.
            category: Body parameter.
            access_level: Body parameter.
            input_by: Body parameter.
            required: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpdateResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.update(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/custom_fields/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "category": category,
                    "access_level": access_level,
                    "input_by": input_by,
                    "required": required,
                },
                custom_field_update_params.CustomFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpdateResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldArchiveResponse:
        """
        Archive a custom worker field. Archived fields keep their existing worker values but cannot receive new ones. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldArchiveResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.archive(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/custom_fields/{id}/archive", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldArchiveResponse,
        )

    def create_option(
        self,
        id: str,
        *,
        label: str,
        value: str,
        sort_order: Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldCreateOptionResponse:
        """
        Add an option to a select or multi_select custom worker field. The option value should be treated as stable; the label can change. Requires the workers:custom_fields permission.

        Args:
            id: The tag of a company custom worker field.
            label: Body parameter.
            value: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldCreateOptionResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.create_option(
                id="cf_1234",
                label="x",
                value="x",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/custom_fields/{id}/options", **{"id": id}),
            body=maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "sort_order": sort_order,
                },
                custom_field_create_option_params.CustomFieldCreateOptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldCreateOptionResponse,
        )

    def update_option(
        self,
        id: str,
        *,
        label: Optional[str] | Omit = omit,
        sort_order: Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpdateOptionResponse:
        """
        Update the label or sort order of a custom worker field option. Options of archived fields cannot be edited. Requires the workers:custom_fields permission.

        Args:
            id: The tag of a company custom worker field option.
            label: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpdateOptionResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.update_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/custom_field_options/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "label": label,
                    "sort_order": sort_order,
                },
                custom_field_update_option_params.CustomFieldUpdateOptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpdateOptionResponse,
        )

    def delete_option(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a custom worker field option that is not applied to any worker. Options in use must be archived instead. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field option.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            client.custom_fields.delete_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/custom_field_options/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def archive_option(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldArchiveOptionResponse:
        """
        Archive a custom worker field option. Archived options remain on existing worker values but cannot be newly selected. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field option.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldArchiveOptionResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.archive_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/custom_field_options/{id}/archive", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldArchiveOptionResponse,
        )

    def list_values(
        self,
        *,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        field_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldListValuesResponse:
        """
        List custom field values for workers, optionally filtered by worker or field. Values are returned only for fields whose category your API key can read.

        Args:
            worker_ids: Query parameter.
            field_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldListValuesResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.list_values()
            ```
        """
        return self._get(
            "/v1/custom_field_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"worker_ids": worker_ids, "field_ids": field_ids},
                    custom_field_list_values_params.CustomFieldListValuesParams,
                ),
            ),
            cast_to=CustomFieldListValuesResponse,
        )

    def upsert_value(
        self,
        *,
        worker_id: str,
        field_id: str,
        value: custom_field_upsert_value_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpsertValueResponse:
        """
        Create or replace a worker's value for a custom field. The value shape must match the field type, and your API key must hold write on the field's category.

        Args:
            worker_id: The id of the worker.
            field_id: The tag of a company custom worker field.
            value: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpsertValueResponse: Success

        Example:
            ```python
            custom_field = client.custom_fields.upsert_value(
                worker_id="wrk_1234",
                field_id="cf_1234",
                value={"type": "text", "value": ""},
            )
            ```
        """
        return self._put(
            "/v1/custom_field_values",
            body=maybe_transform(
                {
                    "worker_id": worker_id,
                    "field_id": field_id,
                    "value": value,
                },
                custom_field_upsert_value_params.CustomFieldUpsertValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpsertValueResponse,
        )

    def clear_value(
        self,
        *,
        worker_id: str,
        field_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a worker's value for a custom field. Your API key must hold write on the field's category.

        Args:
            worker_id: The id of the worker.
            field_id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            client.custom_fields.clear_value(
                worker_id="wrk_1234",
                field_id="cf_1234",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v1/custom_field_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"worker_id": worker_id, "field_id": field_id},
                    custom_field_clear_value_params.CustomFieldClearValueParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncCustomFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldsResourceWithRawResponse:
        return AsyncCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        return AsyncCustomFieldsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldListResponse:
        """
        List the custom worker field definitions your API key can read. Each field belongs to a worker-data category; fields whose category your key cannot read are omitted unless the key holds workers:custom_fields.

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldListResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.list()
            ```
        """
        return await self._get(
            "/v1/custom_fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        type: Literal["text", "number", "date", "boolean", "currency", "percentage", "select", "multi_select"],
        config: Optional[object] | Omit = omit,
        category: Literal["info", "pii", "compensation", "banking", "it", "compliance"],
        access_level: Optional[Literal["admins", "manager", "worker"]] | Omit = omit,
        input_by: Optional[Literal["admin", "worker"]] | Omit = omit,
        required: Optional[bool] | Omit = omit,
        options: Optional[Iterable[custom_field_create_params.Option]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldCreateResponse:
        """
        Create a custom worker field definition. The field type is immutable after creation. Select and multi_select fields can include their initial options. Access to values derives from the field category; requires the workers:custom_fields permission.

        Args:
            name: Body parameter.
            description: Body parameter.
            type: Body parameter.
            config: Body parameter.
            category: Body parameter.
            access_level: Body parameter.
            input_by: Body parameter.
            required: Body parameter.
            options: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldCreateResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.create(
                name="x",
                type="text",
                category="info",
            )
            ```
        """
        return await self._post(
            "/v1/custom_fields",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "type": type,
                    "config": config,
                    "category": category,
                    "access_level": access_level,
                    "input_by": input_by,
                    "required": required,
                    "options": options,
                },
                custom_field_create_params.CustomFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldCreateResponse,
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
    ) -> CustomFieldGetResponse:
        """
        Get a custom worker field definition, including its select options. Archived options may appear on existing worker values but cannot be newly selected.

        Args:
            id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldGetResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.get(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/custom_fields/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldGetResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        config: Optional[object] | Omit = omit,
        category: Optional[Literal["info", "pii", "compensation", "banking", "it", "compliance"]] | Omit = omit,
        access_level: Optional[Literal["admins", "manager", "worker"]] | Omit = omit,
        input_by: Optional[Literal["admin", "worker"]] | Omit = omit,
        required: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpdateResponse:
        """
        Update a custom worker field definition. The field type cannot be changed; create a new field instead. Requires the workers:custom_fields permission; changing the category, access level, or input source requires the manage level.

        Args:
            id: The tag of a company custom worker field.
            name: Body parameter.
            description: Body parameter.
            config: Body parameter.
            category: Body parameter.
            access_level: Body parameter.
            input_by: Body parameter.
            required: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpdateResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.update(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/custom_fields/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "category": category,
                    "access_level": access_level,
                    "input_by": input_by,
                    "required": required,
                },
                custom_field_update_params.CustomFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpdateResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldArchiveResponse:
        """
        Archive a custom worker field. Archived fields keep their existing worker values but cannot receive new ones. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldArchiveResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.archive(
                id="cf_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/custom_fields/{id}/archive", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldArchiveResponse,
        )

    async def create_option(
        self,
        id: str,
        *,
        label: str,
        value: str,
        sort_order: Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldCreateOptionResponse:
        """
        Add an option to a select or multi_select custom worker field. The option value should be treated as stable; the label can change. Requires the workers:custom_fields permission.

        Args:
            id: The tag of a company custom worker field.
            label: Body parameter.
            value: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldCreateOptionResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.create_option(
                id="cf_1234",
                label="x",
                value="x",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/custom_fields/{id}/options", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "value": value,
                    "sort_order": sort_order,
                },
                custom_field_create_option_params.CustomFieldCreateOptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldCreateOptionResponse,
        )

    async def update_option(
        self,
        id: str,
        *,
        label: Optional[str] | Omit = omit,
        sort_order: Optional[Union[float, Literal["Infinity", "-Infinity", "NaN"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpdateOptionResponse:
        """
        Update the label or sort order of a custom worker field option. Options of archived fields cannot be edited. Requires the workers:custom_fields permission.

        Args:
            id: The tag of a company custom worker field option.
            label: Body parameter.
            sort_order: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpdateOptionResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.update_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/custom_field_options/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "sort_order": sort_order,
                },
                custom_field_update_option_params.CustomFieldUpdateOptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpdateOptionResponse,
        )

    async def delete_option(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a custom worker field option that is not applied to any worker. Options in use must be archived instead. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field option.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            await client.custom_fields.delete_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/custom_field_options/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def archive_option(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldArchiveOptionResponse:
        """
        Archive a custom worker field option. Archived options remain on existing worker values but cannot be newly selected. Requires the workers:custom_fields permission at the manage level.

        Args:
            id: The tag of a company custom worker field option.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldArchiveOptionResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.archive_option(
                id="cfo_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/custom_field_options/{id}/archive", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldArchiveOptionResponse,
        )

    async def list_values(
        self,
        *,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        field_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldListValuesResponse:
        """
        List custom field values for workers, optionally filtered by worker or field. Values are returned only for fields whose category your API key can read.

        Args:
            worker_ids: Query parameter.
            field_ids: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldListValuesResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.list_values()
            ```
        """
        return await self._get(
            "/v1/custom_field_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"worker_ids": worker_ids, "field_ids": field_ids},
                    custom_field_list_values_params.CustomFieldListValuesParams,
                ),
            ),
            cast_to=CustomFieldListValuesResponse,
        )

    async def upsert_value(
        self,
        *,
        worker_id: str,
        field_id: str,
        value: custom_field_upsert_value_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomFieldUpsertValueResponse:
        """
        Create or replace a worker's value for a custom field. The value shape must match the field type, and your API key must hold write on the field's category.

        Args:
            worker_id: The id of the worker.
            field_id: The tag of a company custom worker field.
            value: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomFieldUpsertValueResponse: Success

        Example:
            ```python
            custom_field = await client.custom_fields.upsert_value(
                worker_id="wrk_1234",
                field_id="cf_1234",
                value={"type": "text", "value": ""},
            )
            ```
        """
        return await self._put(
            "/v1/custom_field_values",
            body=await async_maybe_transform(
                {
                    "worker_id": worker_id,
                    "field_id": field_id,
                    "value": value,
                },
                custom_field_upsert_value_params.CustomFieldUpsertValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomFieldUpsertValueResponse,
        )

    async def clear_value(
        self,
        *,
        worker_id: str,
        field_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a worker's value for a custom field. Your API key must hold write on the field's category.

        Args:
            worker_id: The id of the worker.
            field_id: The tag of a company custom worker field.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            <No Content>

        Example:
            ```python
            await client.custom_fields.clear_value(
                worker_id="wrk_1234",
                field_id="cf_1234",
            )
            ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v1/custom_field_values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"worker_id": worker_id, "field_id": field_id},
                    custom_field_clear_value_params.CustomFieldClearValueParams,
                ),
            ),
            cast_to=NoneType,
        )


class CustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.list = to_raw_response_wrapper(
            custom_fields.list,
        )
        self.create = to_raw_response_wrapper(
            custom_fields.create,
        )
        self.get = to_raw_response_wrapper(
            custom_fields.get,
        )
        self.update = to_raw_response_wrapper(
            custom_fields.update,
        )
        self.archive = to_raw_response_wrapper(
            custom_fields.archive,
        )
        self.create_option = to_raw_response_wrapper(
            custom_fields.create_option,
        )
        self.update_option = to_raw_response_wrapper(
            custom_fields.update_option,
        )
        self.delete_option = to_raw_response_wrapper(
            custom_fields.delete_option,
        )
        self.archive_option = to_raw_response_wrapper(
            custom_fields.archive_option,
        )
        self.list_values = to_raw_response_wrapper(
            custom_fields.list_values,
        )
        self.upsert_value = to_raw_response_wrapper(
            custom_fields.upsert_value,
        )
        self.clear_value = to_raw_response_wrapper(
            custom_fields.clear_value,
        )


class AsyncCustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.list = async_to_raw_response_wrapper(
            custom_fields.list,
        )
        self.create = async_to_raw_response_wrapper(
            custom_fields.create,
        )
        self.get = async_to_raw_response_wrapper(
            custom_fields.get,
        )
        self.update = async_to_raw_response_wrapper(
            custom_fields.update,
        )
        self.archive = async_to_raw_response_wrapper(
            custom_fields.archive,
        )
        self.create_option = async_to_raw_response_wrapper(
            custom_fields.create_option,
        )
        self.update_option = async_to_raw_response_wrapper(
            custom_fields.update_option,
        )
        self.delete_option = async_to_raw_response_wrapper(
            custom_fields.delete_option,
        )
        self.archive_option = async_to_raw_response_wrapper(
            custom_fields.archive_option,
        )
        self.list_values = async_to_raw_response_wrapper(
            custom_fields.list_values,
        )
        self.upsert_value = async_to_raw_response_wrapper(
            custom_fields.upsert_value,
        )
        self.clear_value = async_to_raw_response_wrapper(
            custom_fields.clear_value,
        )


class CustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.list = to_streamed_response_wrapper(
            custom_fields.list,
        )
        self.create = to_streamed_response_wrapper(
            custom_fields.create,
        )
        self.get = to_streamed_response_wrapper(
            custom_fields.get,
        )
        self.update = to_streamed_response_wrapper(
            custom_fields.update,
        )
        self.archive = to_streamed_response_wrapper(
            custom_fields.archive,
        )
        self.create_option = to_streamed_response_wrapper(
            custom_fields.create_option,
        )
        self.update_option = to_streamed_response_wrapper(
            custom_fields.update_option,
        )
        self.delete_option = to_streamed_response_wrapper(
            custom_fields.delete_option,
        )
        self.archive_option = to_streamed_response_wrapper(
            custom_fields.archive_option,
        )
        self.list_values = to_streamed_response_wrapper(
            custom_fields.list_values,
        )
        self.upsert_value = to_streamed_response_wrapper(
            custom_fields.upsert_value,
        )
        self.clear_value = to_streamed_response_wrapper(
            custom_fields.clear_value,
        )


class AsyncCustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.list = async_to_streamed_response_wrapper(
            custom_fields.list,
        )
        self.create = async_to_streamed_response_wrapper(
            custom_fields.create,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_fields.get,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_fields.update,
        )
        self.archive = async_to_streamed_response_wrapper(
            custom_fields.archive,
        )
        self.create_option = async_to_streamed_response_wrapper(
            custom_fields.create_option,
        )
        self.update_option = async_to_streamed_response_wrapper(
            custom_fields.update_option,
        )
        self.delete_option = async_to_streamed_response_wrapper(
            custom_fields.delete_option,
        )
        self.archive_option = async_to_streamed_response_wrapper(
            custom_fields.archive_option,
        )
        self.list_values = async_to_streamed_response_wrapper(
            custom_fields.list_values,
        )
        self.upsert_value = async_to_streamed_response_wrapper(
            custom_fields.upsert_value,
        )
        self.clear_value = async_to_streamed_response_wrapper(
            custom_fields.clear_value,
        )
