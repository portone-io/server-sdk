from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentAmount:
    """결제 금액 세부 정보
    """
    total: int
    """총 결제금액
    (int64)
    """
    tax_free: int
    """면세액
    (int64)
    """
    discount: int
    """할인금액

    카드사 프로모션, 포트원 프로모션, 적립형 포인트 결제, 쿠폰 할인 등을 포함합니다.
    (int64)
    """
    paid: int
    """실제 결제금액
    (int64)
    """
    cancelled: int
    """취소금액
    (int64)
    """
    cancelled_tax_free: int
    """취소금액 중 면세액
    (int64)
    """
    vat: Optional[int] = field(default=None)
    """부가세액
    (int64)
    """
    supply: Optional[int] = field(default=None)
    """공급가액
    (int64)
    """


def _serialize_payment_amount(obj: PaymentAmount) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["total"] = obj.total
    entity["taxFree"] = obj.tax_free
    entity["discount"] = obj.discount
    entity["paid"] = obj.paid
    entity["cancelled"] = obj.cancelled
    entity["cancelledTaxFree"] = obj.cancelled_tax_free
    if obj.vat is not None:
        entity["vat"] = obj.vat
    if obj.supply is not None:
        entity["supply"] = obj.supply
    return entity


def _deserialize_payment_amount(obj: Any) -> PaymentAmount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "total" not in obj:
        raise KeyError(f"'total' is not in {obj}")
    total = obj["total"]
    if not isinstance(total, int):
        raise ValueError(f"{repr(total)} is not int")
    if "taxFree" not in obj:
        raise KeyError(f"'taxFree' is not in {obj}")
    tax_free = obj["taxFree"]
    if not isinstance(tax_free, int):
        raise ValueError(f"{repr(tax_free)} is not int")
    if "discount" not in obj:
        raise KeyError(f"'discount' is not in {obj}")
    discount = obj["discount"]
    if not isinstance(discount, int):
        raise ValueError(f"{repr(discount)} is not int")
    if "paid" not in obj:
        raise KeyError(f"'paid' is not in {obj}")
    paid = obj["paid"]
    if not isinstance(paid, int):
        raise ValueError(f"{repr(paid)} is not int")
    if "cancelled" not in obj:
        raise KeyError(f"'cancelled' is not in {obj}")
    cancelled = obj["cancelled"]
    if not isinstance(cancelled, int):
        raise ValueError(f"{repr(cancelled)} is not int")
    if "cancelledTaxFree" not in obj:
        raise KeyError(f"'cancelledTaxFree' is not in {obj}")
    cancelled_tax_free = obj["cancelledTaxFree"]
    if not isinstance(cancelled_tax_free, int):
        raise ValueError(f"{repr(cancelled_tax_free)} is not int")
    if "vat" in obj:
        vat = obj["vat"]
        if not isinstance(vat, int):
            raise ValueError(f"{repr(vat)} is not int")
    else:
        vat = None
    if "supply" in obj:
        supply = obj["supply"]
        if not isinstance(supply, int):
            raise ValueError(f"{repr(supply)} is not int")
    else:
        supply = None
    return PaymentAmount(total, tax_free, discount, paid, cancelled, cancelled_tax_free, vat, supply)
