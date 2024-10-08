from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsEasyPayProviderChartSummary:
    """결제금액, 결제 건수의 총합을 나타냅니다.
    """
    total_amount: int
    """결제금액의 합
    (int64)
    """
    total_count: int
    """결제 건수의 합
    (int64)
    """


def _serialize_analytics_easy_pay_provider_chart_summary(obj: AnalyticsEasyPayProviderChartSummary) -> Any:
    entity = {}
    entity["totalAmount"] = obj.total_amount
    entity["totalCount"] = obj.total_count
    return entity


def _deserialize_analytics_easy_pay_provider_chart_summary(obj: Any) -> AnalyticsEasyPayProviderChartSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
    if "totalCount" not in obj:
        raise KeyError(f"'totalCount' is not in {obj}")
    total_count = obj["totalCount"]
    if not isinstance(total_count, int):
        raise ValueError(f"{repr(total_count)} is not int")
    return AnalyticsEasyPayProviderChartSummary(total_amount, total_count)
