from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_billing_key_deleted import WebhookBillingKeyDeleted, _deserialize_webhook_billing_key_deleted
from .webhook_billing_key_failed import WebhookBillingKeyFailed, _deserialize_webhook_billing_key_failed
from .webhook_billing_key_issued import WebhookBillingKeyIssued, _deserialize_webhook_billing_key_issued
from .webhook_billing_key_ready import WebhookBillingKeyReady, _deserialize_webhook_billing_key_ready
from .webhook_billing_key_updated import WebhookBillingKeyUpdated, _deserialize_webhook_billing_key_updated

WebhookBillingKey = Union[WebhookBillingKeyReady, WebhookBillingKeyIssued, WebhookBillingKeyFailed, WebhookBillingKeyDeleted, WebhookBillingKeyUpdated]


def _deserialize_webhook_billing_key(obj: Any) -> WebhookBillingKey:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_billing_key_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_deleted(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_updated(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookBillingKey")
