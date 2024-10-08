from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_average_amount_chart_stat import AnalyticsAverageAmountChartStat, _deserialize_analytics_average_amount_chart_stat, _serialize_analytics_average_amount_chart_stat
from portone_server_sdk._generated.analytics.analytics_average_amount_chart_summary import AnalyticsAverageAmountChartSummary, _deserialize_analytics_average_amount_chart_summary, _serialize_analytics_average_amount_chart_summary

@dataclass
class AnalyticsAverageAmountChart:
    """고객사의 평균 거래액 현황 조회 응답
    """
    stats: list[AnalyticsAverageAmountChartStat]
    summary: AnalyticsAverageAmountChartSummary


def _serialize_analytics_average_amount_chart(obj: AnalyticsAverageAmountChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_average_amount_chart_stat, obj.stats))
    entity["summary"] = _serialize_analytics_average_amount_chart_summary(obj.summary)
    return entity


def _deserialize_analytics_average_amount_chart(obj: Any) -> AnalyticsAverageAmountChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_average_amount_chart_stat(item)
        stats[i] = item
    if "summary" not in obj:
        raise KeyError(f"'summary' is not in {obj}")
    summary = obj["summary"]
    summary = _deserialize_analytics_average_amount_chart_summary(summary)
    return AnalyticsAverageAmountChart(stats, summary)
