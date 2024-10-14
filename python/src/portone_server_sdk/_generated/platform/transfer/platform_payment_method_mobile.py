from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentMethodMobile:
    """모바일
    """
    type: Literal["MOBILE"] = field(repr=False)


def _serialize_platform_payment_method_mobile(obj: PlatformPaymentMethodMobile) -> Any:
    entity = {}
    entity["type"] = "MOBILE"
    return entity


def _deserialize_platform_payment_method_mobile(obj: Any) -> PlatformPaymentMethodMobile:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MOBILE":
        raise ValueError(f"{repr(type)} is not 'MOBILE'")
    return PlatformPaymentMethodMobile(type)
