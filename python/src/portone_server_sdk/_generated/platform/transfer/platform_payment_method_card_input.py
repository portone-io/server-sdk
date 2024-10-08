from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodCardInput:
    pass


def _serialize_platform_payment_method_card_input(obj: PlatformPaymentMethodCardInput) -> Any:
    entity = {}
    return entity


def _deserialize_platform_payment_method_card_input(obj: Any) -> PlatformPaymentMethodCardInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformPaymentMethodCardInput()
