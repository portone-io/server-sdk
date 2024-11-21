from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.promotion.promotion_discount_partition import PromotionDiscountPartition, _deserialize_promotion_discount_partition, _serialize_promotion_discount_partition

@dataclass
class PromotionDiscountPolicy:
    """프로모션 할인 정책
    """
    partitions: list[PromotionDiscountPartition]
    """금액 구간별 프로모션 할인 정책
    """


def _serialize_promotion_discount_policy(obj: PromotionDiscountPolicy) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["partitions"] = list(map(_serialize_promotion_discount_partition, obj.partitions))
    return entity


def _deserialize_promotion_discount_policy(obj: Any) -> PromotionDiscountPolicy:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "partitions" not in obj:
        raise KeyError(f"'partitions' is not in {obj}")
    partitions = obj["partitions"]
    if not isinstance(partitions, list):
        raise ValueError(f"{repr(partitions)} is not list")
    for i, item in enumerate(partitions):
        item = _deserialize_promotion_discount_partition(item)
        partitions[i] = item
    return PromotionDiscountPolicy(partitions)
