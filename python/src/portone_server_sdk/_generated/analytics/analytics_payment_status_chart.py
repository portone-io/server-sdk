from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_payment_status_chart_stat import AnalyticsPaymentStatusChartStat, _deserialize_analytics_payment_status_chart_stat, _serialize_analytics_payment_status_chart_stat

@dataclass
class AnalyticsPaymentStatusChart:
    """고객사의 결제 상태 차트 정보
    """
    stats: list[AnalyticsPaymentStatusChartStat]


def _serialize_analytics_payment_status_chart(obj: AnalyticsPaymentStatusChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_payment_status_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_payment_status_chart(obj: Any) -> AnalyticsPaymentStatusChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_payment_status_chart_stat(item)
        stats[i] = item
    return AnalyticsPaymentStatusChart(stats)
