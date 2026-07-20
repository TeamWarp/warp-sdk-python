# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Iterable, Optional, Union
from typing_extensions import Literal

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
from ..types.worker_list_response import WorkerListResponse, Data, Department
from ..types import worker_list_params, worker_create_employee_params, worker_create_contractor_params
from ..types.worker_retrieve_response import WorkerRetrieveResponse, Department
from ..types.worker_create_employee_response import WorkerCreateEmployeeResponse, Department
from ..types.worker_create_contractor_response import WorkerCreateContractorResponse, Department
from ..types.worker_invite_response import WorkerInviteResponse, Department

__all__ = ["WorkersResource", "AsyncWorkersResource"]


class WorkersResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> WorkersResourceWithRawResponse:
        return WorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersResourceWithStreamingResponse:
        return WorkersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        statuses: Iterable[Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]] | Omit = omit,
        types: Iterable[Literal["employee", "contractor"]] | Omit = omit,
        work_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerListResponse:
        """
        List all workers. Workers include anyone employed by the company, whether US or international, full-time employees or contractors.
        
        Args:
            limit: a number less than or equal to 100
            after_id: The id of the worker.
            before_id: The id of the worker.
            statuses: Query parameter.
            types: Query parameter.
            work_email: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerListResponse: Success
        
        Example:
            ```python
            worker = client.workers.list()
            ```
        """
        return self._get(
            "/v1/workers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "statuses": statuses, "types": types, "work_email": work_email}, worker_list_params.WorkerListParams)),
            cast_to=WorkerListResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerRetrieveResponse:
        """
        Get a specific worker by id.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerRetrieveResponse: Success
        
        Example:
            ```python
            worker = client.workers.retrieve(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/workers/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerRetrieveResponse,
        )

    def delete(
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
        Delete a worker. Only workers who have not yet completed onboarding can be deleted. Active workers must be properly offboarded.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Success
        
        Example:
            ```python
            client.workers.delete(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/workers/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_employee(
        self,
        *,
        first_name: str,
        last_name: str,
        position: str,
        start_date: str,
        email: str,
        work_email: Optional[str] | Omit = omit,
        require_i9: bool | Omit = omit,
        state_registration: Literal["self_managed", "warp_managed"] | Omit = omit,
        department_id: str,
        manager_id: str,
        stock_options: Optional[float] | Omit = omit,
        work_location: Union[worker_create_employee_params.WorkLocation, worker_create_employee_params.WorkLocation2],
        compensation: worker_create_employee_params.Compensation,
        pay_schedule: Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerCreateEmployeeResponse:
        """
        Create a new US employee. The worker will be created in draft status and must be invited separately via the invite endpoint. If hiring in a state without an existing tax registration, you must specify the stateRegistration field.
        
        Args:
            first_name: a non empty string
            last_name: a non empty string
            position: The employee's job title.
            start_date: A date string in the form YYYY-MM-DD
            email: Personal email address. The invite will be sent here.
            work_email: Company-issued email address, if applicable.
            require_i9: Whether the employee is required to complete I-9 work authorization. Set to false if the employee has already been verified off-platform. Defaults to true.
            state_registration: How state tax registration is handled for this employee's work state. Required when hiring in a state where your company doesn't have an existing registration. Use 'self_managed' if you've already registered in this state, or 'warp_managed' for Warp to handle registration on your behalf.
            department_id: The department to assign this employee to.
            manager_id: The worker id of this employee's direct manager.
            stock_options: Number of stock options granted to this employee.
            work_location: Where the employee will work. Either an existing company workplace or a remote US state.
            compensation: The employee's base compensation.
            pay_schedule: The employee's pay schedule. Must be a pay schedule that the company has configured.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerCreateEmployeeResponse: Success
        
        Example:
            ```python
            worker = client.workers.create_employee(
                first_name="",
                last_name="",
                position="",
                start_date="2000-01-01",
                email="john@joinwarp.com",
                department_id="dpt_1234",
                manager_id="wrk_1234",
                work_location={"type": "office", "workplace_id": "wkp_1234"},
                compensation={"amount": 0, "per": "hour"},
            )
            ```
        """
        return self._post(
            "/v1/workers/employee",
            body=maybe_transform(
            {
            "first_name": first_name,
            "last_name": last_name,
            "position": position,
            "start_date": start_date,
            "email": email,
            "work_email": work_email,
            "require_i9": require_i9,
            "state_registration": state_registration,
            "department_id": department_id,
            "manager_id": manager_id,
            "stock_options": stock_options,
            "work_location": work_location,
            "compensation": compensation,
            "pay_schedule": pay_schedule,
        },
            worker_create_employee_params.WorkerCreateEmployeeParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerCreateEmployeeResponse,
        )

    def create_contractor(
        self,
        *,
        entity_type: Literal["individual", "business"],
        first_name: str,
        last_name: str,
        position: str,
        business_name: str | Omit = omit,
        scope_of_work: Optional[str] | Omit = omit,
        start_date: str,
        email: str,
        work_email: Optional[str] | Omit = omit,
        department_id: str,
        manager_id: str,
        work_country: Literal["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "ZA", "ZM", "ZW"],
        compensation: Optional[worker_create_contractor_params.Compensation] | Omit = omit,
        pay_schedule: Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerCreateContractorResponse:
        """
        Create a new contractor. The worker will be created in draft status and must be invited separately via the invite endpoint. For business contractors, the businessName field is required.
        
        Args:
            entity_type: Whether the contractor is an individual person or a business entity.
            first_name: a non empty string
            last_name: a non empty string
            position: The contractor's role or job title.
            business_name: Required when entityType is "business". The legal name of the contractor's business.
            scope_of_work: A description of the work the contractor will perform.
            start_date: A date string in the form YYYY-MM-DD
            email: Personal email address. The invite will be sent here.
            work_email: Company-issued email address, if applicable.
            department_id: The department to assign this contractor to.
            manager_id: The worker id of this contractor's direct manager.
            work_country: Body parameter.
            compensation: The contractor's pay rate. Omit if you'd like to pay on-demand or via invoicing.
            pay_schedule: The contractor's pay schedule. Must be a pay schedule that the company has configured.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerCreateContractorResponse: Success
        
        Example:
            ```python
            worker = client.workers.create_contractor(
                entity_type="individual",
                first_name="",
                last_name="",
                position="",
                start_date="2000-01-01",
                email="john@joinwarp.com",
                department_id="dpt_1234",
                manager_id="wrk_1234",
                work_country="AD",
            )
            ```
        """
        return self._post(
            "/v1/workers/contractor",
            body=maybe_transform(
            {
            "entity_type": entity_type,
            "first_name": first_name,
            "last_name": last_name,
            "position": position,
            "business_name": business_name,
            "scope_of_work": scope_of_work,
            "start_date": start_date,
            "email": email,
            "work_email": work_email,
            "department_id": department_id,
            "manager_id": manager_id,
            "work_country": work_country,
            "compensation": compensation,
            "pay_schedule": pay_schedule,
        },
            worker_create_contractor_params.WorkerCreateContractorParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerCreateContractorResponse,
        )

    def invite(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerInviteResponse:
        """
        Send or resend the worker invite so they can accept and complete onboarding to Warp. If the worker has already been invited, the invite will be resent with extended validity.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerInviteResponse: Success
        
        Example:
            ```python
            worker = client.workers.invite(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/workers/{id}/invite", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerInviteResponse,
        )


class AsyncWorkersResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncWorkersResourceWithRawResponse:
        return AsyncWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersResourceWithStreamingResponse:
        return AsyncWorkersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: str | Omit = omit,
        after_id: str | Omit = omit,
        before_id: str | Omit = omit,
        statuses: Iterable[Literal["draft", "invited", "onboarding", "active", "offboarding", "inactive"]] | Omit = omit,
        types: Iterable[Literal["employee", "contractor"]] | Omit = omit,
        work_email: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerListResponse:
        """
        List all workers. Workers include anyone employed by the company, whether US or international, full-time employees or contractors.
        
        Args:
            limit: a number less than or equal to 100
            after_id: The id of the worker.
            before_id: The id of the worker.
            statuses: Query parameter.
            types: Query parameter.
            work_email: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerListResponse: Success
        
        Example:
            ```python
            worker = await client.workers.list()
            ```
        """
        return await self._get(
            "/v1/workers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({"limit": limit, "after_id": after_id, "before_id": before_id, "statuses": statuses, "types": types, "work_email": work_email}, worker_list_params.WorkerListParams)),
            cast_to=WorkerListResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerRetrieveResponse:
        """
        Get a specific worker by id.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerRetrieveResponse: Success
        
        Example:
            ```python
            worker = await client.workers.retrieve(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/workers/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerRetrieveResponse,
        )

    async def delete(
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
        Delete a worker. Only workers who have not yet completed onboarding can be deleted. Active workers must be properly offboarded.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            Success
        
        Example:
            ```python
            await client.workers.delete(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/workers/{id}", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_employee(
        self,
        *,
        first_name: str,
        last_name: str,
        position: str,
        start_date: str,
        email: str,
        work_email: Optional[str] | Omit = omit,
        require_i9: bool | Omit = omit,
        state_registration: Literal["self_managed", "warp_managed"] | Omit = omit,
        department_id: str,
        manager_id: str,
        stock_options: Optional[float] | Omit = omit,
        work_location: Union[worker_create_employee_params.WorkLocation, worker_create_employee_params.WorkLocation2],
        compensation: worker_create_employee_params.Compensation,
        pay_schedule: Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerCreateEmployeeResponse:
        """
        Create a new US employee. The worker will be created in draft status and must be invited separately via the invite endpoint. If hiring in a state without an existing tax registration, you must specify the stateRegistration field.
        
        Args:
            first_name: a non empty string
            last_name: a non empty string
            position: The employee's job title.
            start_date: A date string in the form YYYY-MM-DD
            email: Personal email address. The invite will be sent here.
            work_email: Company-issued email address, if applicable.
            require_i9: Whether the employee is required to complete I-9 work authorization. Set to false if the employee has already been verified off-platform. Defaults to true.
            state_registration: How state tax registration is handled for this employee's work state. Required when hiring in a state where your company doesn't have an existing registration. Use 'self_managed' if you've already registered in this state, or 'warp_managed' for Warp to handle registration on your behalf.
            department_id: The department to assign this employee to.
            manager_id: The worker id of this employee's direct manager.
            stock_options: Number of stock options granted to this employee.
            work_location: Where the employee will work. Either an existing company workplace or a remote US state.
            compensation: The employee's base compensation.
            pay_schedule: The employee's pay schedule. Must be a pay schedule that the company has configured.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerCreateEmployeeResponse: Success
        
        Example:
            ```python
            worker = await client.workers.create_employee(
                first_name="",
                last_name="",
                position="",
                start_date="2000-01-01",
                email="john@joinwarp.com",
                department_id="dpt_1234",
                manager_id="wrk_1234",
                work_location={"type": "office", "workplace_id": "wkp_1234"},
                compensation={"amount": 0, "per": "hour"},
            )
            ```
        """
        return await self._post(
            "/v1/workers/employee",
            body=await async_maybe_transform(
            {
            "first_name": first_name,
            "last_name": last_name,
            "position": position,
            "start_date": start_date,
            "email": email,
            "work_email": work_email,
            "require_i9": require_i9,
            "state_registration": state_registration,
            "department_id": department_id,
            "manager_id": manager_id,
            "stock_options": stock_options,
            "work_location": work_location,
            "compensation": compensation,
            "pay_schedule": pay_schedule,
        },
            worker_create_employee_params.WorkerCreateEmployeeParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerCreateEmployeeResponse,
        )

    async def create_contractor(
        self,
        *,
        entity_type: Literal["individual", "business"],
        first_name: str,
        last_name: str,
        position: str,
        business_name: str | Omit = omit,
        scope_of_work: Optional[str] | Omit = omit,
        start_date: str,
        email: str,
        work_email: Optional[str] | Omit = omit,
        department_id: str,
        manager_id: str,
        work_country: Literal["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "XK", "YE", "YT", "ZA", "ZM", "ZW"],
        compensation: Optional[worker_create_contractor_params.Compensation] | Omit = omit,
        pay_schedule: Optional[Literal["weekly", "biweekly", "monthly", "semimonthly", "quarterly", "annually"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerCreateContractorResponse:
        """
        Create a new contractor. The worker will be created in draft status and must be invited separately via the invite endpoint. For business contractors, the businessName field is required.
        
        Args:
            entity_type: Whether the contractor is an individual person or a business entity.
            first_name: a non empty string
            last_name: a non empty string
            position: The contractor's role or job title.
            business_name: Required when entityType is "business". The legal name of the contractor's business.
            scope_of_work: A description of the work the contractor will perform.
            start_date: A date string in the form YYYY-MM-DD
            email: Personal email address. The invite will be sent here.
            work_email: Company-issued email address, if applicable.
            department_id: The department to assign this contractor to.
            manager_id: The worker id of this contractor's direct manager.
            work_country: Body parameter.
            compensation: The contractor's pay rate. Omit if you'd like to pay on-demand or via invoicing.
            pay_schedule: The contractor's pay schedule. Must be a pay schedule that the company has configured.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerCreateContractorResponse: Success
        
        Example:
            ```python
            worker = await client.workers.create_contractor(
                entity_type="individual",
                first_name="",
                last_name="",
                position="",
                start_date="2000-01-01",
                email="john@joinwarp.com",
                department_id="dpt_1234",
                manager_id="wrk_1234",
                work_country="AD",
            )
            ```
        """
        return await self._post(
            "/v1/workers/contractor",
            body=await async_maybe_transform(
            {
            "entity_type": entity_type,
            "first_name": first_name,
            "last_name": last_name,
            "position": position,
            "business_name": business_name,
            "scope_of_work": scope_of_work,
            "start_date": start_date,
            "email": email,
            "work_email": work_email,
            "department_id": department_id,
            "manager_id": manager_id,
            "work_country": work_country,
            "compensation": compensation,
            "pay_schedule": pay_schedule,
        },
            worker_create_contractor_params.WorkerCreateContractorParams,
        ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerCreateContractorResponse,
        )

    async def invite(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerInviteResponse:
        """
        Send or resend the worker invite so they can accept and complete onboarding to Warp. If the worker has already been invited, the invite will be resent with extended validity.
        
        Args:
            id: The id of the worker.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
        
        Returns:
            WorkerInviteResponse: Success
        
        Example:
            ```python
            worker = await client.workers.invite(
                id="wrk_1234",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/workers/{id}/invite", **{"id": id}),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkerInviteResponse,
        )


class WorkersResourceWithRawResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.list = to_raw_response_wrapper(
            workers.list,
        )
        self.retrieve = to_raw_response_wrapper(
            workers.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            workers.delete,
        )
        self.create_employee = to_raw_response_wrapper(
            workers.create_employee,
        )
        self.create_contractor = to_raw_response_wrapper(
            workers.create_contractor,
        )
        self.invite = to_raw_response_wrapper(
            workers.invite,
        )


class AsyncWorkersResourceWithRawResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.list = async_to_raw_response_wrapper(
            workers.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workers.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            workers.delete,
        )
        self.create_employee = async_to_raw_response_wrapper(
            workers.create_employee,
        )
        self.create_contractor = async_to_raw_response_wrapper(
            workers.create_contractor,
        )
        self.invite = async_to_raw_response_wrapper(
            workers.invite,
        )


class WorkersResourceWithStreamingResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.list = to_streamed_response_wrapper(
            workers.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            workers.delete,
        )
        self.create_employee = to_streamed_response_wrapper(
            workers.create_employee,
        )
        self.create_contractor = to_streamed_response_wrapper(
            workers.create_contractor,
        )
        self.invite = to_streamed_response_wrapper(
            workers.invite,
        )


class AsyncWorkersResourceWithStreamingResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.list = async_to_streamed_response_wrapper(
            workers.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            workers.delete,
        )
        self.create_employee = async_to_streamed_response_wrapper(
            workers.create_employee,
        )
        self.create_contractor = async_to_streamed_response_wrapper(
            workers.create_contractor,
        )
        self.invite = async_to_streamed_response_wrapper(
            workers.invite,
        )
