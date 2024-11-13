from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class UnauthorizedError:
    """인증 정보가 올바르지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_unauthorized_error(obj: UnauthorizedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "UNAUTHORIZED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_unauthorized_error(obj: Any) -> UnauthorizedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "UNAUTHORIZED":
        raise ValueError(f"{repr(type)} is not 'UNAUTHORIZED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return UnauthorizedError(message)
