from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_easy_pay_provider_chart_remainder_stat import AnalyticsEasyPayProviderChartRemainderStat, _deserialize_analytics_easy_pay_provider_chart_remainder_stat, _serialize_analytics_easy_pay_provider_chart_remainder_stat
from portone_server_sdk._generated.analytics.analytics_easy_pay_provider_chart_stat import AnalyticsEasyPayProviderChartStat, _deserialize_analytics_easy_pay_provider_chart_stat, _serialize_analytics_easy_pay_provider_chart_stat
from portone_server_sdk._generated.analytics.analytics_easy_pay_provider_chart_summary import AnalyticsEasyPayProviderChartSummary, _deserialize_analytics_easy_pay_provider_chart_summary, _serialize_analytics_easy_pay_provider_chart_summary

@dataclass
class AnalyticsEasyPayProviderChart:
    """고객사의 간편결제사별 결제 현황 차트 정보
    """
    stats: list[AnalyticsEasyPayProviderChartStat]
    remainder_stats: list[AnalyticsEasyPayProviderChartRemainderStat]
    summary: AnalyticsEasyPayProviderChartSummary


def _serialize_analytics_easy_pay_provider_chart(obj: AnalyticsEasyPayProviderChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_easy_pay_provider_chart_stat, obj.stats))
    entity["remainderStats"] = list(map(_serialize_analytics_easy_pay_provider_chart_remainder_stat, obj.remainder_stats))
    entity["summary"] = _serialize_analytics_easy_pay_provider_chart_summary(obj.summary)
    return entity


def _deserialize_analytics_easy_pay_provider_chart(obj: Any) -> AnalyticsEasyPayProviderChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_easy_pay_provider_chart_stat(item)
        stats[i] = item
    if "remainderStats" not in obj:
        raise KeyError(f"'remainderStats' is not in {obj}")
    remainder_stats = obj["remainderStats"]
    if not isinstance(remainder_stats, list):
        raise ValueError(f"{repr(remainder_stats)} is not list")
    for i, item in enumerate(remainder_stats):
        item = _deserialize_analytics_easy_pay_provider_chart_remainder_stat(item)
        remainder_stats[i] = item
    if "summary" not in obj:
        raise KeyError(f"'summary' is not in {obj}")
    summary = obj["summary"]
    summary = _deserialize_analytics_easy_pay_provider_chart_summary(summary)
    return AnalyticsEasyPayProviderChart(stats, remainder_stats, summary)
