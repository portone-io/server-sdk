from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsTimeGranularityWeek:
    """주
    """
    timezone_hour_offset: int
    """(int32)
    """


def _serialize_analytics_time_granularity_week(obj: AnalyticsTimeGranularityWeek) -> Any:
    entity = {}
    entity["timezoneHourOffset"] = obj.timezone_hour_offset
    return entity


def _deserialize_analytics_time_granularity_week(obj: Any) -> AnalyticsTimeGranularityWeek:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timezoneHourOffset" not in obj:
        raise KeyError(f"'timezoneHourOffset' is not in {obj}")
    timezone_hour_offset = obj["timezoneHourOffset"]
    if not isinstance(timezone_hour_offset, int):
        raise ValueError(f"{repr(timezone_hour_offset)} is not int")
    return AnalyticsTimeGranularityWeek(timezone_hour_offset)