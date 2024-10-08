from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_payment_status_by_payment_client_chart_stat import AnalyticsPaymentStatusByPaymentClientChartStat, _deserialize_analytics_payment_status_by_payment_client_chart_stat, _serialize_analytics_payment_status_by_payment_client_chart_stat

@dataclass
class AnalyticsPaymentStatusByPaymentClientChart:
    """고객사의 결제 환경 별 결제 상태 차트 정보
    """
    stats: list[AnalyticsPaymentStatusByPaymentClientChartStat]


def _serialize_analytics_payment_status_by_payment_client_chart(obj: AnalyticsPaymentStatusByPaymentClientChart) -> Any:
    entity = {}
    entity["stats"] = list(map(_serialize_analytics_payment_status_by_payment_client_chart_stat, obj.stats))
    return entity


def _deserialize_analytics_payment_status_by_payment_client_chart(obj: Any) -> AnalyticsPaymentStatusByPaymentClientChart:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "stats" not in obj:
        raise KeyError(f"'stats' is not in {obj}")
    stats = obj["stats"]
    if not isinstance(stats, list):
        raise ValueError(f"{repr(stats)} is not list")
    for i, item in enumerate(stats):
        item = _deserialize_analytics_payment_status_by_payment_client_chart_stat(item)
        stats[i] = item
    return AnalyticsPaymentStatusByPaymentClientChart(stats)
