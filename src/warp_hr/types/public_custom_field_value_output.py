# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .text_custom_field_value import TextCustomFieldValue
from .number_custom_field_value import NumberCustomFieldValue
from .date_custom_field_value import DateCustomFieldValue
from .boolean_custom_field_value import BooleanCustomFieldValue
from .currency_custom_field_value import CurrencyCustomFieldValue
from .percentage_custom_field_value import PercentageCustomFieldValue
from .select_custom_field_value import SelectCustomFieldValue
from .multi_select_custom_field_value import MultiSelectCustomFieldValue

__all__ = ["PublicCustomFieldValueOutput"]

PublicCustomFieldValueOutput: TypeAlias = Union[
    TextCustomFieldValue,
    NumberCustomFieldValue,
    DateCustomFieldValue,
    BooleanCustomFieldValue,
    CurrencyCustomFieldValue,
    PercentageCustomFieldValue,
    SelectCustomFieldValue,
    MultiSelectCustomFieldValue,
]
