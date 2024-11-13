from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionSpareBudgetAmount:
    """환불 대비용 프로모션 추가 예산
    """
    amount: int
    """(int64)
    """


def _serialize_promotion_spare_budget_amount(obj: PromotionSpareBudgetAmount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "AMOUNT"
    entity["amount"] = obj.amount
    return entity


def _deserialize_promotion_spare_budget_amount(obj: Any) -> PromotionSpareBudgetAmount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "AMOUNT":
        raise ValueError(f"{repr(type)} is not 'AMOUNT'")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    return PromotionSpareBudgetAmount(amount)
