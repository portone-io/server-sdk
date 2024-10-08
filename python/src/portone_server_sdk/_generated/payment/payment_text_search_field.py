from __future__ import annotations
from typing import Any, Literal, Optional

PaymentTextSearchField = Literal["ALL", "PAYMENT_ID", "TX_ID", "SCHEDULE_ID", "FAIL_REASON", "CARD_ISSUER", "CARD_ACQUIRER", "CARD_BIN", "CARD_NUMBER", "CARD_APPROVAL_NUMBER", "CARD_RECEIPT_NAME", "CARD_INSTALLMENT", "TRANS_BANK", "VIRTUAL_ACCOUNT_HOLDER_NAME", "VIRTUAL_ACCOUNT_BANK", "VIRTUAL_ACCOUNT_NUMBER", "PG_MERCHANT_ID", "PG_TX_ID", "PG_RECEIPT_ID", "RECEIPT_APPROVAL_NUMBER", "PG_CANCELLATION_ID", "CANCEL_REASON", "ORDER_NAME", "CUSTOMER_NAME", "CUSTOMER_EMAIL", "CUSTOMER_PHONE_NUMBER", "CUSTOMER_ADDRESS", "CUSTOMER_ZIPCODE", "USER_AGENT", "BILLING_KEY", "PROMOTION_ID", "GIFT_CERTIFICATION_APPROVAL_NUMBER"]
"""통합검색 항목
"""


def _serialize_payment_text_search_field(obj: PaymentTextSearchField) -> Any:
    return obj


def _deserialize_payment_text_search_field(obj: Any) -> PaymentTextSearchField:
    if obj not in ["ALL", "PAYMENT_ID", "TX_ID", "SCHEDULE_ID", "FAIL_REASON", "CARD_ISSUER", "CARD_ACQUIRER", "CARD_BIN", "CARD_NUMBER", "CARD_APPROVAL_NUMBER", "CARD_RECEIPT_NAME", "CARD_INSTALLMENT", "TRANS_BANK", "VIRTUAL_ACCOUNT_HOLDER_NAME", "VIRTUAL_ACCOUNT_BANK", "VIRTUAL_ACCOUNT_NUMBER", "PG_MERCHANT_ID", "PG_TX_ID", "PG_RECEIPT_ID", "RECEIPT_APPROVAL_NUMBER", "PG_CANCELLATION_ID", "CANCEL_REASON", "ORDER_NAME", "CUSTOMER_NAME", "CUSTOMER_EMAIL", "CUSTOMER_PHONE_NUMBER", "CUSTOMER_ADDRESS", "CUSTOMER_ZIPCODE", "USER_AGENT", "BILLING_KEY", "PROMOTION_ID", "GIFT_CERTIFICATION_APPROVAL_NUMBER"]:
        raise ValueError(f"{repr(obj)} is not PaymentTextSearchField")
    return obj
