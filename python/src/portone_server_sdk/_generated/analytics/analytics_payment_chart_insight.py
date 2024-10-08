from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.day_of_week import DayOfWeek, _deserialize_day_of_week, _serialize_day_of_week

@dataclass
class AnalyticsPaymentChartInsight:
    """고객사의 결제 현황 인사이트 정보
    """
    highest_hour_in_day: int
    """일간 최고 거래액 발생 시간
    (int64)
    """
    lowest_hour_in_day: int
    """일간 최저 거래액 발생 시간
    (int64)
    """
    highest_date_in_month: Optional[int]
    """월간 최고 거래액 발생일
    (int64)
    """
    lowest_date_in_month: Optional[int]
    """월간 최저 거래액 발생일
    (int64)
    """
    highest_day_in_week: Optional[DayOfWeek]
    """주간 최고 거래액 발생 요일
    """
    lowest_day_in_week: Optional[DayOfWeek]
    """주간 최저 거래액 발생 요일
    """


def _serialize_analytics_payment_chart_insight(obj: AnalyticsPaymentChartInsight) -> Any:
    entity = {}
    entity["highestHourInDay"] = obj.highest_hour_in_day
    entity["lowestHourInDay"] = obj.lowest_hour_in_day
    if obj.highest_date_in_month is not None:
        entity["highestDateInMonth"] = obj.highest_date_in_month
    if obj.lowest_date_in_month is not None:
        entity["lowestDateInMonth"] = obj.lowest_date_in_month
    if obj.highest_day_in_week is not None:
        entity["highestDayInWeek"] = _serialize_day_of_week(obj.highest_day_in_week)
    if obj.lowest_day_in_week is not None:
        entity["lowestDayInWeek"] = _serialize_day_of_week(obj.lowest_day_in_week)
    return entity


def _deserialize_analytics_payment_chart_insight(obj: Any) -> AnalyticsPaymentChartInsight:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "highestHourInDay" not in obj:
        raise KeyError(f"'highestHourInDay' is not in {obj}")
    highest_hour_in_day = obj["highestHourInDay"]
    if not isinstance(highest_hour_in_day, int):
        raise ValueError(f"{repr(highest_hour_in_day)} is not int")
    if "lowestHourInDay" not in obj:
        raise KeyError(f"'lowestHourInDay' is not in {obj}")
    lowest_hour_in_day = obj["lowestHourInDay"]
    if not isinstance(lowest_hour_in_day, int):
        raise ValueError(f"{repr(lowest_hour_in_day)} is not int")
    if "highestDateInMonth" in obj:
        highest_date_in_month = obj["highestDateInMonth"]
        if not isinstance(highest_date_in_month, int):
            raise ValueError(f"{repr(highest_date_in_month)} is not int")
    else:
        highest_date_in_month = None
    if "lowestDateInMonth" in obj:
        lowest_date_in_month = obj["lowestDateInMonth"]
        if not isinstance(lowest_date_in_month, int):
            raise ValueError(f"{repr(lowest_date_in_month)} is not int")
    else:
        lowest_date_in_month = None
    if "highestDayInWeek" in obj:
        highest_day_in_week = obj["highestDayInWeek"]
        highest_day_in_week = _deserialize_day_of_week(highest_day_in_week)
    else:
        highest_day_in_week = None
    if "lowestDayInWeek" in obj:
        lowest_day_in_week = obj["lowestDayInWeek"]
        lowest_day_in_week = _deserialize_day_of_week(lowest_day_in_week)
    else:
        lowest_day_in_week = None
    return AnalyticsPaymentChartInsight(highest_hour_in_day, lowest_hour_in_day, highest_date_in_month, lowest_date_in_month, highest_day_in_week, lowest_day_in_week)
