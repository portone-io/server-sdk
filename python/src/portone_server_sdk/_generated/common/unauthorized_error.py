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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "UNAUTHORIZED":
        raise ValueError("Expected 'UNAUTHORIZED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return UnauthorizedError(message)
