from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentMethodType = Union[Literal["CARD", "TRANSFER", "VIRTUAL_ACCOUNT", "GIFT_CERTIFICATE", "MOBILE", "EASY_PAY"], str]


def _serialize_payment_method_type(obj: PaymentMethodType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_method_type(obj: Any) -> PaymentMethodType:
    return obj
