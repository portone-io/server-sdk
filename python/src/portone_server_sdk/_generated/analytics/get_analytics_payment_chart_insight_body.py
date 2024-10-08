from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency

@dataclass
class GetAnalyticsPaymentChartInsightBody:
    """고객사의 결제 현황 인사이트 조회를 위한 입력 정보
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
    timezone_hour_offset: int
    """타임존 시간 오프셋

    입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.
    (int32)
    """
    exclude_cancelled: Optional[bool]
    """결제취소건 제외 여부

    true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
    """


def _serialize_get_analytics_payment_chart_insight_body(obj: GetAnalyticsPaymentChartInsightBody) -> Any:
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    entity["currency"] = _serialize_currency(obj.currency)
    entity["timezoneHourOffset"] = obj.timezone_hour_offset
    if obj.exclude_cancelled is not None:
        entity["excludeCancelled"] = obj.exclude_cancelled
    return entity


def _deserialize_get_analytics_payment_chart_insight_body(obj: Any) -> GetAnalyticsPaymentChartInsightBody:
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
    if "timezoneHourOffset" not in obj:
        raise KeyError(f"'timezoneHourOffset' is not in {obj}")
    timezone_hour_offset = obj["timezoneHourOffset"]
    if not isinstance(timezone_hour_offset, int):
        raise ValueError(f"{repr(timezone_hour_offset)} is not int")
    if "excludeCancelled" in obj:
        exclude_cancelled = obj["excludeCancelled"]
        if not isinstance(exclude_cancelled, bool):
            raise ValueError(f"{repr(exclude_cancelled)} is not bool")
    else:
        exclude_cancelled = None
    return GetAnalyticsPaymentChartInsightBody(from_, until, currency, timezone_hour_offset, exclude_cancelled)
