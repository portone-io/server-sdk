from __future__ import annotations
from typing import Any, Literal, Optional, Union

SortOrder = Union[Literal["DESC", "ASC"], str]
"""정렬 방식
"""


def _serialize_sort_order(obj: SortOrder) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_sort_order(obj: Any) -> SortOrder:
    return obj
