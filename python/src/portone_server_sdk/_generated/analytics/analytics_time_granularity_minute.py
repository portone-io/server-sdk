from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsTimeGranularityMinute:
    """분
    """
    pass


def _serialize_analytics_time_granularity_minute(obj: AnalyticsTimeGranularityMinute) -> Any:
    entity = {}
    return entity


def _deserialize_analytics_time_granularity_minute(obj: Any) -> AnalyticsTimeGranularityMinute:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return AnalyticsTimeGranularityMinute()
