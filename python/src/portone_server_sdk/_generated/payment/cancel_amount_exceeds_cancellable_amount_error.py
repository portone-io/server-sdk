from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelAmountExceedsCancellableAmountError:
    """결제 취소 금액이 취소 가능 금액을 초과한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_cancel_amount_exceeds_cancellable_amount_error(obj: CancelAmountExceedsCancellableAmountError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_cancel_amount_exceeds_cancellable_amount_error(obj: Any) -> CancelAmountExceedsCancellableAmountError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT":
        raise ValueError("Expected 'CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return CancelAmountExceedsCancellableAmountError(message)
