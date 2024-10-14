from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentScheduleAlreadyExistsError:
    """결제 예약건이 이미 존재하는 경우
    """
    type: Literal["PAYMENT_SCHEDULE_ALREADY_EXISTS"] = field(repr=False)
    message: Optional[str]


def _serialize_payment_schedule_already_exists_error(obj: PaymentScheduleAlreadyExistsError) -> Any:
    entity = {}
    entity["type"] = "PAYMENT_SCHEDULE_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_schedule_already_exists_error(obj: Any) -> PaymentScheduleAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_SCHEDULE_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_SCHEDULE_ALREADY_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentScheduleAlreadyExistsError(type, message)
