from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.card import Card, _deserialize_card, _serialize_card

@dataclass
class BillingKeyPaymentMethodCard:
    """카드 정보
    """
    type: Literal["BillingKeyPaymentMethodCard"] = field(repr=False)
    card: Optional[Card]
    """카드 상세 정보
    """


def _serialize_billing_key_payment_method_card(obj: BillingKeyPaymentMethodCard) -> Any:
    entity = {}
    entity["type"] = "BillingKeyPaymentMethodCard"
    if obj.card is not None:
        entity["card"] = _serialize_card(obj.card)
    return entity


def _deserialize_billing_key_payment_method_card(obj: Any) -> BillingKeyPaymentMethodCard:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BillingKeyPaymentMethodCard":
        raise ValueError(f"{repr(type)} is not 'BillingKeyPaymentMethodCard'")
    if "card" in obj:
        card = obj["card"]
        card = _deserialize_card(card)
    else:
        card = None
    return BillingKeyPaymentMethodCard(type, card)
