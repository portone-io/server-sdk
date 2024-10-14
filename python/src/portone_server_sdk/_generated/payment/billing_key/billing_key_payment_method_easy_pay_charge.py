from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyPaymentMethodEasyPayCharge:
    """충전식 포인트 결제 정보
    """
    type: Literal["BillingKeyPaymentMethodEasyPayCharge"] = field(repr=False)


def _serialize_billing_key_payment_method_easy_pay_charge(obj: BillingKeyPaymentMethodEasyPayCharge) -> Any:
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodEasyPayCharge"
    return entity


def _deserialize_billing_key_payment_method_easy_pay_charge(obj: Any) -> BillingKeyPaymentMethodEasyPayCharge:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodEasyPayCharge":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodEasyPayCharge'")
    return BillingKeyPaymentMethodEasyPayCharge(type)
