from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentInstallment:
    """할부 정보
    """
    month: int
    """할부 개월 수
    (int32)
    """
    is_interest_free: bool
    """무이자할부 여부
    """


def _serialize_payment_installment(obj: PaymentInstallment) -> Any:
    entity = {}
    entity["month"] = obj.month
    entity["isInterestFree"] = obj.is_interest_free
    return entity


def _deserialize_payment_installment(obj: Any) -> PaymentInstallment:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "month" not in obj:
        raise KeyError(f"'month' is not in {obj}")
    month = obj["month"]
    if not isinstance(month, int):
        raise ValueError(f"{repr(month)} is not int")
    if "isInterestFree" not in obj:
        raise KeyError(f"'isInterestFree' is not in {obj}")
    is_interest_free = obj["isInterestFree"]
    if not isinstance(is_interest_free, bool):
        raise ValueError(f"{repr(is_interest_free)} is not bool")
    return PaymentInstallment(month, is_interest_free)
