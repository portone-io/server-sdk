from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodCard:
    """카드
    """
    type: Literal["CARD"] = field(repr=False)


def _serialize_platform_payment_method_card(obj: PlatformPaymentMethodCard) -> Any:
    entity = {}
    entity["type"] = "CARD"
    return entity


def _deserialize_platform_payment_method_card(obj: Any) -> PlatformPaymentMethodCard:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "CARD":
        raise ValueError(f"{repr(type)} is not 'CARD'")
    return PlatformPaymentMethodCard(type)
