from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bNotEnabledError:
    """B2B 기능이 활성화되지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_not_enabled_error(obj: B2bNotEnabledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_NOT_ENABLED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_not_enabled_error(obj: Any) -> B2bNotEnabledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_NOT_ENABLED":
        raise ValueError(f"{repr(type)} is not 'B2B_NOT_ENABLED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bNotEnabledError(message)
