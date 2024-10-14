from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentScheduleAlreadyRevokedError:
    """결제 예약건이 이미 취소된 경우
    """
    type: Literal["PAYMENT_SCHEDULE_ALREADY_REVOKED"] = field(repr=False)
    message: Optional[str]


def _serialize_payment_schedule_already_revoked_error(obj: PaymentScheduleAlreadyRevokedError) -> Any:
    entity = {}
    entity["type"] = "PAYMENT_SCHEDULE_ALREADY_REVOKED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_schedule_already_revoked_error(obj: Any) -> PaymentScheduleAlreadyRevokedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_SCHEDULE_ALREADY_REVOKED":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_SCHEDULE_ALREADY_REVOKED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentScheduleAlreadyRevokedError(type, message)
