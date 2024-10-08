from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.payment_status import PaymentStatus, _deserialize_payment_status, _serialize_payment_status
from portone_server_sdk._generated.common.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company

@dataclass
class AnalyticsPaymentStatusByPgCompanyChartStat:
    """각 상태의 건수와 금액, 사분위수를 나타냅니다.
    """
    pg_company: PgCompany
    """PG사
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


def _serialize_analytics_payment_status_by_pg_company_chart_stat(obj: AnalyticsPaymentStatusByPgCompanyChartStat) -> Any:
    entity = {}
    entity["pgCompany"] = _serialize_pg_company(obj.pg_company)
    entity["paymentStatus"] = _serialize_payment_status(obj.payment_status)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_payment_status_by_pg_company_chart_stat(obj: Any) -> AnalyticsPaymentStatusByPgCompanyChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "pgCompany" not in obj:
        raise KeyError(f"'pgCompany' is not in {obj}")
    pg_company = obj["pgCompany"]
    pg_company = _deserialize_pg_company(pg_company)
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
    return AnalyticsPaymentStatusByPgCompanyChartStat(pg_company, payment_status, amount, count)
