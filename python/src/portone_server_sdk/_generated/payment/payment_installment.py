from __future__ import annotations
from dataclasses import field
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
    is_interest_free_from_merchant: Optional[bool] = field(default=None)
    """상점 부담 무이자할부 여부

    정보 필요시 포트원과 협의해 주세요.
    """


def _serialize_payment_installment(obj: PaymentInstallment) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["month"] = obj.month
    entity["isInterestFree"] = obj.is_interest_free
    if obj.is_interest_free_from_merchant is not None:
        entity["isInterestFreeFromMerchant"] = obj.is_interest_free_from_merchant
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
    if "isInterestFreeFromMerchant" in obj:
        is_interest_free_from_merchant = obj["isInterestFreeFromMerchant"]
        if not isinstance(is_interest_free_from_merchant, bool):
            raise ValueError(f"{repr(is_interest_free_from_merchant)} is not bool")
    else:
        is_interest_free_from_merchant = None
    return PaymentInstallment(month, is_interest_free, is_interest_free_from_merchant)
