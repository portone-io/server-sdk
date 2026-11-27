from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodMobile:
    """모바일
    """
    pass


def _serialize_platform_payment_method_mobile(obj: PlatformPaymentMethodMobile) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MOBILE"
    return entity


def _deserialize_platform_payment_method_mobile(obj: Any) -> PlatformPaymentMethodMobile:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "MOBILE":
        raise ValueError("Expected 'MOBILE' for type")
    return PlatformPaymentMethodMobile()
