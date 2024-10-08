from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsCardCompanyChartRemainderStat:
    """특정 시점의 나머지 카드사들의 결제금액, 결제 건수를 나타냅니다.
    """
    timestamp: str
    """시점
    (RFC 3339 date-time)
    """
    amount: int
    """결제금액
    (int64)
    """
    count: int
    """결제 건수
    (int64)
    """


def _serialize_analytics_card_company_chart_remainder_stat(obj: AnalyticsCardCompanyChartRemainderStat) -> Any:
    entity = {}
    entity["timestamp"] = obj.timestamp
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_card_company_chart_remainder_stat(obj: Any) -> AnalyticsCardCompanyChartRemainderStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "amount" not in obj:
        raise KeyError(f"'amount' is not in {obj}")
    amount = obj["amount"]
    if not isinstance(amount, int):
        raise ValueError(f"{repr(amount)} is not int")
    if "count" not in obj:
        raise KeyError(f"'count' is not in {obj}")
    count = obj["count"]
    if not isinstance(count, int):
        raise ValueError(f"{repr(count)} is not int")
    return AnalyticsCardCompanyChartRemainderStat(timestamp, amount, count)
