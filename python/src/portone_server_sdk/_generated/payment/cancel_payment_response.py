from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_cancellation import PaymentCancellation, _deserialize_payment_cancellation, _serialize_payment_cancellation

@dataclass
class CancelPaymentResponse:
    """결제 취소 성공 응답
    """
    cancellation: PaymentCancellation
    """결체 취소 내역
    """


def _serialize_cancel_payment_response(obj: CancelPaymentResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["cancellation"] = _serialize_payment_cancellation(obj.cancellation)
    return entity


def _deserialize_cancel_payment_response(obj: Any) -> CancelPaymentResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cancellation" not in obj:
        raise KeyError(f"'cancellation' is not in {obj}")
    cancellation = obj["cancellation"]
    cancellation = _deserialize_payment_cancellation(cancellation)
    return CancelPaymentResponse(cancellation)
