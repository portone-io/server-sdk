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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "WEEKLY":
        raise ValueError("Expected 'WEEKLY' for type")
    if "daysOfWeek" not in obj:
        raise KeyError("Missing required field 'daysOfWeek'")
    days_of_week = obj["daysOfWeek"]
    if not isinstance(days_of_week, list):
        raise ValueError("Expected list for days_of_week")
    for i, item in enumerate(days_of_week):
        item = _deserialize_day_of_week(item)
        days_of_week[i] = item
    return PlatformSettlementCycleMethodWeekly(days_of_week)
