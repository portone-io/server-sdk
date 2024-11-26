from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.easy_pay_method_type import EasyPayMethodType, _deserialize_easy_pay_method_type, _serialize_easy_pay_method_type
from ...common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider

@dataclass
class PlatformPaymentMethodEasyPay:
    """간편 결제
    """
    provider: Optional[EasyPayProvider] = field(default=None)
    """간편 결제사
    """
    method_type: Optional[EasyPayMethodType] = field(default=None)
    """간편 결제 수단
    """


def _serialize_platform_payment_method_easy_pay(obj: PlatformPaymentMethodEasyPay) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "EASY_PAY"
    if obj.provider is not None:
        entity["provider"] = _serialize_easy_pay_provider(obj.provider)
    if obj.method_type is not None:
        entity["methodType"] = _serialize_easy_pay_method_type(obj.method_type)
    return entity


def _deserialize_platform_payment_method_easy_pay(obj: Any) -> PlatformPaymentMethodEasyPay:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "EASY_PAY":
        raise ValueError(f"{repr(type)} is not 'EASY_PAY'")
    if "provider" in obj:
        provider = obj["provider"]
        provider = _deserialize_easy_pay_provider(provider)
    else:
        provider = None
    if "methodType" in obj:
        method_type = obj["methodType"]
        method_type = _deserialize_easy_pay_method_type(method_type)
    else:
        method_type = None
    return PlatformPaymentMethodEasyPay(provider, method_type)
