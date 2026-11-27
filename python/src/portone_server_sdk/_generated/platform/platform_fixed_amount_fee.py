from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformFixedAmountFee:
    """정액 수수료

    총 금액에 무관하게 정해진 수수료 금액을 책정합니다.
    """
    amount: int
    """고정된 수수료 금액
    (int64)
    """


def _serialize_platform_fixed_amount_fee(obj: PlatformFixedAmountFee) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "FIXED_AMOUNT"
    entity["amount"] = obj.amount
    return entity


def _deserialize_platform_fixed_amount_fee(obj: Any) -> PlatformFixedAmountFee:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "FIXED_AMOUNT":
        raise ValueError("Expected 'FIXED_AMOUNT' for type")
    if "amount" not in obj:
        raise KeyError("Missing required field 'amount'")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError("Expected int for amount")
    return PlatformFixedAmountFee(amount)
