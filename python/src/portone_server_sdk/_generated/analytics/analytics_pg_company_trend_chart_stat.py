from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.pg_company import PgCompany, _deserialize_pg_company, _serialize_pg_company

@dataclass
class AnalyticsPgCompanyTrendChartStat:
    """특정 시점의 결제대행사 별 결제금액, 결제 건수를 나타냅니다.
    """
    timestamp: str
    """시점
    (RFC 3339 date-time)
    """
    pg_company: PgCompany
    """결제대행사
    """
    amount: int
    """결제금액
    (int64)
    """
    count: int
    """결제 건수
    (int64)
    """


def _serialize_analytics_pg_company_trend_chart_stat(obj: AnalyticsPgCompanyTrendChartStat) -> Any:
    entity = {}
    entity["timestamp"] = obj.timestamp
    entity["pgCompany"] = _serialize_pg_company(obj.pg_company)
    entity["amount"] = obj.amount
    entity["count"] = obj.count
    return entity


def _deserialize_analytics_pg_company_trend_chart_stat(obj: Any) -> AnalyticsPgCompanyTrendChartStat:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "timestamp" not in obj:
        raise KeyError(f"'timestamp' is not in {obj}")
    timestamp = obj["timestamp"]
    if not isinstance(timestamp, str):
        raise ValueError(f"{repr(timestamp)} is not str")
    if "pgCompany" not in obj:
        raise KeyError(f"'pgCompany' is not in {obj}")
    pg_company = obj["pgCompany"]
    pg_company = _deserialize_pg_company(pg_company)
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
    return AnalyticsPgCompanyTrendChartStat(timestamp, pg_company, amount, count)
