from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.card_company import CardCompany, _deserialize_card_company, _serialize_card_company

@dataclass
class AnalyticsCardCompanyChartStat:
    """특정 시점의 카드사 별 결제금액, 결제 건수를 나타냅니다.
    """
    timestamp: str
    """시점
    (RFC 3339 date-time)
    """
    card_company: CardCompany
    """카드사
    """
    amount: int
    """결제금액
    (int64)
    """
    count: int
    """결제 건수
    (int64)
    """


def _serialize_analytics_card_company_chart_stat(obj: AnalyticsCardCompanyChartStat) -> Any:
    entity = {}
    entity["timestamp"] = obj.timestamp
    entity["cardCompany"] = _serialize_card_company(obj.card_company)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_card_company_chart_stat(obj: Any) -> AnalyticsCardCompanyChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "cardCompany" not in obj:
        raise KeyError(f"'cardCompany' is not in {obj}")
    card_company = obj["cardCompany"]
    card_company = _deserialize_card_company(card_company)
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
    return AnalyticsCardCompanyChartStat(timestamp, card_company, amount, count)
