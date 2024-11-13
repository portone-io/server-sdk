from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformUserDefinedPropertyNotFoundError:
    """사용자 정의 속성이 존재 하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_user_defined_property_not_found_error(obj: PlatformUserDefinedPropertyNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_user_defined_property_not_found_error(obj: Any) -> PlatformUserDefinedPropertyNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformUserDefinedPropertyNotFoundError(message)
