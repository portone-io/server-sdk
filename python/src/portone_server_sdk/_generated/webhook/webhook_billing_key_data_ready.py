from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookBillingKeyDataReady:
    """빌링키 발급창이 열렸을 때 이벤트의 실제 세부 내용입니다.
    """
    billing_key: str
    """포트원에서 채번한 빌링키입니다.
    """


def _deserialize_webhook_billing_key_data_ready(obj: Any) -> WebhookBillingKeyDataReady:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    return WebhookBillingKeyDataReady(billing_key)
