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
from ..types.bank_account_list_response import BankAccountListResponse
from ..types import bank_account_list_params
from ..types.public_bank_account import PublicBankAccount

__all__ = ["BankAccountsResource", "AsyncBankAccountsResource"]


class BankAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BankAccountsResourceWithRawResponse:
        return BankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankAccountsResourceWithStreamingResponse:
        return BankAccountsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[Literal["verified", "pending_verification", "needs_address", "unverified", "blocked"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccountListResponse:
        """
        List stored worker bank accounts, newest first. Requires workers banking and profile read scopes.

        Args:
            limit: Query parameter.
            after_id: The tag of the bank account.
            before_id: The tag of the bank account.
            worker_ids: Worker IDs to include as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            statuses: Verification states to include as repeated parameters. Omit for all states.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BankAccountListResponse: Success

        Example:
            ```python
            bank_account = client.bank_accounts.list(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/bank_accounts",
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
                    bank_account_list_params.BankAccountListParams,
                ),
            ),
            cast_to=BankAccountListResponse,
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
    ) -> PublicBankAccount:
        """
        Get a stored worker bank account. Requires workers banking and profile read scopes.

        Args:
            id: The tag of the bank account.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBankAccount

        Example:
            ```python
            bank_account = client.bank_accounts.get(
                id="bank_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/bank_accounts/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBankAccount,
        )


class AsyncBankAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBankAccountsResourceWithRawResponse:
        return AsyncBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankAccountsResourceWithStreamingResponse:
        return AsyncBankAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        statuses: Optional[List[Literal["verified", "pending_verification", "needs_address", "unverified", "blocked"]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankAccountListResponse:
        """
        List stored worker bank accounts, newest first. Requires workers banking and profile read scopes.

        Args:
            limit: Query parameter.
            after_id: The tag of the bank account.
            before_id: The tag of the bank account.
            worker_ids: Worker IDs to include as repeated parameters. Omit for all workers. Unknown or foreign IDs contribute no matches.
            statuses: Verification states to include as repeated parameters. Omit for all states.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BankAccountListResponse: Success

        Example:
            ```python
            bank_account = await client.bank_accounts.list(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/bank_accounts",
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
                    bank_account_list_params.BankAccountListParams,
                ),
            ),
            cast_to=BankAccountListResponse,
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
    ) -> PublicBankAccount:
        """
        Get a stored worker bank account. Requires workers banking and profile read scopes.

        Args:
            id: The tag of the bank account.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicBankAccount

        Example:
            ```python
            bank_account = await client.bank_accounts.get(
                id="bank_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/bank_accounts/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicBankAccount,
        )


class BankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.list = to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.get = to_raw_response_wrapper(
            bank_accounts.get,
        )


class AsyncBankAccountsResourceWithRawResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.list = async_to_raw_response_wrapper(
            bank_accounts.list,
        )
        self.get = async_to_raw_response_wrapper(
            bank_accounts.get,
        )


class BankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: BankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.list = to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.get = to_streamed_response_wrapper(
            bank_accounts.get,
        )


class AsyncBankAccountsResourceWithStreamingResponse:
    def __init__(self, bank_accounts: AsyncBankAccountsResource) -> None:
        self._bank_accounts = bank_accounts

        self.list = async_to_streamed_response_wrapper(
            bank_accounts.list,
        )
        self.get = async_to_streamed_response_wrapper(
            bank_accounts.get,
        )
