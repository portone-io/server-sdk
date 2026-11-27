from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentScheduleAlreadyRevokedError:
    """결제 예약건이 이미 취소된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_schedule_already_revoked_error(obj: PaymentScheduleAlreadyRevokedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_SCHEDULE_ALREADY_REVOKED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_schedule_already_revoked_error(obj: Any) -> PaymentScheduleAlreadyRevokedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PAYMENT_SCHEDULE_ALREADY_REVOKED":
        raise ValueError("Expected 'PAYMENT_SCHEDULE_ALREADY_REVOKED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PaymentScheduleAlreadyRevokedError(message)
