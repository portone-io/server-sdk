from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionPercentDiscountScheme:
    """프로모션 할인 유형
    """
    percent: int
    """(int32)
    """


def _serialize_promotion_percent_discount_scheme(obj: PromotionPercentDiscountScheme) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PERCENT"
    entity["percent"] = obj.percent
    return entity


def _deserialize_promotion_percent_discount_scheme(obj: Any) -> PromotionPercentDiscountScheme:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PERCENT":
        raise ValueError(f"{repr(type)} is not 'PERCENT'")
    if "percent" not in obj:
        raise KeyError(f"'percent' is not in {obj}")
    percent = obj["percent"]
    if not isinstance(percent, int):
        raise ValueError(f"{repr(percent)} is not int")
    return PromotionPercentDiscountScheme(percent)
