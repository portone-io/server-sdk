from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformTransferPropertyExactMatchInput:
    """사용자 정의 속성 key/value exact match
    """
    key: str
    """키
    """
    value: str
    """값
    """


def _serialize_platform_transfer_property_exact_match_input(obj: PlatformTransferPropertyExactMatchInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["key"] = obj.key
    entity["value"] = obj.value
    return entity


def _deserialize_platform_transfer_property_exact_match_input(obj: Any) -> PlatformTransferPropertyExactMatchInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "key" not in obj:
        raise KeyError(f"'key' is not in {obj}")
    key = obj["key"]
    if not isinstance(key, str):
        raise ValueError(f"{repr(key)} is not str")
    if "value" not in obj:
        raise KeyError(f"'value' is not in {obj}")
    value = obj["value"]
    if not isinstance(value, str):
        raise ValueError(f"{repr(value)} is not str")
    return PlatformTransferPropertyExactMatchInput(key, value)
