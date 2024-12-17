from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class WebhookBillingKeyDataUpdated:
    """빌링키가 업데이트되었을 때 이벤트의 실제 세부 내용입니다.
    """
    billing_key: str
    """포트원에서 채번한 빌링키입니다.
    """
    store_id: str
    """웹훅을 트리거한 상점의 아이디입니다.
    """


def _deserialize_webhook_billing_key_data_updated(obj: Any) -> WebhookBillingKeyDataUpdated:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "billingKey" not in obj:
        raise KeyError(f"'billingKey' is not in {obj}")
    billing_key = obj["billingKey"]
    if not isinstance(billing_key, str):
        raise ValueError(f"{repr(billing_key)} is not str")
    if "storeId" not in obj:
        raise KeyError(f"'storeId' is not in {obj}")
    store_id = obj["storeId"]
    if not isinstance(store_id, str):
        raise ValueError(f"{repr(store_id)} is not str")
    return WebhookBillingKeyDataUpdated(billing_key, store_id)
