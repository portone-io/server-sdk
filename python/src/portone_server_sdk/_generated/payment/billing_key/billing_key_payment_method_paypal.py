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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodPaypal":
        raise ValueError("Expected 'BillingKeyPaymentMethodPaypal' for type")
    return BillingKeyPaymentMethodPaypal()
