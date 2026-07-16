# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import time_off, workers, departments, workplaces
    from .resources.time_off import TimeOffResource, AsyncTimeOffResource
    from .resources.workers import WorkersResource, AsyncWorkersResource
    from .resources.departments import DepartmentsResource, AsyncDepartmentsResource
    from .resources.workplaces import WorkplacesResource, AsyncWorkplacesResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = ["Warp", "AsyncWarp", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class Warp(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Warp client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WARP_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("WARP_API_KEY")
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("WARP_BASE_URL")
        if base_url is None:
            base_url = "https://api.joinwarp.com"
        custom_headers_env = os.environ.get("WARP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def time_off(self) -> "TimeOffResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import TimeOffResource
        return TimeOffResource(self)

    @cached_property
    def workers(self) -> "WorkersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import WorkersResource
        return WorkersResource(self)

    @cached_property
    def departments(self) -> "DepartmentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import DepartmentsResource
        return DepartmentsResource(self)

    @cached_property
    def workplaces(self) -> "WorkplacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import WorkplacesResource
        return WorkplacesResource(self)

    @cached_property
    def with_raw_response(self) -> WarpWithRawResponse:
        return WarpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WarpWithStreamedResponse:
        return WarpWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
        }

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"x-api-key": value}


    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("x-api-key"):
            return
        if isinstance(custom_headers.get("x-api-key"), Omit):
            return
        raise TypeError("Could not resolve authentication method. Expected x-api-key to be set.")


    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncWarp(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncWarp client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `WARP_API_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("WARP_API_KEY")
        self.api_key = api_key
        if base_url is None:
            base_url = os.environ.get("WARP_BASE_URL")
        if base_url is None:
            base_url = "https://api.joinwarp.com"
        custom_headers_env = os.environ.get("WARP_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def time_off(self) -> "AsyncTimeOffResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import AsyncTimeOffResource
        return AsyncTimeOffResource(self)

    @cached_property
    def workers(self) -> "AsyncWorkersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import AsyncWorkersResource
        return AsyncWorkersResource(self)

    @cached_property
    def departments(self) -> "AsyncDepartmentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import AsyncDepartmentsResource
        return AsyncDepartmentsResource(self)

    @cached_property
    def workplaces(self) -> "AsyncWorkplacesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import AsyncWorkplacesResource
        return AsyncWorkplacesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncWarpWithRawResponse:
        return AsyncWarpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWarpWithStreamedResponse:
        return AsyncWarpWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
        }

    @property
    def _api_key_header_auth(self) -> dict[str, str]:
        value = self.api_key
        if value is None:
            return {}
        return {"x-api-key": value}


    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("x-api-key"):
            return
        if isinstance(custom_headers.get("x-api-key"), Omit):
            return
        raise TypeError("Could not resolve authentication method. Expected x-api-key to be set.")


    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class WarpWithRawResponse:
    _client: Warp

    def __init__(self, client: Warp) -> None:
        self._client = client

    @cached_property
    def time_off(self) -> time_off.TimeOffResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import TimeOffResourceWithRawResponse
        return TimeOffResourceWithRawResponse(self._client.time_off)

    @cached_property
    def workers(self) -> workers.WorkersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import WorkersResourceWithRawResponse
        return WorkersResourceWithRawResponse(self._client.workers)

    @cached_property
    def departments(self) -> departments.DepartmentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import DepartmentsResourceWithRawResponse
        return DepartmentsResourceWithRawResponse(self._client.departments)

    @cached_property
    def workplaces(self) -> workplaces.WorkplacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import WorkplacesResourceWithRawResponse
        return WorkplacesResourceWithRawResponse(self._client.workplaces)


class AsyncWarpWithRawResponse:
    _client: AsyncWarp

    def __init__(self, client: AsyncWarp) -> None:
        self._client = client

    @cached_property
    def time_off(self) -> time_off.AsyncTimeOffResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import AsyncTimeOffResourceWithRawResponse
        return AsyncTimeOffResourceWithRawResponse(self._client.time_off)

    @cached_property
    def workers(self) -> workers.AsyncWorkersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import AsyncWorkersResourceWithRawResponse
        return AsyncWorkersResourceWithRawResponse(self._client.workers)

    @cached_property
    def departments(self) -> departments.AsyncDepartmentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import AsyncDepartmentsResourceWithRawResponse
        return AsyncDepartmentsResourceWithRawResponse(self._client.departments)

    @cached_property
    def workplaces(self) -> workplaces.AsyncWorkplacesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import AsyncWorkplacesResourceWithRawResponse
        return AsyncWorkplacesResourceWithRawResponse(self._client.workplaces)


class WarpWithStreamedResponse:
    _client: Warp

    def __init__(self, client: Warp) -> None:
        self._client = client

    @cached_property
    def time_off(self) -> time_off.TimeOffResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import TimeOffResourceWithStreamingResponse
        return TimeOffResourceWithStreamingResponse(self._client.time_off)

    @cached_property
    def workers(self) -> workers.WorkersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import WorkersResourceWithStreamingResponse
        return WorkersResourceWithStreamingResponse(self._client.workers)

    @cached_property
    def departments(self) -> departments.DepartmentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import DepartmentsResourceWithStreamingResponse
        return DepartmentsResourceWithStreamingResponse(self._client.departments)

    @cached_property
    def workplaces(self) -> workplaces.WorkplacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import WorkplacesResourceWithStreamingResponse
        return WorkplacesResourceWithStreamingResponse(self._client.workplaces)


class AsyncWarpWithStreamedResponse:
    _client: AsyncWarp

    def __init__(self, client: AsyncWarp) -> None:
        self._client = client

    @cached_property
    def time_off(self) -> time_off.AsyncTimeOffResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.time_off import AsyncTimeOffResourceWithStreamingResponse
        return AsyncTimeOffResourceWithStreamingResponse(self._client.time_off)

    @cached_property
    def workers(self) -> workers.AsyncWorkersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workers import AsyncWorkersResourceWithStreamingResponse
        return AsyncWorkersResourceWithStreamingResponse(self._client.workers)

    @cached_property
    def departments(self) -> departments.AsyncDepartmentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.departments import AsyncDepartmentsResourceWithStreamingResponse
        return AsyncDepartmentsResourceWithStreamingResponse(self._client.departments)

    @cached_property
    def workplaces(self) -> workplaces.AsyncWorkplacesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.workplaces import AsyncWorkplacesResourceWithStreamingResponse
        return AsyncWorkplacesResourceWithStreamingResponse(self._client.workplaces)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Warp
AsyncClient = AsyncWarp
