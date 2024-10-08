from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyPaymentMethodPaypal:
    """페이팔 정보
    """
    type: Literal["BillingKeyPaymentMethodPaypal"] = field(repr=False)


def _serialize_billing_key_payment_method_paypal(obj: BillingKeyPaymentMethodPaypal) -> Any:
    entity = {}
    entity["type"] = obj.type
    return entity


def _deserialize_billing_key_payment_method_paypal(obj: Any) -> BillingKeyPaymentMethodPaypal:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodPaypal":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodPaypal'")
    return BillingKeyPaymentMethodPaypal(type)
