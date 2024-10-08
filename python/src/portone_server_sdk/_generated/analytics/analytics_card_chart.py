from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_card_chart_stat import AnalyticsCardChartStat, _deserialize_analytics_card_chart_stat, _serialize_analytics_card_chart_stat

@dataclass
class AnalyticsCardChart:
    """고객사의 카드결제 현황 차트 정보
    """
    stats: list[AnalyticsCardChartStat]


def _serialize_analytics_card_chart(obj: AnalyticsCardChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_card_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_card_chart(obj: Any) -> AnalyticsCardChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_card_chart_stat(item)
        stats[i] = item
    return AnalyticsCardChart(stats)
