from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bIdAlreadyExistsError:
    """ID가 이미 사용중인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_id_already_exists_error(obj: B2bIdAlreadyExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_ID_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_id_already_exists_error(obj: Any) -> B2bIdAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_ID_ALREADY_EXISTS":
        raise ValueError("Expected 'B2B_ID_ALREADY_EXISTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bIdAlreadyExistsError(message)
