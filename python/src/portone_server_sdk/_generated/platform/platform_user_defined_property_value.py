from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformUserDefinedPropertyValue:
    string: str


def _serialize_platform_user_defined_property_value(obj: PlatformUserDefinedPropertyValue) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["string"] = obj.string
    return entity


def _deserialize_platform_user_defined_property_value(obj: Any) -> PlatformUserDefinedPropertyValue:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "string" not in obj:
        raise KeyError("Missing required field 'string'")
    string = obj["string"]
    if not isinstance(string, str):
        raise ValueError("Expected str for string")
    return PlatformUserDefinedPropertyValue(string)
