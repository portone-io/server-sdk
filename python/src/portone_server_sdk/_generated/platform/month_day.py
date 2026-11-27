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
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["month"] = obj.month
    entity["day"] = obj.day
    return entity


def _deserialize_month_day(obj: Any) -> MonthDay:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "month" not in obj:
        raise KeyError("Missing required field 'month'")
    month = obj["month"]
    if not isinstance(month, int):
        raise ValueError("Expected int for month")
    if "day" not in obj:
        raise KeyError("Missing required field 'day'")
    day = obj["day"]
    if not isinstance(day, int):
        raise ValueError("Expected int for day")
    return MonthDay(month, day)
