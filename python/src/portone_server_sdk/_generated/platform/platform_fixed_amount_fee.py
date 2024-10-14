from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformFixedAmountFee:
    """정액 수수료

    총 금액에 무관하게 정해진 수수료 금액을 책정합니다.
    """
    type: Literal["FIXED_AMOUNT"] = field(repr=False)
    amount: int
    """고정된 수수료 금액
    (int64)
    """


def _serialize_platform_fixed_amount_fee(obj: PlatformFixedAmountFee) -> Any:
    entity = {}
    entity["type"] = "FIXED_AMOUNT"
    entity["amount"] = obj.amount
    return entity


def _deserialize_platform_fixed_amount_fee(obj: Any) -> PlatformFixedAmountFee:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "FIXED_AMOUNT":
        raise ValueError(f"{repr(type)} is not 'FIXED_AMOUNT'")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    return PlatformFixedAmountFee(type, amount)
