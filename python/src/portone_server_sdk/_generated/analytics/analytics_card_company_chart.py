from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_card_company_chart_remainder_stat import AnalyticsCardCompanyChartRemainderStat, _deserialize_analytics_card_company_chart_remainder_stat, _serialize_analytics_card_company_chart_remainder_stat
from portone_server_sdk._generated.analytics.analytics_card_company_chart_stat import AnalyticsCardCompanyChartStat, _deserialize_analytics_card_company_chart_stat, _serialize_analytics_card_company_chart_stat
from portone_server_sdk._generated.analytics.analytics_card_company_chart_summary import AnalyticsCardCompanyChartSummary, _deserialize_analytics_card_company_chart_summary, _serialize_analytics_card_company_chart_summary

@dataclass
class AnalyticsCardCompanyChart:
    """고객사의 카드사별 결제 현황 조회 응답
    """
    stats: list[AnalyticsCardCompanyChartStat]
    remainder_stats: list[AnalyticsCardCompanyChartRemainderStat]
    summary: AnalyticsCardCompanyChartSummary


def _serialize_analytics_card_company_chart(obj: AnalyticsCardCompanyChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_card_company_chart_stat, obj.stats))
    entity["remainderStats"] = list(map(_serialize_analytics_card_company_chart_remainder_stat, obj.remainder_stats))
    entity["summary"] = _serialize_analytics_card_company_chart_summary(obj.summary)
    return entity


def _deserialize_analytics_card_company_chart(obj: Any) -> AnalyticsCardCompanyChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_card_company_chart_stat(item)
        stats[i] = item
    if "remainderStats" not in obj:
        raise KeyError(f"'remainderStats' is not in {obj}")
    remainder_stats = obj["remainderStats"]
    if not isinstance(remainder_stats, list):
        raise ValueError(f"{repr(remainder_stats)} is not list")
    for i, item in enumerate(remainder_stats):
        item = _deserialize_analytics_card_company_chart_remainder_stat(item)
        remainder_stats[i] = item
    if "summary" not in obj:
        raise KeyError(f"'summary' is not in {obj}")
    summary = obj["summary"]
    summary = _deserialize_analytics_card_company_chart_summary(summary)
    return AnalyticsCardCompanyChart(stats, remainder_stats, summary)
