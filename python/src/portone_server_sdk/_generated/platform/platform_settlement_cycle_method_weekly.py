from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.day_of_week import DayOfWeek, _deserialize_day_of_week, _serialize_day_of_week

@dataclass
class PlatformSettlementCycleMethodWeekly:
    """매주 정해진 요일에 정산
    """
    days_of_week: list[DayOfWeek]
    """요일
    """


def _serialize_platform_settlement_cycle_method_weekly(obj: PlatformSettlementCycleMethodWeekly) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "WEEKLY"
    entity["daysOfWeek"] = list(map(_serialize_day_of_week, obj.days_of_week))
    return entity


def _deserialize_platform_settlement_cycle_method_weekly(obj: Any) -> PlatformSettlementCycleMethodWeekly:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "WEEKLY":
        raise ValueError(f"{repr(type)} is not 'WEEKLY'")
    if "daysOfWeek" not in obj:
        raise KeyError(f"'daysOfWeek' is not in {obj}")
    days_of_week = obj["daysOfWeek"]
    if not isinstance(days_of_week, list):
        raise ValueError(f"{repr(days_of_week)} is not list")
    for i, item in enumerate(days_of_week):
        item = _deserialize_day_of_week(item)
        days_of_week[i] = item
    return PlatformSettlementCycleMethodWeekly(days_of_week)
