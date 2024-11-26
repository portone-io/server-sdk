from __future__ import annotations
from typing import Any, Literal, Optional, Union

BillingKeyPaymentMethodType = Union[Literal["CARD", "MOBILE", "EASY_PAY", "TRANSFER"], str]
"""빌링키 결제 수단
"""


def _serialize_billing_key_payment_method_type(obj: BillingKeyPaymentMethodType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_billing_key_payment_method_type(obj: Any) -> BillingKeyPaymentMethodType:
    return obj
