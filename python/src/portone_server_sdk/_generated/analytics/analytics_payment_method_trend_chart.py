from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_payment_method_trend_chart_stat import AnalyticsPaymentMethodTrendChartStat, _deserialize_analytics_payment_method_trend_chart_stat, _serialize_analytics_payment_method_trend_chart_stat

@dataclass
class AnalyticsPaymentMethodTrendChart:
    """고객사의 결제수단 트렌드 차트 정보
    """
    stats: list[AnalyticsPaymentMethodTrendChartStat]
    """결제수단별 결제금액, 결제 건수 데이터

    (timestamp, paymentMethod) 를 기준으로 오름차순 정렬되어 주어집니다.
    """


def _serialize_analytics_payment_method_trend_chart(obj: AnalyticsPaymentMethodTrendChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_payment_method_trend_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_payment_method_trend_chart(obj: Any) -> AnalyticsPaymentMethodTrendChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_payment_method_trend_chart_stat(item)
        stats[i] = item
    return AnalyticsPaymentMethodTrendChart(stats)
