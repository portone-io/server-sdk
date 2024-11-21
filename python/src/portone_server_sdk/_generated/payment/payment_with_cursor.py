from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment import Payment, _deserialize_payment, _serialize_payment

@dataclass
class PaymentWithCursor:
    """결제 건 및 커서 정보
    """
    payment: Payment
    """결제 건 정보
    """
    cursor: str
    """해당 결제 건의 커서 정보
    """


def _serialize_payment_with_cursor(obj: PaymentWithCursor) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["payment"] = _serialize_payment(obj.payment)
    entity["cursor"] = obj.cursor
    return entity


def _deserialize_payment_with_cursor(obj: Any) -> PaymentWithCursor:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "payment" not in obj:
        raise KeyError(f"'payment' is not in {obj}")
    payment = obj["payment"]
    payment = _deserialize_payment(payment)
    if "cursor" not in obj:
        raise KeyError(f"'cursor' is not in {obj}")
    cursor = obj["cursor"]
    if not isinstance(cursor, str):
        raise ValueError(f"{repr(cursor)} is not str")
    return PaymentWithCursor(payment, cursor)
