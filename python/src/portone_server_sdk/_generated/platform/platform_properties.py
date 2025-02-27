from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_user_defined_property_value import PlatformUserDefinedPropertyValue, _deserialize_platform_user_defined_property_value, _serialize_platform_user_defined_property_value

@dataclass
class PlatformProperties:
    additional_properties: dict[str, PlatformUserDefinedPropertyValue]
    """추가 데이터
    """


def _serialize_platform_properties(obj: PlatformProperties) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    for key, value in obj.additional_properties.items():
        entity[key] = _serialize_platform_user_defined_property_value(value)
    return entity


def _deserialize_platform_properties(obj: Any) -> PlatformProperties:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional_properties = {}
    for key, value in obj.items():
        if key in []:
            continue
        additional_properties[key] = _deserialize_platform_user_defined_property_value(value)
    return PlatformProperties(additional_properties)
