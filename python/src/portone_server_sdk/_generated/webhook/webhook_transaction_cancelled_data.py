from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_transaction_cancelled_data_cancel_pending import WebhookTransactionCancelledDataCancelPending, _deserialize_webhook_transaction_cancelled_data_cancel_pending
from .webhook_transaction_cancelled_data_cancelled import WebhookTransactionCancelledDataCancelled, _deserialize_webhook_transaction_cancelled_data_cancelled
from .webhook_transaction_cancelled_data_partial_cancelled import WebhookTransactionCancelledDataPartialCancelled, _deserialize_webhook_transaction_cancelled_data_partial_cancelled

WebhookTransactionCancelledData = Union[WebhookTransactionCancelledDataPartialCancelled, WebhookTransactionCancelledDataCancelled, WebhookTransactionCancelledDataCancelPending]


def _deserialize_webhook_transaction_cancelled_data(obj: Any) -> WebhookTransactionCancelledData:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_transaction_cancelled_data_partial_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_data_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_data_cancel_pending(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookTransactionCancelledData")
