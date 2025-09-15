from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bFileNotFoundError:
    """업로드한 파일을 찾을 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_file_not_found_error(obj: B2bFileNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_FILE_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_file_not_found_error(obj: Any) -> B2bFileNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_FILE_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'B2B_FILE_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bFileNotFoundError(message)
