from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.billing_key.instant_billing_key_payment_method_input_card import InstantBillingKeyPaymentMethodInputCard, _deserialize_instant_billing_key_payment_method_input_card, _serialize_instant_billing_key_payment_method_input_card

@dataclass
class InstantBillingKeyPaymentMethodInput:
    """빌링키 발급 시 결제 수단 입력 양식
    """
    card: Optional[InstantBillingKeyPaymentMethodInputCard] = field(default=None)


def _serialize_instant_billing_key_payment_method_input(obj: InstantBillingKeyPaymentMethodInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.card is not None:
        entity["card"] = _serialize_instant_billing_key_payment_method_input_card(obj.card)
    return entity


def _deserialize_instant_billing_key_payment_method_input(obj: Any) -> InstantBillingKeyPaymentMethodInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_instant_billing_key_payment_method_input_card(card)
    else:
        card = None
    return InstantBillingKeyPaymentMethodInput(card)
