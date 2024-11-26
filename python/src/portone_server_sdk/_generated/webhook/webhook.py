from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_billing_key import WebhookBillingKey, _deserialize_webhook_billing_key
from .webhook_transaction import WebhookTransaction, _deserialize_webhook_transaction

Webhook = Union[WebhookTransaction, WebhookBillingKey, dict]


def _deserialize_webhook(obj: Any) -> Webhook:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key(obj)
    except Exception:
        pass
    return obj
