from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class OneLineAddress:
    """한 줄 형식 주소

    한 줄 형식 주소만 존재합니다.
    """
    one_line: str
    """주소 (한 줄)
    """


def _serialize_one_line_address(obj: OneLineAddress) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "ONE_LINE"
    entity["oneLine"] = obj.one_line
    return entity


def _deserialize_one_line_address(obj: Any) -> OneLineAddress:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "ONE_LINE":
        raise ValueError("Expected 'ONE_LINE' for type")
    if "oneLine" not in obj:
        raise KeyError("Missing required field 'oneLine'")
    one_line = obj["oneLine"]
    if not isinstance(one_line, str):
        raise ValueError("Expected str for one_line")
    return OneLineAddress(one_line)
