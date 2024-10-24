from __future__ import annotations
from typing import Any, Literal, Optional

DayOfWeek = Literal["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
"""요일
"""


def _serialize_day_of_week(obj: DayOfWeek) -> Any:
    return obj


def _deserialize_day_of_week(obj: Any) -> DayOfWeek:
    if obj not in ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]:
        raise ValueError(f"{repr(obj)} is not DayOfWeek")
    return obj
