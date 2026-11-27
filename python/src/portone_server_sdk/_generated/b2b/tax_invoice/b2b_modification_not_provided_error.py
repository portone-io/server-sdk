from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bModificationNotProvidedError:
    """세금계산서 수정 입력 정보를 찾을 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_modification_not_provided_error(obj: B2bModificationNotProvidedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_MODIFICATION_NOT_PROVIDED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_modification_not_provided_error(obj: Any) -> B2bModificationNotProvidedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_MODIFICATION_NOT_PROVIDED":
        raise ValueError("Expected 'B2B_MODIFICATION_NOT_PROVIDED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bModificationNotProvidedError(message)
