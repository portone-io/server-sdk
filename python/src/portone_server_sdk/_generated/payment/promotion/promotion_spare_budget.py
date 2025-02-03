from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.promotion.promotion_spare_budget_amount import PromotionSpareBudgetAmount, _deserialize_promotion_spare_budget_amount, _serialize_promotion_spare_budget_amount
from ...payment.promotion.promotion_spare_budget_percent import PromotionSpareBudgetPercent, _deserialize_promotion_spare_budget_percent, _serialize_promotion_spare_budget_percent

PromotionSpareBudget = Union[PromotionSpareBudgetAmount, PromotionSpareBudgetPercent, dict]


def _serialize_promotion_spare_budget(obj: PromotionSpareBudget) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PromotionSpareBudgetAmount):
        return _serialize_promotion_spare_budget_amount(obj)
    if isinstance(obj, PromotionSpareBudgetPercent):
        return _serialize_promotion_spare_budget_percent(obj)


def _deserialize_promotion_spare_budget(obj: Any) -> PromotionSpareBudget:
    try:
        return _deserialize_promotion_spare_budget_amount(obj)
    except Exception:
        pass
    try:
        return _deserialize_promotion_spare_budget_percent(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PromotionSpareBudget")
