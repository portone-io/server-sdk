from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class MaxCancelCountReachedError:
    """취소 시도 횟수가 초과된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_max_cancel_count_reached_error(obj: MaxCancelCountReachedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MAX_CANCEL_COUNT_REACHED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_max_cancel_count_reached_error(obj: Any) -> MaxCancelCountReachedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MAX_CANCEL_COUNT_REACHED":
        raise ValueError(f"{repr(type)} is not 'MAX_CANCEL_COUNT_REACHED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return MaxCancelCountReachedError(message)
