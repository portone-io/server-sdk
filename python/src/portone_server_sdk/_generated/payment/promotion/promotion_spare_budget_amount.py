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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "AMOUNT":
        raise ValueError("Expected 'AMOUNT' for type")
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    return PromotionSpareBudgetAmount(amount)
