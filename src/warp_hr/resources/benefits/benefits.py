# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .health_plans import (
    HealthPlansResource,
    AsyncHealthPlansResource,
    HealthPlansResourceWithRawResponse,
    AsyncHealthPlansResourceWithRawResponse,
    HealthPlansResourceWithStreamingResponse,
    AsyncHealthPlansResourceWithStreamingResponse,
)
from .retirement_plans import (
    RetirementPlansResource,
    AsyncRetirementPlansResource,
    RetirementPlansResourceWithRawResponse,
    AsyncRetirementPlansResourceWithRawResponse,
    RetirementPlansResourceWithStreamingResponse,
    AsyncRetirementPlansResourceWithStreamingResponse,
)
from .deductions import (
    DeductionsResource,
    AsyncDeductionsResource,
    DeductionsResourceWithRawResponse,
    AsyncDeductionsResourceWithRawResponse,
    DeductionsResourceWithStreamingResponse,
    AsyncDeductionsResourceWithStreamingResponse,
)

__all__ = ["BenefitsResource", "AsyncBenefitsResource"]


class BenefitsResource(SyncAPIResource):
    @cached_property
    def health_plans(self) -> HealthPlansResource:
        return HealthPlansResource(self._client)

    @cached_property
    def retirement_plans(self) -> RetirementPlansResource:
        return RetirementPlansResource(self._client)

    @cached_property
    def deductions(self) -> DeductionsResource:
        return DeductionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BenefitsResourceWithRawResponse:
        return BenefitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenefitsResourceWithStreamingResponse:
        return BenefitsResourceWithStreamingResponse(self)


class AsyncBenefitsResource(AsyncAPIResource):
    @cached_property
    def health_plans(self) -> AsyncHealthPlansResource:
        return AsyncHealthPlansResource(self._client)

    @cached_property
    def retirement_plans(self) -> AsyncRetirementPlansResource:
        return AsyncRetirementPlansResource(self._client)

    @cached_property
    def deductions(self) -> AsyncDeductionsResource:
        return AsyncDeductionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBenefitsResourceWithRawResponse:
        return AsyncBenefitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenefitsResourceWithStreamingResponse:
        return AsyncBenefitsResourceWithStreamingResponse(self)


class BenefitsResourceWithRawResponse:
    def __init__(self, benefits: BenefitsResource) -> None:
        self._benefits = benefits

    @cached_property
    def health_plans(self) -> HealthPlansResourceWithRawResponse:
        return HealthPlansResourceWithRawResponse(self._benefits.health_plans)

    @cached_property
    def retirement_plans(self) -> RetirementPlansResourceWithRawResponse:
        return RetirementPlansResourceWithRawResponse(self._benefits.retirement_plans)

    @cached_property
    def deductions(self) -> DeductionsResourceWithRawResponse:
        return DeductionsResourceWithRawResponse(self._benefits.deductions)


class AsyncBenefitsResourceWithRawResponse:
    def __init__(self, benefits: AsyncBenefitsResource) -> None:
        self._benefits = benefits

    @cached_property
    def health_plans(self) -> AsyncHealthPlansResourceWithRawResponse:
        return AsyncHealthPlansResourceWithRawResponse(self._benefits.health_plans)

    @cached_property
    def retirement_plans(self) -> AsyncRetirementPlansResourceWithRawResponse:
        return AsyncRetirementPlansResourceWithRawResponse(self._benefits.retirement_plans)

    @cached_property
    def deductions(self) -> AsyncDeductionsResourceWithRawResponse:
        return AsyncDeductionsResourceWithRawResponse(self._benefits.deductions)


class BenefitsResourceWithStreamingResponse:
    def __init__(self, benefits: BenefitsResource) -> None:
        self._benefits = benefits

    @cached_property
    def health_plans(self) -> HealthPlansResourceWithStreamingResponse:
        return HealthPlansResourceWithStreamingResponse(self._benefits.health_plans)

    @cached_property
    def retirement_plans(self) -> RetirementPlansResourceWithStreamingResponse:
        return RetirementPlansResourceWithStreamingResponse(self._benefits.retirement_plans)

    @cached_property
    def deductions(self) -> DeductionsResourceWithStreamingResponse:
        return DeductionsResourceWithStreamingResponse(self._benefits.deductions)


class AsyncBenefitsResourceWithStreamingResponse:
    def __init__(self, benefits: AsyncBenefitsResource) -> None:
        self._benefits = benefits

    @cached_property
    def health_plans(self) -> AsyncHealthPlansResourceWithStreamingResponse:
        return AsyncHealthPlansResourceWithStreamingResponse(self._benefits.health_plans)

    @cached_property
    def retirement_plans(self) -> AsyncRetirementPlansResourceWithStreamingResponse:
        return AsyncRetirementPlansResourceWithStreamingResponse(self._benefits.retirement_plans)

    @cached_property
    def deductions(self) -> AsyncDeductionsResourceWithStreamingResponse:
        return AsyncDeductionsResourceWithStreamingResponse(self._benefits.deductions)
