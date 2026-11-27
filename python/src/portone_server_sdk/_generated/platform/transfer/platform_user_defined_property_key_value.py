from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...platform.platform_user_defined_property_value import PlatformUserDefinedPropertyValue, _deserialize_platform_user_defined_property_value, _serialize_platform_user_defined_property_value

@dataclass
class PlatformUserDefinedPropertyKeyValue:
    """사용자 정의 속성
    """
    key: str
    """사용자 정의 속성 키
    """
    value: PlatformUserDefinedPropertyValue
    """사용자 정의 속성 값
    """


def _serialize_platform_user_defined_property_key_value(obj: PlatformUserDefinedPropertyKeyValue) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["key"] = obj.key
    entity["value"] = _serialize_platform_user_defined_property_value(obj.value)
    return entity


def _deserialize_platform_user_defined_property_key_value(obj: Any) -> PlatformUserDefinedPropertyKeyValue:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "key" not in obj:
        raise KeyError("Missing required field 'key'")
    key = obj["key"]
    if not isinstance(key, str):
        raise ValueError("Expected str for key")
    if "value" not in obj:
        raise KeyError("Missing required field 'value'")
    value = obj["value"]
    value = _deserialize_platform_user_defined_property_value(value)
    return PlatformUserDefinedPropertyKeyValue(key, value)
