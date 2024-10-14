from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionAmountDiscount:
    type: Literal["AMOUNT"] = field(repr=False)
    """프로모션 할인 유형
    """
    amount: int
    """(int64)
    """


def _serialize_promotion_amount_discount(obj: PromotionAmountDiscount) -> Any:
    entity = {}
    entity["type"] = "AMOUNT"
    entity["amount"] = obj.amount
    return entity


def _deserialize_promotion_amount_discount(obj: Any) -> PromotionAmountDiscount:
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
    return PromotionAmountDiscount(type, amount)
