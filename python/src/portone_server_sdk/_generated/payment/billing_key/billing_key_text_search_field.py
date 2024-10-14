from __future__ import annotations
from typing import Any, Literal, Optional

BillingKeyTextSearchField = Literal["CARD_BIN", "CARD_NUMBER", "PG_MERCHANT_ID", "CUSTOMER_NAME", "CUSTOMER_EMAIL", "CUSTOMER_PHONE_NUMBER", "CUSTOMER_ADDRESS", "CUSTOMER_ZIPCODE", "USER_AGENT", "BILLING_KEY", "CHANNEL_GROUP_NAME"]
"""통합검색 항목
"""


def _serialize_billing_key_text_search_field(obj: BillingKeyTextSearchField) -> Any:
    return obj


def _deserialize_billing_key_text_search_field(obj: Any) -> BillingKeyTextSearchField:
    if obj not in ["CARD_BIN", "CARD_NUMBER", "PG_MERCHANT_ID", "CUSTOMER_NAME", "CUSTOMER_EMAIL", "CUSTOMER_PHONE_NUMBER", "CUSTOMER_ADDRESS", "CUSTOMER_ZIPCODE", "USER_AGENT", "BILLING_KEY", "CHANNEL_GROUP_NAME"]:
        raise ValueError(f"{repr(obj)} is not BillingKeyTextSearchField")
    return obj
