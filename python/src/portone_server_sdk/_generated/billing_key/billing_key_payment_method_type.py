from __future__ import annotations
from typing import Any, Literal, Optional

BillingKeyPaymentMethodType = Literal["CARD", "MOBILE", "EASY_PAY", "TRANSFER"]
"""빌링키 결제 수단
"""


def _serialize_billing_key_payment_method_type(obj: BillingKeyPaymentMethodType) -> Any:
    return obj


def _deserialize_billing_key_payment_method_type(obj: Any) -> BillingKeyPaymentMethodType:
    if obj not in ["CARD", "MOBILE", "EASY_PAY", "TRANSFER"]:
        raise ValueError(f"{repr(obj)} is not BillingKeyPaymentMethodType")
    return obj
