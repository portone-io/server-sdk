from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider

@dataclass
class AnalyticsEasyPayProviderChartStat:
    """특정 시점의 간편결제사별 결제금액, 결제 건수를 나타냅니다.
    """
    timestamp: str
    """시점
    (RFC 3339 date-time)
    """
    easy_pay_provider: EasyPayProvider
    """간편결제사
    """
    amount: int
    """결제금액
    (int64)
    """
    count: int
    """결제 건수
    (int64)
    """


def _serialize_analytics_easy_pay_provider_chart_stat(obj: AnalyticsEasyPayProviderChartStat) -> Any:
    entity = {}
    entity["timestamp"] = obj.timestamp
    entity["easyPayProvider"] = _serialize_easy_pay_provider(obj.easy_pay_provider)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_easy_pay_provider_chart_stat(obj: Any) -> AnalyticsEasyPayProviderChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "easyPayProvider" not in obj:
        raise KeyError(f"'easyPayProvider' is not in {obj}")
    easy_pay_provider = obj["easyPayProvider"]
    easy_pay_provider = _deserialize_easy_pay_provider(easy_pay_provider)
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
    return AnalyticsEasyPayProviderChartStat(timestamp, easy_pay_provider, amount, count)
