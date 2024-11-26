from __future__ import annotations
from typing import Any, Literal, Optional, Union

DayOfWeek = Union[Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"], str]
"""요일
"""


def _serialize_day_of_week(obj: DayOfWeek) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_day_of_week(obj: Any) -> DayOfWeek:
    return obj
