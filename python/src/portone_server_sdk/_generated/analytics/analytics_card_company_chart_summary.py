from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsCardCompanyChartSummary:
    """결제금액, 결제 건수의 총합을 나타냅니다.
    """
    total_amount: int
    """결제금액 합
    (int64)
    """
    total_count: int
    """결제 건수 합
    (int64)
    """


def _serialize_analytics_card_company_chart_summary(obj: AnalyticsCardCompanyChartSummary) -> Any:
    entity = {}
    entity["totalAmount"] = obj.total_amount
    entity["totalCount"] = obj.total_count
    return entity


def _deserialize_analytics_card_company_chart_summary(obj: Any) -> AnalyticsCardCompanyChartSummary:
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
    return AnalyticsCardCompanyChartSummary(total_amount, total_count)
