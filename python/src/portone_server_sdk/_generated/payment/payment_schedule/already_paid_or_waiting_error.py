from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AlreadyPaidOrWaitingError:
    """결제가 이미 완료되었거나 대기중인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_already_paid_or_waiting_error(obj: AlreadyPaidOrWaitingError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "ALREADY_PAID_OR_WAITING"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_already_paid_or_waiting_error(obj: Any) -> AlreadyPaidOrWaitingError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ALREADY_PAID_OR_WAITING":
        raise ValueError(f"{repr(type)} is not 'ALREADY_PAID_OR_WAITING'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return AlreadyPaidOrWaitingError(message)
