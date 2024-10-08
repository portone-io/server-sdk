from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class MonthDay:
    """월 및 일자 정보
    """
    month: int
    """(int32)
    """
    day: int
    """(int32)
    """


def _serialize_month_day(obj: MonthDay) -> Any:
    entity = {}
    entity["month"] = obj.month
    entity["day"] = obj.day
    return entity


def _deserialize_month_day(obj: Any) -> MonthDay:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "month" not in obj:
        raise KeyError(f"'month' is not in {obj}")
    month = obj["month"]
    if not isinstance(month, int):
        raise ValueError(f"{repr(month)} is not int")
    if "day" not in obj:
        raise KeyError(f"'day' is not in {obj}")
    day = obj["day"]
    if not isinstance(day, int):
        raise ValueError(f"{repr(day)} is not int")
    return MonthDay(month, day)
