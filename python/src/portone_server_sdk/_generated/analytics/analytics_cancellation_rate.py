from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsCancellationRate:
    """고객사의 환불율 정보
    """
    cancellation_rate: float


def _serialize_analytics_cancellation_rate(obj: AnalyticsCancellationRate) -> Any:
    entity = {}
    entity["cancellationRate"] = obj.cancellation_rate
    return entity


def _deserialize_analytics_cancellation_rate(obj: Any) -> AnalyticsCancellationRate:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cancellationRate" not in obj:
        raise KeyError(f"'cancellationRate' is not in {obj}")
    cancellation_rate = obj["cancellationRate"]
    if not isinstance(cancellation_rate, (float, int)):
        raise ValueError(f"{repr(cancellation_rate)} is not (float, int)")
    return AnalyticsCancellationRate(cancellation_rate)
