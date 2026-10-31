# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo

from .time_off_request_created_webhook_event import TimeOffRequestCreatedWebhookEvent
from .time_off_request_reviewed_webhook_event import TimeOffRequestReviewedWebhookEvent
from .time_off_request_deleted_webhook_event import TimeOffRequestDeletedWebhookEvent
from .time_off_balance_adjusted_webhook_event import TimeOffBalanceAdjustedWebhookEvent
from .worker_created_webhook_event import WorkerCreatedWebhookEvent
from .worker_updated_webhook_event import WorkerUpdatedWebhookEvent
from .worker_deleted_webhook_event import WorkerDeletedWebhookEvent
from .worker_invite_sent_webhook_event import WorkerInviteSentWebhookEvent
from .worker_invite_accepted_webhook_event import WorkerInviteAcceptedWebhookEvent
from .worker_onboarding_completed_webhook_event import WorkerOnboardingCompletedWebhookEvent
from .worker_offboarding_started_webhook_event import WorkerOffboardingStartedWebhookEvent
from .worker_offboarded_webhook_event import WorkerOffboardedWebhookEvent
from .worker_reactivated_webhook_event import WorkerReactivatedWebhookEvent
from .offer_created_webhook_event import OfferCreatedWebhookEvent
from .offer_signature_requested_webhook_event import OfferSignatureRequestedWebhookEvent
from .offer_sent_webhook_event import OfferSentWebhookEvent
from .offer_viewed_webhook_event import OfferViewedWebhookEvent
from .offer_accepted_webhook_event import OfferAcceptedWebhookEvent
from .offer_voided_webhook_event import OfferVoidedWebhookEvent
from .offer_expired_webhook_event import OfferExpiredWebhookEvent
from .pay_rate_created_webhook_event import PayRateCreatedWebhookEvent
from .pay_rate_deleted_webhook_event import PayRateDeletedWebhookEvent

__all__ = ["ParsedWebhookEvent"]


ParsedWebhookEvent: TypeAlias = Annotated[
    Union[
        TimeOffRequestCreatedWebhookEvent,
        TimeOffRequestReviewedWebhookEvent,
        TimeOffRequestDeletedWebhookEvent,
        TimeOffBalanceAdjustedWebhookEvent,
        WorkerCreatedWebhookEvent,
        WorkerUpdatedWebhookEvent,
        WorkerDeletedWebhookEvent,
        WorkerInviteSentWebhookEvent,
        WorkerInviteAcceptedWebhookEvent,
        WorkerOnboardingCompletedWebhookEvent,
        WorkerOffboardingStartedWebhookEvent,
        WorkerOffboardedWebhookEvent,
        WorkerReactivatedWebhookEvent,
        OfferCreatedWebhookEvent,
        OfferSignatureRequestedWebhookEvent,
        OfferSentWebhookEvent,
        OfferViewedWebhookEvent,
        OfferAcceptedWebhookEvent,
        OfferVoidedWebhookEvent,
        OfferExpiredWebhookEvent,
        PayRateCreatedWebhookEvent,
        PayRateDeletedWebhookEvent,
    ],
    PropertyInfo(discriminator="type"),
]
