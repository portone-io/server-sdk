from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_pg_company_chart_stat import AnalyticsPgCompanyChartStat, _deserialize_analytics_pg_company_chart_stat, _serialize_analytics_pg_company_chart_stat

@dataclass
class AnalyticsPgCompanyChart:
    """고객사의 결제대행사 현황 차트 정보
    """
    stats: list[AnalyticsPgCompanyChartStat]


def _serialize_analytics_pg_company_chart(obj: AnalyticsPgCompanyChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_pg_company_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_pg_company_chart(obj: Any) -> AnalyticsPgCompanyChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_pg_company_chart_stat(item)
        stats[i] = item
    return AnalyticsPgCompanyChart(stats)
