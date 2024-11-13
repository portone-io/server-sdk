from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentAmountInput:
    """금액 세부 입력 정보
    """
    total: int
    """총 금액
    (int64)
    """
    tax_free: Optional[int] = field(default=None)
    """면세액
    (int64)
    """
    vat: Optional[int] = field(default=None)
    """부가세액

    고객사에서 직접 계산이 필요한 경우 입력합니다.
    입력하지 않으면 면세 금액을 제외한 금액의 1/11 로 자동 계산됩니다.
    (int64)
    """


def _serialize_payment_amount_input(obj: PaymentAmountInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["total"] = obj.total
    if obj.tax_free is not None:
        entity["taxFree"] = obj.tax_free
    if obj.vat is not None:
        entity["vat"] = obj.vat
    return entity


def _deserialize_payment_amount_input(obj: Any) -> PaymentAmountInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "total" not in obj:
        raise KeyError(f"'total' is not in {obj}")
    total = obj["total"]
    if not isinstance(total, int):
        raise ValueError(f"{repr(total)} is not int")
    if "taxFree" in obj:
        tax_free = obj["taxFree"]
        if not isinstance(tax_free, int):
            raise ValueError(f"{repr(tax_free)} is not int")
    else:
        tax_free = None
    if "vat" in obj:
        vat = obj["vat"]
        if not isinstance(vat, int):
            raise ValueError(f"{repr(vat)} is not int")
    else:
        vat = None
    return PaymentAmountInput(total, tax_free, vat)
