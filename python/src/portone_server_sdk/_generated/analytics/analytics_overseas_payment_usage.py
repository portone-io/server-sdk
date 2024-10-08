from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class AnalyticsOverseasPaymentUsage:
    """고객사의 해외 결제 사용 여부
    """
    is_using: bool


def _serialize_analytics_overseas_payment_usage(obj: AnalyticsOverseasPaymentUsage) -> Any:
    entity = {}
    entity["isUsing"] = obj.is_using
    return entity


def _deserialize_analytics_overseas_payment_usage(obj: Any) -> AnalyticsOverseasPaymentUsage:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "isUsing" not in obj:
        raise KeyError(f"'isUsing' is not in {obj}")
    is_using = obj["isUsing"]
    if not isinstance(is_using, bool):
        raise ValueError(f"{repr(is_using)} is not bool")
    return AnalyticsOverseasPaymentUsage(is_using)
