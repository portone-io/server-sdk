from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...common.card import Card, _deserialize_card, _serialize_card

@dataclass
class BillingKeyPaymentMethodCard:
    """카드 정보
    """
    card: Optional[Card] = field(default=None)
    """카드 상세 정보
    """


def _serialize_billing_key_payment_method_card(obj: BillingKeyPaymentMethodCard) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodCard"
    if obj.card is not None:
        entity["card"] = _serialize_card(obj.card)
    return entity


def _deserialize_billing_key_payment_method_card(obj: Any) -> BillingKeyPaymentMethodCard:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodCard":
        raise ValueError("Expected 'BillingKeyPaymentMethodCard' for type")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_card(card)
    else:
        card = None
    return BillingKeyPaymentMethodCard(card)
