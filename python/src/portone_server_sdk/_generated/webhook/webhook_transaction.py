from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from portone_server_sdk._generated.webhook.webhook_transaction_cancel_pending import WebhookTransactionCancelPending, _deserialize_webhook_transaction_cancel_pending
from portone_server_sdk._generated.webhook.webhook_transaction_cancelled import WebhookTransactionCancelled, _deserialize_webhook_transaction_cancelled
from portone_server_sdk._generated.webhook.webhook_transaction_failed import WebhookTransactionFailed, _deserialize_webhook_transaction_failed
from portone_server_sdk._generated.webhook.webhook_transaction_paid import WebhookTransactionPaid, _deserialize_webhook_transaction_paid
from portone_server_sdk._generated.webhook.webhook_transaction_pay_pending import WebhookTransactionPayPending, _deserialize_webhook_transaction_pay_pending
from portone_server_sdk._generated.webhook.webhook_transaction_ready import WebhookTransactionReady, _deserialize_webhook_transaction_ready
from portone_server_sdk._generated.webhook.webhook_transaction_virtual_account_issued import WebhookTransactionVirtualAccountIssued, _deserialize_webhook_transaction_virtual_account_issued

WebhookTransaction = Union[WebhookTransactionReady, WebhookTransactionPaid, WebhookTransactionVirtualAccountIssued, WebhookTransactionFailed, WebhookTransactionPayPending, WebhookTransactionCancelPending, WebhookTransactionCancelled]


def _deserialize_webhook_transaction(obj: Any) -> WebhookTransaction:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_transaction_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_paid(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_virtual_account_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_pay_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancel_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookTransaction")