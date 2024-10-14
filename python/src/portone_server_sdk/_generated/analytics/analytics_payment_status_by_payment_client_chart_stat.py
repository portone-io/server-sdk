from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.payment_client_type import PaymentClientType, _deserialize_payment_client_type, _serialize_payment_client_type
from portone_server_sdk._generated.common.payment_status import PaymentStatus, _deserialize_payment_status, _serialize_payment_status

@dataclass
class AnalyticsPaymentStatusByPaymentClientChartStat:
    """고객사의 결제 환경 별 결제 상태 차트 정보
    """
    payment_client_type: PaymentClientType
    """결제가 발생한 클라이언트 환경
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


def _serialize_analytics_payment_status_by_payment_client_chart_stat(obj: AnalyticsPaymentStatusByPaymentClientChartStat) -> Any:
    entity = {}
    entity["paymentClientType"] = _serialize_payment_client_type(obj.payment_client_type)
    entity["paymentStatus"] = _serialize_payment_status(obj.payment_status)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_payment_status_by_payment_client_chart_stat(obj: Any) -> AnalyticsPaymentStatusByPaymentClientChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "paymentClientType" not in obj:
        raise KeyError(f"'paymentClientType' is not in {obj}")
    payment_client_type = obj["paymentClientType"]
    payment_client_type = _deserialize_payment_client_type(payment_client_type)
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
    return AnalyticsPaymentStatusByPaymentClientChartStat(payment_client_type, payment_status, amount, count)