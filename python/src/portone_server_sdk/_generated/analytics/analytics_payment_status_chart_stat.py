from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.payment_status import PaymentStatus, _deserialize_payment_status, _serialize_payment_status

@dataclass
class AnalyticsPaymentStatusChartStat:
    """각 상태의 건수와 금액, 사분위수를 나타냅니다.
    """
    payment_status: PaymentStatus
    """결제 건 상태
    """
    amount: int
    """거래액
    (int64)
    """
    count: int
    """거래 건수
    (int64)
    """
    average_ratio: int
    """해당 상태 비율
    (int64)
    """
    first_quantile: int
    """1 사분위수
    (int64)
    """
    median: int
    """중앙값
    (int64)
    """
    third_quantile: int
    """3 사분위수
    (int64)
    """


def _serialize_analytics_payment_status_chart_stat(obj: AnalyticsPaymentStatusChartStat) -> Any:
    entity = {}
    entity["paymentStatus"] = _serialize_payment_status(obj.payment_status)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    entity["averageRatio"] = obj.average_ratio
    entity["firstQuantile"] = obj.first_quantile
    entity["median"] = obj.median
    entity["thirdQuantile"] = obj.third_quantile
    return entity


def _deserialize_analytics_payment_status_chart_stat(obj: Any) -> AnalyticsPaymentStatusChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentStatus" not in obj:
        raise KeyError(f"'paymentStatus' is not in {obj}")
    payment_status = obj["paymentStatus"]
    payment_status = _deserialize_payment_status(payment_status)
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
    if "averageRatio" not in obj:
        raise KeyError(f"'averageRatio' is not in {obj}")
    average_ratio = obj["averageRatio"]
    if not isinstance(average_ratio, int):
        raise ValueError(f"{repr(average_ratio)} is not int")
    if "firstQuantile" not in obj:
        raise KeyError(f"'firstQuantile' is not in {obj}")
    first_quantile = obj["firstQuantile"]
    if not isinstance(first_quantile, int):
        raise ValueError(f"{repr(first_quantile)} is not int")
    if "median" not in obj:
        raise KeyError(f"'median' is not in {obj}")
    median = obj["median"]
    if not isinstance(median, int):
        raise ValueError(f"{repr(median)} is not int")
    if "thirdQuantile" not in obj:
        raise KeyError(f"'thirdQuantile' is not in {obj}")
    third_quantile = obj["thirdQuantile"]
    if not isinstance(third_quantile, int):
        raise ValueError(f"{repr(third_quantile)} is not int")
    return AnalyticsPaymentStatusChartStat(payment_status, amount, count, average_ratio, first_quantile, median, third_quantile)
