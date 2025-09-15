from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmedBillingKeySummary:
    """빌링키 발급 수동 승인 완료 응답
    """
    billing_key: str
    """빌링키
    """


def _serialize_confirmed_billing_key_summary(obj: ConfirmedBillingKeySummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["billingKey"] = obj.billing_key
    return entity


def _deserialize_confirmed_billing_key_summary(obj: Any) -> ConfirmedBillingKeySummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    return ConfirmedBillingKeySummary(billing_key)
