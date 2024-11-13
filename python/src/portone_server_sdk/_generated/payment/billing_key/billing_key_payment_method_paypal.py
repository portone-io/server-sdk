from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyPaymentMethodPaypal:
    """페이팔 정보
    """
    pass


def _serialize_billing_key_payment_method_paypal(obj: BillingKeyPaymentMethodPaypal) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodPaypal"
    return entity


def _deserialize_billing_key_payment_method_paypal(obj: Any) -> BillingKeyPaymentMethodPaypal:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodPaypal":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodPaypal'")
    return BillingKeyPaymentMethodPaypal()
