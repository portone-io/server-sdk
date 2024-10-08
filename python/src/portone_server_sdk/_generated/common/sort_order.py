from __future__ import annotations
from typing import Any, Literal, Optional

SortOrder = Literal["DESC", "ASC"]
"""정렬 방식
"""


def _serialize_sort_order(obj: SortOrder) -> Any:
    return obj


def _deserialize_sort_order(obj: Any) -> SortOrder:
    if obj not in ["DESC", "ASC"]:
        raise ValueError(f"{repr(obj)} is not SortOrder")
    return obj
