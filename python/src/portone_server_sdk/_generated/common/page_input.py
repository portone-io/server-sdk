from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PageInput:
    """다건 조회 API 에 사용되는 페이지 입력 정보
    """
    number: Optional[int] = field(default=None)
    """0부터 시작하는 페이지 번호
    (int32)
    """
    size: Optional[int] = field(default=None)
    """각 페이지 당 포함할 객체 수
    (int32)
    """


def _serialize_page_input(obj: PageInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.number is not None:
        entity["number"] = obj.number
    if obj.size is not None:
        entity["size"] = obj.size
    return entity


def _deserialize_page_input(obj: Any) -> PageInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "number" in obj:
        number = obj["number"]
        if not isinstance(number, int):
            raise ValueError(f"{repr(number)} is not int")
    else:
        number = None
    if "size" in obj:
        size = obj["size"]
        if not isinstance(size, int):
            raise ValueError(f"{repr(size)} is not int")
    else:
        size = None
    return PageInput(number, size)
