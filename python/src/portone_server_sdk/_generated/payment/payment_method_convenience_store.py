from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.convenience_store_brand import ConvenienceStoreBrand, _deserialize_convenience_store_brand, _serialize_convenience_store_brand

@dataclass
class PaymentMethodConvenienceStore:
    """편의점 결제 상세 정보
    """
    convenience_store_brand: Optional[ConvenienceStoreBrand] = field(default=None)
    """편의점 브랜드
    """
    confirmation_number: Optional[str] = field(default=None)
    """결제 확인 번호
    """
    receipt_number: Optional[str] = field(default=None)
    """결제 접수 번호
    """
    payment_deadline: Optional[str] = field(default=None)
    """결제 마감 시간
    (RFC 3339 date-time)
    """


def _serialize_payment_method_convenience_store(obj: PaymentMethodConvenienceStore) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PaymentMethodConvenienceStore"
    if obj.convenience_store_brand is not None:
        entity["convenienceStoreBrand"] = _serialize_convenience_store_brand(obj.convenience_store_brand)
    if obj.confirmation_number is not None:
        entity["confirmationNumber"] = obj.confirmation_number
    if obj.receipt_number is not None:
        entity["receiptNumber"] = obj.receipt_number
    if obj.payment_deadline is not None:
        entity["paymentDeadline"] = obj.payment_deadline
    return entity


def _deserialize_payment_method_convenience_store(obj: Any) -> PaymentMethodConvenienceStore:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PaymentMethodConvenienceStore":
        raise ValueError(f"{repr(type)} is not 'PaymentMethodConvenienceStore'")
    if "convenienceStoreBrand" in obj:
        convenience_store_brand = obj["convenienceStoreBrand"]
        convenience_store_brand = _deserialize_convenience_store_brand(convenience_store_brand)
    else:
        convenience_store_brand = None
    if "confirmationNumber" in obj:
        confirmation_number = obj["confirmationNumber"]
        if not isinstance(confirmation_number, str):
            raise ValueError(f"{repr(confirmation_number)} is not str")
    else:
        confirmation_number = None
    if "receiptNumber" in obj:
        receipt_number = obj["receiptNumber"]
        if not isinstance(receipt_number, str):
            raise ValueError(f"{repr(receipt_number)} is not str")
    else:
        receipt_number = None
    if "paymentDeadline" in obj:
        payment_deadline = obj["paymentDeadline"]
        if not isinstance(payment_deadline, str):
            raise ValueError(f"{repr(payment_deadline)} is not str")
    else:
        payment_deadline = None
    return PaymentMethodConvenienceStore(convenience_store_brand, confirmation_number, receipt_number, payment_deadline)
