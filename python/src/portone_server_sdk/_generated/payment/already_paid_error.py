from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AlreadyPaidError:
    """결제가 이미 완료된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_already_paid_error(obj: AlreadyPaidError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "ALREADY_PAID"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_already_paid_error(obj: Any) -> AlreadyPaidError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "ALREADY_PAID":
        raise ValueError("Expected 'ALREADY_PAID' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return AlreadyPaidError(message)
