from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.payment_method_type import PaymentMethodType, _deserialize_payment_method_type, _serialize_payment_method_type
from portone_server_sdk._generated.common.payment_status import PaymentStatus, _deserialize_payment_status, _serialize_payment_status

@dataclass
class AnalyticsPaymentStatusByPaymentMethodChartStat:
    """각 결제수단, 상태 별 건수와 금액을 나타냅니다.
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
    payment_method: Optional[PaymentMethodType]
    """결제수단
    """


def _serialize_analytics_payment_status_by_payment_method_chart_stat(obj: AnalyticsPaymentStatusByPaymentMethodChartStat) -> Any:
    entity = {}
    entity["paymentStatus"] = _serialize_payment_status(obj.payment_status)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    if obj.payment_method is not None:
        entity["paymentMethod"] = _serialize_payment_method_type(obj.payment_method)
    return entity


def _deserialize_analytics_payment_status_by_payment_method_chart_stat(obj: Any) -> AnalyticsPaymentStatusByPaymentMethodChartStat:
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
    if "paymentMethod" in obj:
        payment_method = obj["paymentMethod"]
        payment_method = _deserialize_payment_method_type(payment_method)
    else:
        payment_method = None
    return AnalyticsPaymentStatusByPaymentMethodChartStat(payment_status, amount, count, payment_method)