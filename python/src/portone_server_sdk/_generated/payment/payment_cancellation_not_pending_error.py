from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentCancellationNotPendingError:
    """결제 취소 내역이 취소 요청 상태가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_cancellation_not_pending_error(obj: PaymentCancellationNotPendingError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_CANCELLATION_NOT_PENDING"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_cancellation_not_pending_error(obj: Any) -> PaymentCancellationNotPendingError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PAYMENT_CANCELLATION_NOT_PENDING":
        raise ValueError("Expected 'PAYMENT_CANCELLATION_NOT_PENDING' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PaymentCancellationNotPendingError(message)
