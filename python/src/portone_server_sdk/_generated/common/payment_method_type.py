from __future__ import annotations
from typing import Any, Literal, Optional

PaymentMethodType = Literal["CARD", "TRANSFER", "VIRTUAL_ACCOUNT", "GIFT_CERTIFICATE", "MOBILE", "EASY_PAY"]


def _serialize_payment_method_type(obj: PaymentMethodType) -> Any:
    return obj


def _deserialize_payment_method_type(obj: Any) -> PaymentMethodType:
    if obj not in ["CARD", "TRANSFER", "VIRTUAL_ACCOUNT", "GIFT_CERTIFICATE", "MOBILE", "EASY_PAY"]:
        raise ValueError(f"{repr(obj)} is not PaymentMethodType")
    return obj
