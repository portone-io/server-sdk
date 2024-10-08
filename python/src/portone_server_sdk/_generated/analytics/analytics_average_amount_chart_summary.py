from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsAverageAmountChartSummary:
    """전체 구간의 건별 평균 거래액, 고객 당 평균 거래액을 나타냅니다.
    """
    payment_average_amount: int
    """건별 평균 거래액
    (int64)
    """
    customer_average_amount: int
    """고객 당 평균 거래액
    (int64)
    """


def _serialize_analytics_average_amount_chart_summary(obj: AnalyticsAverageAmountChartSummary) -> Any:
    entity = {}
    entity["paymentAverageAmount"] = obj.payment_average_amount
    entity["customerAverageAmount"] = obj.customer_average_amount
    return entity


def _deserialize_analytics_average_amount_chart_summary(obj: Any) -> AnalyticsAverageAmountChartSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentAverageAmount" not in obj:
        raise KeyError(f"'paymentAverageAmount' is not in {obj}")
    payment_average_amount = obj["paymentAverageAmount"]
    if not isinstance(payment_average_amount, int):
        raise ValueError(f"{repr(payment_average_amount)} is not int")
    if "customerAverageAmount" not in obj:
        raise KeyError(f"'customerAverageAmount' is not in {obj}")
    customer_average_amount = obj["customerAverageAmount"]
    if not isinstance(customer_average_amount, int):
        raise ValueError(f"{repr(customer_average_amount)} is not int")
    return AnalyticsAverageAmountChartSummary(payment_average_amount, customer_average_amount)
