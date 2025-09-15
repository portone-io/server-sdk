from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InformationMismatchError:
    """정보가 일치하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_information_mismatch_error(obj: InformationMismatchError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "INFORMATION_MISMATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_information_mismatch_error(obj: Any) -> InformationMismatchError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INFORMATION_MISMATCH":
        raise ValueError(f"{repr(type)} is not 'INFORMATION_MISMATCH'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return InformationMismatchError(message)
