from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_billing_key_data_deleted import WebhookBillingKeyDataDeleted, _deserialize_webhook_billing_key_data_deleted
from .webhook_billing_key_data_failed import WebhookBillingKeyDataFailed, _deserialize_webhook_billing_key_data_failed
from .webhook_billing_key_data_issued import WebhookBillingKeyDataIssued, _deserialize_webhook_billing_key_data_issued
from .webhook_billing_key_data_ready import WebhookBillingKeyDataReady, _deserialize_webhook_billing_key_data_ready
from .webhook_billing_key_data_updated import WebhookBillingKeyDataUpdated, _deserialize_webhook_billing_key_data_updated

WebhookBillingKeyData = Union[WebhookBillingKeyDataReady, WebhookBillingKeyDataIssued, WebhookBillingKeyDataFailed, WebhookBillingKeyDataDeleted, WebhookBillingKeyDataUpdated]


def _deserialize_webhook_billing_key_data(obj: Any) -> WebhookBillingKeyData:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_billing_key_data_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_data_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_data_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_data_deleted(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_data_updated(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookBillingKeyData")
