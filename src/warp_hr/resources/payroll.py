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
from ..types.public_payroll_list import PublicPayrollList
from ..types.public_payroll_type import PublicPayrollType
from ..types.public_payroll_subtype import PublicPayrollSubtype
from ..types.public_payroll_status import PublicPayrollStatus
from ..types.public_pay_frequency import PublicPayFrequency
from ..types import payroll_list_params, payroll_list_paychecks_params
from ..types.public_payroll_detail import PublicPayrollDetail
from ..types.public_paycheck_list import PublicPaycheckList
from ..types.public_paycheck_status import PublicPaycheckStatus
from ..types.public_paycheck_payment_method import PublicPaycheckPaymentMethod
from ..types.public_payroll_currency import PublicPayrollCurrency
from ..types.public_paycheck_detail import PublicPaycheckDetail

__all__ = ["PayrollResource", "AsyncPayrollResource"]


class PayrollResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayrollResourceWithRawResponse:
        return PayrollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayrollResourceWithStreamingResponse:
        return PayrollResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[List[PublicPayrollType]] | Omit = omit,
        subtypes: Optional[List[PublicPayrollSubtype]] | Omit = omit,
        statuses: Optional[List[PublicPayrollStatus]] | Omit = omit,
        pay_frequencies: Optional[List[PublicPayFrequency]] | Omit = omit,
        payday_on_or_after: Optional[str] | Omit = omit,
        payday_before: Optional[str] | Omit = omit,
        pay_period_end_on_or_after: Optional[str] | Omit = omit,
        pay_period_end_before: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPayrollList:
        """
        List payroll summaries newest first with stable cursor ordering. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

        Args:
            limit: The maximum number of payrolls to return, from 1 to 50.
            after_id: Return payrolls after this payroll ID in the stable cursor order. Cannot be used with beforeId.
            before_id: Return payrolls before this payroll ID in the stable cursor order. Cannot be used with afterId.
            types: Payroll calculation types to include.
            subtypes: Payroll subtypes to include.
            statuses: Lifecycle statuses to include. Omit to include every status.
            pay_frequencies: Pay cadences to include.
            payday_on_or_after: Inclusive start of the half-open payday range.
            payday_before: Exclusive end of the half-open payday range.
            pay_period_end_on_or_after: Inclusive start of the half-open pay-period-end range.
            pay_period_end_before: Exclusive end of the half-open pay-period-end range.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayrollList

        Example:
            ```python
            payroll = client.payroll.list(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/payrolls",
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
                        "types": types,
                        "subtypes": subtypes,
                        "statuses": statuses,
                        "pay_frequencies": pay_frequencies,
                        "payday_on_or_after": payday_on_or_after,
                        "payday_before": payday_before,
                        "pay_period_end_on_or_after": pay_period_end_on_or_after,
                        "pay_period_end_before": pay_period_end_before,
                    },
                    payroll_list_params.PayrollListParams,
                ),
            ),
            cast_to=PublicPayrollList,
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
    ) -> PublicPayrollDetail:
        """
        Get a payroll by id. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Missing, foreign, unauthorized, or unavailable payrolls return 404.

        Args:
            id: The payroll ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayrollDetail

        Example:
            ```python
            payroll = client.payroll.get(
                id="pay_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/payrolls/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPayrollDetail,
        )

    def list_paychecks(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        payroll_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        worker_types: Optional[List[Literal["us_w2", "us_1099", "global_contractor", "eor_employee"]]] | Omit = omit,
        payroll_types: Optional[List[PublicPayrollType]] | Omit = omit,
        statuses: Optional[List[PublicPaycheckStatus]] | Omit = omit,
        payment_methods: Optional[List[PublicPaycheckPaymentMethod]] | Omit = omit,
        compensation_currencies: Optional[List[PublicPayrollCurrency]] | Omit = omit,
        pay_frequencies: Optional[List[PublicPayFrequency]] | Omit = omit,
        payday_on_or_after: Optional[str] | Omit = omit,
        payday_before: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPaycheckList:
        """
        List per-worker paycheck summaries newest first with stable cursor ordering. By default, the response includes every worker type visible to the API key, including US W-2 employees, US 1099 contractors, and global contractors; use workerTypes to narrow the results. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

        Args:
            limit: The maximum number of paychecks to return, from 1 to 50.
            after_id: Return paychecks after this paycheck ID in the stable cursor order. Cannot be used with beforeId.
            before_id: Return paychecks before this paycheck ID in the stable cursor order. Cannot be used with afterId.
            payroll_ids: Payrolls whose paychecks should be included.
            worker_ids: Workers whose paychecks should be included.
            worker_types: Worker classifications in effect for the paycheck to include. Omit to include every worker type visible to the API key.
            payroll_types: Payroll calculation types to include, subject to the API key permissions.
            statuses: Lifecycle statuses to include. Omit to include every status.
            payment_methods: Payment methods to include.
            compensation_currencies: Paycheck compensation currencies to include.
            pay_frequencies: Pay cadences to include.
            payday_on_or_after: Inclusive start of the half-open payday range.
            payday_before: Exclusive end of the half-open payday range.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPaycheckList

        Example:
            ```python
            payroll = client.payroll.list_paychecks(
                limit="limit",
            )
            ```
        """
        return self._get(
            "/v1/paychecks",
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
                        "payroll_ids": payroll_ids,
                        "worker_ids": worker_ids,
                        "worker_types": worker_types,
                        "payroll_types": payroll_types,
                        "statuses": statuses,
                        "payment_methods": payment_methods,
                        "compensation_currencies": compensation_currencies,
                        "pay_frequencies": pay_frequencies,
                        "payday_on_or_after": payday_on_or_after,
                        "payday_before": payday_before,
                    },
                    payroll_list_paychecks_params.PayrollListPaychecksParams,
                ),
            ),
            cast_to=PublicPaycheckList,
        )

    def get_paycheck(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPaycheckDetail:
        """
        Get a paycheck by id. All worker types use the same paycheck schema. Categories that do not apply to a worker are represented by zero-valued totals and empty line-item arrays. For example, a US 1099 contractor with no applicable payroll taxes returns zero `workerTaxes` and `employerTaxes` totals and an empty `taxes` array. Missing, foreign, unauthorized, or unavailable paychecks return 404.

        Args:
            id: The paycheck ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPaycheckDetail

        Example:
            ```python
            payroll = client.payroll.get_paycheck(
                id="pyc_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/paychecks/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPaycheckDetail,
        )


class AsyncPayrollResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayrollResourceWithRawResponse:
        return AsyncPayrollResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayrollResourceWithStreamingResponse:
        return AsyncPayrollResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        types: Optional[List[PublicPayrollType]] | Omit = omit,
        subtypes: Optional[List[PublicPayrollSubtype]] | Omit = omit,
        statuses: Optional[List[PublicPayrollStatus]] | Omit = omit,
        pay_frequencies: Optional[List[PublicPayFrequency]] | Omit = omit,
        payday_on_or_after: Optional[str] | Omit = omit,
        payday_before: Optional[str] | Omit = omit,
        pay_period_end_on_or_after: Optional[str] | Omit = omit,
        pay_period_end_before: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPayrollList:
        """
        List payroll summaries newest first with stable cursor ordering. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

        Args:
            limit: The maximum number of payrolls to return, from 1 to 50.
            after_id: Return payrolls after this payroll ID in the stable cursor order. Cannot be used with beforeId.
            before_id: Return payrolls before this payroll ID in the stable cursor order. Cannot be used with afterId.
            types: Payroll calculation types to include.
            subtypes: Payroll subtypes to include.
            statuses: Lifecycle statuses to include. Omit to include every status.
            pay_frequencies: Pay cadences to include.
            payday_on_or_after: Inclusive start of the half-open payday range.
            payday_before: Exclusive end of the half-open payday range.
            pay_period_end_on_or_after: Inclusive start of the half-open pay-period-end range.
            pay_period_end_before: Exclusive end of the half-open pay-period-end range.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayrollList

        Example:
            ```python
            payroll = await client.payroll.list(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/payrolls",
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
                        "types": types,
                        "subtypes": subtypes,
                        "statuses": statuses,
                        "pay_frequencies": pay_frequencies,
                        "payday_on_or_after": payday_on_or_after,
                        "payday_before": payday_before,
                        "pay_period_end_on_or_after": pay_period_end_on_or_after,
                        "pay_period_end_before": pay_period_end_before,
                    },
                    payroll_list_params.PayrollListParams,
                ),
            ),
            cast_to=PublicPayrollList,
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
    ) -> PublicPayrollDetail:
        """
        Get a payroll by id. Every amount in totals is expressed in fundingCurrency, the currency the employer uses to fund the payroll. Line-derived categories are converted and rounded per paycheck before aggregation, while netPay remains provider-authoritative. Missing, foreign, unauthorized, or unavailable payrolls return 404.

        Args:
            id: The payroll ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPayrollDetail

        Example:
            ```python
            payroll = await client.payroll.get(
                id="pay_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/payrolls/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPayrollDetail,
        )

    async def list_paychecks(
        self,
        *,
        limit: Optional[str],
        after_id: Optional[str] | Omit = omit,
        before_id: Optional[str] | Omit = omit,
        payroll_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        worker_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        worker_types: Optional[List[Literal["us_w2", "us_1099", "global_contractor", "eor_employee"]]] | Omit = omit,
        payroll_types: Optional[List[PublicPayrollType]] | Omit = omit,
        statuses: Optional[List[PublicPaycheckStatus]] | Omit = omit,
        payment_methods: Optional[List[PublicPaycheckPaymentMethod]] | Omit = omit,
        compensation_currencies: Optional[List[PublicPayrollCurrency]] | Omit = omit,
        pay_frequencies: Optional[List[PublicPayFrequency]] | Omit = omit,
        payday_on_or_after: Optional[str] | Omit = omit,
        payday_before: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPaycheckList:
        """
        List per-worker paycheck summaries newest first with stable cursor ordering. By default, the response includes every worker type visible to the API key, including US W-2 employees, US 1099 contractors, and global contractors; use workerTypes to narrow the results. Payroll type visibility follows the API key permissions. All lifecycle statuses are included unless statuses are provided.

        Args:
            limit: The maximum number of paychecks to return, from 1 to 50.
            after_id: Return paychecks after this paycheck ID in the stable cursor order. Cannot be used with beforeId.
            before_id: Return paychecks before this paycheck ID in the stable cursor order. Cannot be used with afterId.
            payroll_ids: Payrolls whose paychecks should be included.
            worker_ids: Workers whose paychecks should be included.
            worker_types: Worker classifications in effect for the paycheck to include. Omit to include every worker type visible to the API key.
            payroll_types: Payroll calculation types to include, subject to the API key permissions.
            statuses: Lifecycle statuses to include. Omit to include every status.
            payment_methods: Payment methods to include.
            compensation_currencies: Paycheck compensation currencies to include.
            pay_frequencies: Pay cadences to include.
            payday_on_or_after: Inclusive start of the half-open payday range.
            payday_before: Exclusive end of the half-open payday range.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPaycheckList

        Example:
            ```python
            payroll = await client.payroll.list_paychecks(
                limit="limit",
            )
            ```
        """
        return await self._get(
            "/v1/paychecks",
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
                        "payroll_ids": payroll_ids,
                        "worker_ids": worker_ids,
                        "worker_types": worker_types,
                        "payroll_types": payroll_types,
                        "statuses": statuses,
                        "payment_methods": payment_methods,
                        "compensation_currencies": compensation_currencies,
                        "pay_frequencies": pay_frequencies,
                        "payday_on_or_after": payday_on_or_after,
                        "payday_before": payday_before,
                    },
                    payroll_list_paychecks_params.PayrollListPaychecksParams,
                ),
            ),
            cast_to=PublicPaycheckList,
        )

    async def get_paycheck(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPaycheckDetail:
        """
        Get a paycheck by id. All worker types use the same paycheck schema. Categories that do not apply to a worker are represented by zero-valued totals and empty line-item arrays. For example, a US 1099 contractor with no applicable payroll taxes returns zero `workerTaxes` and `employerTaxes` totals and an empty `taxes` array. Missing, foreign, unauthorized, or unavailable paychecks return 404.

        Args:
            id: The paycheck ID.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PublicPaycheckDetail

        Example:
            ```python
            payroll = await client.payroll.get_paycheck(
                id="pyc_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/paychecks/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPaycheckDetail,
        )


