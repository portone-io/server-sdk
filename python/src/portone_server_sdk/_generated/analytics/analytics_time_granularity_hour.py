from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsTimeGranularityHour:
    """시간
    """
    pass


def _serialize_analytics_time_granularity_hour(obj: AnalyticsTimeGranularityHour) -> Any:
    entity = {}
    return entity


def _deserialize_analytics_time_granularity_hour(obj: Any) -> AnalyticsTimeGranularityHour:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return AnalyticsTimeGranularityHour()
