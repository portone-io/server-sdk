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
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformExternalApiTemporarilyFailedError(message)
