from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InvalidRequestError:
    """요청된 입력 정보가 유효하지 않은 경우

    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """
    message: Optional[str] = field(default=None)


def _serialize_invalid_request_error(obj: InvalidRequestError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "INVALID_REQUEST"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_invalid_request_error(obj: Any) -> InvalidRequestError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "INVALID_REQUEST":
        raise ValueError("Expected 'INVALID_REQUEST' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return InvalidRequestError(message)
