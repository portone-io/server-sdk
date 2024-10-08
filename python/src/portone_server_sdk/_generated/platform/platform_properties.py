from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_user_defined_property_value import PlatformUserDefinedPropertyValue, _deserialize_platform_user_defined_property_value, _serialize_platform_user_defined_property_value

@dataclass
class PlatformProperties(PlatformUserDefinedPropertyValue):
    pass


def _serialize_platform_properties(obj: PlatformProperties) -> Any:
    entity = _serialize_platform_user_defined_property_value(obj)
    return entity


def _deserialize_platform_properties(obj: Any) -> PlatformProperties:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    additional = _deserialize_platform_user_defined_property_value(obj)
    string = additional.string
    return PlatformProperties(string)
