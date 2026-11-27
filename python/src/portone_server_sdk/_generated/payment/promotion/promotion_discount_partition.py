from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.promotion.promotion_discount_scheme import PromotionDiscountScheme, _deserialize_promotion_discount_scheme, _serialize_promotion_discount_scheme

@dataclass
class PromotionDiscountPartition:
    """금액 구간별 프로모션 할인 정책
    """
    amount_from: int
    """(int64)
    """
    scheme: PromotionDiscountScheme


def _serialize_promotion_discount_partition(obj: PromotionDiscountPartition) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["amountFrom"] = obj.amount_from
    entity["scheme"] = _serialize_promotion_discount_scheme(obj.scheme)
    return entity


def _deserialize_promotion_discount_partition(obj: Any) -> PromotionDiscountPartition:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "amountFrom" not in obj:
        raise KeyError("Missing required field 'amountFrom'")
    amount_from = obj["amountFrom"]
    if not isinstance(amount_from, int):
        raise ValueError("Expected int for amount_from")
    if "scheme" not in obj:
        raise KeyError("Missing required field 'scheme'")
    scheme = obj["scheme"]
    scheme = _deserialize_promotion_discount_scheme(scheme)
    return PromotionDiscountPartition(amount_from, scheme)
