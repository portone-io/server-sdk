from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentAlreadyCancelledError:
    """결제가 이미 취소된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_already_cancelled_error(obj: PaymentAlreadyCancelledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_ALREADY_CANCELLED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_already_cancelled_error(obj: Any) -> PaymentAlreadyCancelledError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PAYMENT_ALREADY_CANCELLED":
        raise ValueError("Expected 'PAYMENT_ALREADY_CANCELLED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PaymentAlreadyCancelledError(message)
