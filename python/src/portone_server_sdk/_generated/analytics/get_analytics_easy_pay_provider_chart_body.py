from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.analytics.analytics_time_granularity import AnalyticsTimeGranularity, _deserialize_analytics_time_granularity, _serialize_analytics_time_granularity
from portone_server_sdk._generated.common.currency import Currency, _deserialize_currency, _serialize_currency
from portone_server_sdk._generated.common.easy_pay_provider import EasyPayProvider, _deserialize_easy_pay_provider, _serialize_easy_pay_provider

@dataclass
class GetAnalyticsEasyPayProviderChartBody:
    """고객사의 간편결제사별 결제 현황 조회를 위한 입력 정보
    """
    from_: str
    """조회할 간편결제사별 결제 현황의 시작 시간
    (RFC 3339 date-time)
    """
    until: str
    """조회할 간편결제사별 결제 현황의 끝 시간
    (RFC 3339 date-time)
    """
    currency: Currency
    """조회할 결제 통화

    입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
    """
    exclude_cancelled: bool
    """결제취소건 제외 여부

    true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
    """
    time_granularity: AnalyticsTimeGranularity
    """간편결제사별 결제 현황 조회 단위

    시간별, 월별 단위만 지원됩니다.
    """
    easy_pay_providers: list[EasyPayProvider]
    """조회할 간편결제사
    """
    excludes_from_remainders: list[EasyPayProvider]
    """나머지 집계에 포함되지 않을 간편결제사
    """


def _serialize_get_analytics_easy_pay_provider_chart_body(obj: GetAnalyticsEasyPayProviderChartBody) -> Any:
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    entity["currency"] = _serialize_currency(obj.currency)
    entity["excludeCancelled"] = obj.exclude_cancelled
    entity["timeGranularity"] = _serialize_analytics_time_granularity(obj.time_granularity)
    entity["easyPayProviders"] = list(map(_serialize_easy_pay_provider, obj.easy_pay_providers))
    entity["excludesFromRemainders"] = list(map(_serialize_easy_pay_provider, obj.excludes_from_remainders))
    return entity


def _deserialize_get_analytics_easy_pay_provider_chart_body(obj: Any) -> GetAnalyticsEasyPayProviderChartBody:
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
    if "excludeCancelled" not in obj:
        raise KeyError(f"'excludeCancelled' is not in {obj}")
    exclude_cancelled = obj["excludeCancelled"]
    if not isinstance(exclude_cancelled, bool):
        raise ValueError(f"{repr(exclude_cancelled)} is not bool")
    if "timeGranularity" not in obj:
        raise KeyError(f"'timeGranularity' is not in {obj}")
    time_granularity = obj["timeGranularity"]
    time_granularity = _deserialize_analytics_time_granularity(time_granularity)
    if "easyPayProviders" not in obj:
        raise KeyError(f"'easyPayProviders' is not in {obj}")
    easy_pay_providers = obj["easyPayProviders"]
    if not isinstance(easy_pay_providers, list):
        raise ValueError(f"{repr(easy_pay_providers)} is not list")
    for i, item in enumerate(easy_pay_providers):
        item = _deserialize_easy_pay_provider(item)
        easy_pay_providers[i] = item
    if "excludesFromRemainders" not in obj:
        raise KeyError(f"'excludesFromRemainders' is not in {obj}")
    excludes_from_remainders = obj["excludesFromRemainders"]
    if not isinstance(excludes_from_remainders, list):
        raise ValueError(f"{repr(excludes_from_remainders)} is not list")
    for i, item in enumerate(excludes_from_remainders):
        item = _deserialize_easy_pay_provider(item)
        excludes_from_remainders[i] = item
    return GetAnalyticsEasyPayProviderChartBody(from_, until, currency, exclude_cancelled, time_granularity, easy_pay_providers, excludes_from_remainders)
