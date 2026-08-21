from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class SessionNotFoundError:
    """결제 세션이 존재하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_session_not_found_error(obj: SessionNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "SESSION_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_session_not_found_error(obj: Any) -> SessionNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "SESSION_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'SESSION_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return SessionNotFoundError(message)
