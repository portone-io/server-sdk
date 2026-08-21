from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..common.checkout_payment_method import CheckoutPaymentMethod, _deserialize_checkout_payment_method, _serialize_checkout_payment_method

@dataclass
class EvaluatedCheckoutMethod:
    """결제 수단
    """
    payment_method: CheckoutPaymentMethod
    """결제수단
    """
    channel_key: str
    """채널 키
    """


def _serialize_evaluated_checkout_method(obj: EvaluatedCheckoutMethod) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["paymentMethod"] = _serialize_checkout_payment_method(obj.payment_method)
    entity["channelKey"] = obj.channel_key
    return entity


def _deserialize_evaluated_checkout_method(obj: Any) -> EvaluatedCheckoutMethod:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentMethod" not in obj:
        raise KeyError(f"'paymentMethod' is not in {obj}")
    payment_method = obj["paymentMethod"]
    payment_method = _deserialize_checkout_payment_method(payment_method)
    if "channelKey" not in obj:
        raise KeyError(f"'channelKey' is not in {obj}")
    channel_key = obj["channelKey"]
    if not isinstance(channel_key, str):
        raise ValueError(f"{repr(channel_key)} is not str")
    return EvaluatedCheckoutMethod(payment_method, channel_key)
