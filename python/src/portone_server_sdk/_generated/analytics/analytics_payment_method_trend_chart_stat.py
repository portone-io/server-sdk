from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type

@dataclass
class AnalyticsPaymentMethodTrendChartStat:
    """특정 시점의 결제수단별 결제금액, 결제 건수를 나타냅니다.
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
    payment_method: Optional[PaymentMethodType]
    """결제수단
    """


def _serialize_analytics_payment_method_trend_chart_stat(obj: AnalyticsPaymentMethodTrendChartStat) -> Any:
    entity = {}
    entity["timestamp"] = obj.timestamp
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    if obj.payment_method is not None:
        entity["paymentMethod"] = _serialize_payment_method_type(obj.payment_method)
    return entity


def _deserialize_analytics_payment_method_trend_chart_stat(obj: Any) -> AnalyticsPaymentMethodTrendChartStat:
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
    if "paymentMethod" in obj:
        payment_method = obj["paymentMethod"]
        payment_method = _deserialize_payment_method_type(payment_method)
    else:
        payment_method = None
    return AnalyticsPaymentMethodTrendChartStat(timestamp, amount, count, payment_method)
