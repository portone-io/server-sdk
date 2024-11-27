from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_transaction_cancelled_cancel_pending import WebhookTransactionCancelledCancelPending, _deserialize_webhook_transaction_cancelled_cancel_pending
from .webhook_transaction_cancelled_cancelled import WebhookTransactionCancelledCancelled, _deserialize_webhook_transaction_cancelled_cancelled
from .webhook_transaction_cancelled_partial_cancelled import WebhookTransactionCancelledPartialCancelled, _deserialize_webhook_transaction_cancelled_partial_cancelled

WebhookTransactionCancelled = Union[WebhookTransactionCancelledPartialCancelled, WebhookTransactionCancelledCancelled, WebhookTransactionCancelledCancelPending]


def _deserialize_webhook_transaction_cancelled(obj: Any) -> WebhookTransactionCancelled:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_transaction_cancelled_partial_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_cancel_pending(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookTransactionCancelled")
