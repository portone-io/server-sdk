from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentScheduleAlreadyProcessedError:
    """결제 예약건이 이미 처리된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_schedule_already_processed_error(obj: PaymentScheduleAlreadyProcessedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_SCHEDULE_ALREADY_PROCESSED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_schedule_already_processed_error(obj: Any) -> PaymentScheduleAlreadyProcessedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_SCHEDULE_ALREADY_PROCESSED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentScheduleAlreadyProcessedError(message)
