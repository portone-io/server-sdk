from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodMobileInput:
    pass


def _serialize_platform_payment_method_mobile_input(obj: PlatformPaymentMethodMobileInput) -> Any:
    entity = {}
    return entity


def _deserialize_platform_payment_method_mobile_input(obj: Any) -> PlatformPaymentMethodMobileInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformPaymentMethodMobileInput()
