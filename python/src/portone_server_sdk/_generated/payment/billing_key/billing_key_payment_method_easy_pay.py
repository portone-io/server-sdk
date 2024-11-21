from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.billing_key.billing_key_payment_method_easy_pay_method import BillingKeyPaymentMethodEasyPayMethod, _deserialize_billing_key_payment_method_easy_pay_method, _serialize_billing_key_payment_method_easy_pay_method
from ...common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider

@dataclass
class BillingKeyPaymentMethodEasyPay:
    """간편 결제 정보
    """
    provider: Optional[EasyPayProvider] = field(default=None)
    """간편 결제 PG사
    """
    method: Optional[BillingKeyPaymentMethodEasyPayMethod] = field(default=None)
    """간편 결제 수단
    """


def _serialize_billing_key_payment_method_easy_pay(obj: BillingKeyPaymentMethodEasyPay) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodEasyPay"
    if obj.provider is not None:
        entity["provider"] = _serialize_easy_pay_provider(obj.provider)
    if obj.method is not None:
        entity["method"] = _serialize_billing_key_payment_method_easy_pay_method(obj.method)
    return entity


def _deserialize_billing_key_payment_method_easy_pay(obj: Any) -> BillingKeyPaymentMethodEasyPay:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodEasyPay":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodEasyPay'")
    if "provider" in obj:
        provider = obj["provider"]
        provider = _deserialize_easy_pay_provider(provider)
    else:
        provider = None
    if "method" in obj:
        method = obj["method"]
        method = _deserialize_billing_key_payment_method_easy_pay_method(method)
    else:
        method = None
    return BillingKeyPaymentMethodEasyPay(provider, method)
