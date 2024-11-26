from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.transfer.easy_pay_method_type import EasyPayMethodType, _deserialize_easy_pay_method_type, _serialize_easy_pay_method_type
from ...common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider

@dataclass
class PlatformPaymentMethodEasyPayInput:
    """간편 결제 입력 정보
    """
    provider: Optional[EasyPayProvider] = field(default=None)
    """간편 결제사
    """
    method_type: Optional[EasyPayMethodType] = field(default=None)
    """간편 결제 수단
    """


def _serialize_platform_payment_method_easy_pay_input(obj: PlatformPaymentMethodEasyPayInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.provider is not None:
        entity["provider"] = _serialize_easy_pay_provider(obj.provider)
    if obj.method_type is not None:
        entity["methodType"] = _serialize_easy_pay_method_type(obj.method_type)
    return entity


def _deserialize_platform_payment_method_easy_pay_input(obj: Any) -> PlatformPaymentMethodEasyPayInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
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
    return PlatformPaymentMethodEasyPayInput(provider, method_type)