class PayrollResourceWithRawResponse:
    def __init__(self, payroll: PayrollResource) -> None:
        self._payroll = payroll

        self.list = to_raw_response_wrapper(
            payroll.list,
        )
        self.get = to_raw_response_wrapper(
            payroll.get,
        )
        self.list_paychecks = to_raw_response_wrapper(
            payroll.list_paychecks,
        )
        self.get_paycheck = to_raw_response_wrapper(
            payroll.get_paycheck,
        )


class AsyncPayrollResourceWithRawResponse:
    def __init__(self, payroll: AsyncPayrollResource) -> None:
        self._payroll = payroll

        self.list = async_to_raw_response_wrapper(
            payroll.list,
        )
        self.get = async_to_raw_response_wrapper(
            payroll.get,
        )
        self.list_paychecks = async_to_raw_response_wrapper(
            payroll.list_paychecks,
        )
        self.get_paycheck = async_to_raw_response_wrapper(
            payroll.get_paycheck,
        )


class PayrollResourceWithStreamingResponse:
    def __init__(self, payroll: PayrollResource) -> None:
        self._payroll = payroll

        self.list = to_streamed_response_wrapper(
            payroll.list,
        )
        self.get = to_streamed_response_wrapper(
            payroll.get,
        )
        self.list_paychecks = to_streamed_response_wrapper(
            payroll.list_paychecks,
        )
        self.get_paycheck = to_streamed_response_wrapper(
            payroll.get_paycheck,
        )


class AsyncPayrollResourceWithStreamingResponse:
    def __init__(self, payroll: AsyncPayrollResource) -> None:
        self._payroll = payroll

        self.list = async_to_streamed_response_wrapper(
            payroll.list,
        )
        self.get = async_to_streamed_response_wrapper(
            payroll.get,
        )
        self.list_paychecks = async_to_streamed_response_wrapper(
            payroll.list_paychecks,
        )
        self.get_paycheck = async_to_streamed_response_wrapper(
            payroll.get_paycheck,
        )
