from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PageInfo:
    """반환된 페이지 결과 정보
    """
    number: int
    """요청된 페이지 번호
    (int32)
    """
    size: int
    """요청된 페이지 당 객체 수
    (int32)
    """
    total_count: int
    """실제 반환된 객체 수
    (int32)
    """


def _serialize_page_info(obj: PageInfo) -> Any:
    entity = {}
    entity["number"] = obj.number
    entity["size"] = obj.size
    entity["totalCount"] = obj.total_count
    return entity


def _deserialize_page_info(obj: Any) -> PageInfo:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "number" not in obj:
        raise KeyError(f"'number' is not in {obj}")
    number = obj["number"]
    if not isinstance(number, int):
        raise ValueError(f"{repr(number)} is not int")
    if "size" not in obj:
        raise KeyError(f"'size' is not in {obj}")
    size = obj["size"]
    if not isinstance(size, int):
        raise ValueError(f"{repr(size)} is not int")
    if "totalCount" not in obj:
        raise KeyError(f"'totalCount' is not in {obj}")
    total_count = obj["totalCount"]
    if not isinstance(total_count, int):
        raise ValueError(f"{repr(total_count)} is not int")
    return PageInfo(number, size, total_count)
