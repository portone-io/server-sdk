from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_pg_company_trend_chart_stat import AnalyticsPgCompanyTrendChartStat, _deserialize_analytics_pg_company_trend_chart_stat, _serialize_analytics_pg_company_trend_chart_stat

@dataclass
class AnalyticsPgCompanyTrendChart:
    """고객사의 결제대행사별 거래 추이 차트 정보
    """
    stats: list[AnalyticsPgCompanyTrendChartStat]


def _serialize_analytics_pg_company_trend_chart(obj: AnalyticsPgCompanyTrendChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_pg_company_trend_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_pg_company_trend_chart(obj: Any) -> AnalyticsPgCompanyTrendChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_pg_company_trend_chart_stat(item)
        stats[i] = item
    return AnalyticsPgCompanyTrendChart(stats)
