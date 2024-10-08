from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_time_granularity_day import AnalyticsTimeGranularityDay, _deserialize_analytics_time_granularity_day, _serialize_analytics_time_granularity_day
from portone_server_sdk._generated.analytics.analytics_time_granularity_hour import AnalyticsTimeGranularityHour, _deserialize_analytics_time_granularity_hour, _serialize_analytics_time_granularity_hour
from portone_server_sdk._generated.analytics.analytics_time_granularity_minute import AnalyticsTimeGranularityMinute, _deserialize_analytics_time_granularity_minute, _serialize_analytics_time_granularity_minute
from portone_server_sdk._generated.analytics.analytics_time_granularity_month import AnalyticsTimeGranularityMonth, _deserialize_analytics_time_granularity_month, _serialize_analytics_time_granularity_month
from portone_server_sdk._generated.analytics.analytics_time_granularity_week import AnalyticsTimeGranularityWeek, _deserialize_analytics_time_granularity_week, _serialize_analytics_time_granularity_week

@dataclass
class AnalyticsTimeGranularity:
    """조회 시간 단위

    하나의 단위 필드만 선택하여 입력합니다.
    """
    minute: Optional[AnalyticsTimeGranularityMinute]
    hour: Optional[AnalyticsTimeGranularityHour]
    day: Optional[AnalyticsTimeGranularityDay]
    week: Optional[AnalyticsTimeGranularityWeek]
    month: Optional[AnalyticsTimeGranularityMonth]


def _serialize_analytics_time_granularity(obj: AnalyticsTimeGranularity) -> Any:
    entity = {}
    if obj.minute is not None:
        entity["minute"] = _serialize_analytics_time_granularity_minute(obj.minute)
    if obj.hour is not None:
        entity["hour"] = _serialize_analytics_time_granularity_hour(obj.hour)
    if obj.day is not None:
        entity["day"] = _serialize_analytics_time_granularity_day(obj.day)
    if obj.week is not None:
        entity["week"] = _serialize_analytics_time_granularity_week(obj.week)
    if obj.month is not None:
        entity["month"] = _serialize_analytics_time_granularity_month(obj.month)
    return entity


def _deserialize_analytics_time_granularity(obj: Any) -> AnalyticsTimeGranularity:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "minute" in obj:
        minute = obj["minute"]
        minute = _deserialize_analytics_time_granularity_minute(minute)
    else:
        minute = None
    if "hour" in obj:
        hour = obj["hour"]
        hour = _deserialize_analytics_time_granularity_hour(hour)
    else:
        hour = None
    if "day" in obj:
        day = obj["day"]
        day = _deserialize_analytics_time_granularity_day(day)
    else:
        day = None
    if "week" in obj:
        week = obj["week"]
        week = _deserialize_analytics_time_granularity_week(week)
    else:
        week = None
    if "month" in obj:
        month = obj["month"]
        month = _deserialize_analytics_time_granularity_month(month)
    else:
        month = None
    return AnalyticsTimeGranularity(minute, hour, day, week, month)
