# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .public_text_worker_custom_field import PublicTextWorkerCustomField
from .public_number_worker_custom_field import PublicNumberWorkerCustomField
from .public_date_worker_custom_field import PublicDateWorkerCustomField
from .public_boolean_worker_custom_field import PublicBooleanWorkerCustomField
from .public_currency_worker_custom_field import PublicCurrencyWorkerCustomField
from .public_percentage_worker_custom_field import PublicPercentageWorkerCustomField
from .public_select_worker_custom_field import PublicSelectWorkerCustomField
from .public_multi_select_worker_custom_field import PublicMultiSelectWorkerCustomField

__all__ = ["PublicWorkerCustomField"]

PublicWorkerCustomField: TypeAlias = Union[
    PublicTextWorkerCustomField,
    PublicNumberWorkerCustomField,
    PublicDateWorkerCustomField,
    PublicBooleanWorkerCustomField,
    PublicCurrencyWorkerCustomField,
    PublicPercentageWorkerCustomField,
    PublicSelectWorkerCustomField,
    PublicMultiSelectWorkerCustomField,
]
