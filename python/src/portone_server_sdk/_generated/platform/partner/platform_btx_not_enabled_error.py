from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformBtxNotEnabledError:
    """BTX 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_btx_not_enabled_error(obj: PlatformBtxNotEnabledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_BTX_NOT_ENABLED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_btx_not_enabled_error(obj: Any) -> PlatformBtxNotEnabledError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_BTX_NOT_ENABLED":
        raise ValueError("Expected 'PLATFORM_BTX_NOT_ENABLED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformBtxNotEnabledError(message)
