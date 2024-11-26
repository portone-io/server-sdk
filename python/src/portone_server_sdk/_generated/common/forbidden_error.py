from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ForbiddenError:
    """요청이 거절된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_forbidden_error(obj: ForbiddenError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "FORBIDDEN"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_forbidden_error(obj: Any) -> ForbiddenError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "FORBIDDEN":
        raise ValueError(f"{repr(type)} is not 'FORBIDDEN'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return ForbiddenError(message)
