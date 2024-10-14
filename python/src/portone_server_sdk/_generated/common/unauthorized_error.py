from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class UnauthorizedError:
    """인증 정보가 올바르지 않은 경우
    """
    type: Literal["UNAUTHORIZED"] = field(repr=False)
    message: Optional[str]


def _serialize_unauthorized_error(obj: UnauthorizedError) -> Any:
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
    return UnauthorizedError(type, message)
