from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.day_of_week import DayOfWeek, _deserialize_day_of_week, _serialize_day_of_week

@dataclass
class PlatformSettlementCycleMethodWeeklyInput:
    days_of_week: list[DayOfWeek]
    """요일
    """


def _serialize_platform_settlement_cycle_method_weekly_input(obj: PlatformSettlementCycleMethodWeeklyInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["daysOfWeek"] = list(map(_serialize_day_of_week, obj.days_of_week))
    return entity


def _deserialize_platform_settlement_cycle_method_weekly_input(obj: Any) -> PlatformSettlementCycleMethodWeeklyInput:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "daysOfWeek" not in obj:
        raise KeyError("Missing required field 'daysOfWeek'")
    days_of_week = obj["daysOfWeek"]
    if not isinstance(days_of_week, list):
        raise ValueError("Expected list for days_of_week")
    for i, item in enumerate(days_of_week):
        item = _deserialize_day_of_week(item)
        days_of_week[i] = item
    return PlatformSettlementCycleMethodWeeklyInput(days_of_week)
