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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PERCENT":
        raise ValueError("Expected 'PERCENT' for type")
    if "percent" not in obj:
        raise KeyError("Missing required field 'percent'")
    percent = obj["percent"]
    if not isinstance(percent, int):
        raise ValueError("Expected int for percent")
    return PromotionPercentDiscountScheme(percent)
