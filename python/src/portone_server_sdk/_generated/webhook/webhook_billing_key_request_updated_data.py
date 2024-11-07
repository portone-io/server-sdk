from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookBillingKeyRequestUpdatedData:
    billing_key: str
    """포트원에서 채번한 빌링키입니다.
    """


def _serialize_webhook_billing_key_request_updated_data(obj: WebhookBillingKeyRequestUpdatedData) -> Any:
    entity = {}
    entity["billingKey"] = obj.billing_key
    return entity


def _deserialize_webhook_billing_key_request_updated_data(obj: Any) -> WebhookBillingKeyRequestUpdatedData:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    return WebhookBillingKeyRequestUpdatedData(billing_key)
