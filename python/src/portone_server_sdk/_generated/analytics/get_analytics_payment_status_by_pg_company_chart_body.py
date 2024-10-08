from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class GetAnalyticsPaymentStatusByPgCompanyChartBody:
    """고객사의 PG사별 결제전환율 조회를 위한 입력 정보
    """
    from_: str
    """조회할 결제 현황의 시작 시간
    (RFC 3339 date-time)
    """
    until: str
    """조회할 결제 현황의 끝 시간
    (RFC 3339 date-time)
    """
    currency: Currency
    """조회할 결제 통화

    입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
    """


def _serialize_get_analytics_payment_status_by_pg_company_chart_body(obj: GetAnalyticsPaymentStatusByPgCompanyChartBody) -> Any:
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    entity["currency"] = _serialize_currency(obj.currency)
    return entity


def _deserialize_get_analytics_payment_status_by_pg_company_chart_body(obj: Any) -> GetAnalyticsPaymentStatusByPgCompanyChartBody:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "from" not in obj:
        raise KeyError(f"'from' is not in {obj}")
    from_ = obj["from"]
    if not isinstance(from_, str):
        raise ValueError(f"{repr(from_)} is not str")
    if "until" not in obj:
        raise KeyError(f"'until' is not in {obj}")
    until = obj["until"]
    if not isinstance(until, str):
        raise ValueError(f"{repr(until)} is not str")
    if "currency" not in obj:
        raise KeyError(f"'currency' is not in {obj}")
    currency = obj["currency"]
    currency = _deserialize_currency(currency)
    return GetAnalyticsPaymentStatusByPgCompanyChartBody(from_, until, currency)
