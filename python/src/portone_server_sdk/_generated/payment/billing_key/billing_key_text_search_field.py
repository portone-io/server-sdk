from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeyTextSearchField = Union[Literal["CARD_BIN", "CARD_NUMBER", "PG_MERCHANT_ID", "CUSTOMER_NAME", "CUSTOMER_EMAIL", "CUSTOMER_PHONE_NUMBER", "CUSTOMER_ADDRESS", "CUSTOMER_ZIPCODE", "USER_AGENT", "BILLING_KEY", "CHANNEL_GROUP_NAME"], str]
"""통합검색 항목
"""


def _serialize_billing_key_text_search_field(obj: BillingKeyTextSearchField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_text_search_field(obj: Any) -> BillingKeyTextSearchField:
    return obj
