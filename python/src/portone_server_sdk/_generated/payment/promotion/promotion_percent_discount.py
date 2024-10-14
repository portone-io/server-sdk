from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionPercentDiscount:
    type: Literal["PERCENT"] = field(repr=False)
    """프로모션 할인 유형
    """
    percent: int
    """(int32)
    """


def _serialize_promotion_percent_discount(obj: PromotionPercentDiscount) -> Any:
    entity = {}
    entity["type"] = "PERCENT"
    entity["percent"] = obj.percent
    return entity


def _deserialize_promotion_percent_discount(obj: Any) -> PromotionPercentDiscount:
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
    return PromotionPercentDiscount(type, percent)
