from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider
from portone_server_sdk._generated.payment.payment_method_easy_pay_method import PaymentMethodEasyPayMethod, _deserialize_payment_method_easy_pay_method, _serialize_payment_method_easy_pay_method

@dataclass
class PaymentMethodEasyPay:
    """간편 결제 상세 정보
    """
    type: Literal["PaymentMethodEasyPay"] = field(repr=False)
    provider: Optional[EasyPayProvider]
    """간편 결제 PG사
    """
    easy_pay_method: Optional[PaymentMethodEasyPayMethod]
    """간편 결제 수단
    """


def _serialize_payment_method_easy_pay(obj: PaymentMethodEasyPay) -> Any:
    entity = {}
    entity["type"] = "PaymentMethodEasyPay"
    if obj.provider is not None:
        entity["provider"] = _serialize_easy_pay_provider(obj.provider)
    if obj.easy_pay_method is not None:
        entity["easyPayMethod"] = _serialize_payment_method_easy_pay_method(obj.easy_pay_method)
    return entity


def _deserialize_payment_method_easy_pay(obj: Any) -> PaymentMethodEasyPay:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodEasyPay":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodEasyPay'")
    if "provider" in obj:
        provider = obj["provider"]
        provider = _deserialize_easy_pay_provider(provider)
    else:
        provider = None
    if "easyPayMethod" in obj:
        easy_pay_method = obj["easyPayMethod"]
        easy_pay_method = _deserialize_payment_method_easy_pay_method(easy_pay_method)
    else:
        easy_pay_method = None
    return PaymentMethodEasyPay(type, provider, easy_pay_method)
