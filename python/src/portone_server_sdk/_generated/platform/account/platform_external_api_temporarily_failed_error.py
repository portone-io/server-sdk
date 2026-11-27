from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformExternalApiTemporarilyFailedError:
    """외부 api의 일시적인 오류
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_external_api_temporarily_failed_error(obj: PlatformExternalApiTemporarilyFailedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_external_api_temporarily_failed_error(obj: Any) -> PlatformExternalApiTemporarilyFailedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
        raise ValueError("Expected 'PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformExternalApiTemporarilyFailedError(message)
