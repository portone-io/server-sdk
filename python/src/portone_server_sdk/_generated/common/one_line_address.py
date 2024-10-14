from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class OneLineAddress:
    """한 줄 형식 주소

    한 줄 형식 주소만 존재합니다.
    """
    type: Literal["ONE_LINE"] = field(repr=False)
    one_line: str
    """주소 (한 줄)
    """


def _serialize_one_line_address(obj: OneLineAddress) -> Any:
    entity = {}
    entity["type"] = "ONE_LINE"
    entity["oneLine"] = obj.one_line
    return entity


def _deserialize_one_line_address(obj: Any) -> OneLineAddress:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ONE_LINE":
        raise ValueError(f"{repr(type)} is not 'ONE_LINE'")
    if "oneLine" not in obj:
        raise KeyError(f"'oneLine' is not in {obj}")
    one_line = obj["oneLine"]
    if not isinstance(one_line, str):
        raise ValueError(f"{repr(one_line)} is not str")
    return OneLineAddress(type, one_line)
