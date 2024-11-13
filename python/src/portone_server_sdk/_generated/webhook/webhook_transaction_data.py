from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from portone_server_sdk._generated.webhook.webhook_transaction_cancelled_data import WebhookTransactionCancelledData, _deserialize_webhook_transaction_cancelled_data
from portone_server_sdk._generated.webhook.webhook_transaction_data_cancel_pending import WebhookTransactionDataCancelPending, _deserialize_webhook_transaction_data_cancel_pending
from portone_server_sdk._generated.webhook.webhook_transaction_data_failed import WebhookTransactionDataFailed, _deserialize_webhook_transaction_data_failed
from portone_server_sdk._generated.webhook.webhook_transaction_data_paid import WebhookTransactionDataPaid, _deserialize_webhook_transaction_data_paid
from portone_server_sdk._generated.webhook.webhook_transaction_data_pay_pending import WebhookTransactionDataPayPending, _deserialize_webhook_transaction_data_pay_pending
from portone_server_sdk._generated.webhook.webhook_transaction_data_ready import WebhookTransactionDataReady, _deserialize_webhook_transaction_data_ready
from portone_server_sdk._generated.webhook.webhook_transaction_data_virtual_account_issued import WebhookTransactionDataVirtualAccountIssued, _deserialize_webhook_transaction_data_virtual_account_issued

WebhookTransactionData = Union[WebhookTransactionDataReady, WebhookTransactionDataPaid, WebhookTransactionDataVirtualAccountIssued, WebhookTransactionDataFailed, WebhookTransactionDataPayPending, WebhookTransactionDataCancelPending, WebhookTransactionCancelledData]


def _deserialize_webhook_transaction_data(obj: Any) -> WebhookTransactionData:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    try:
        return _deserialize_webhook_transaction_data_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_data_paid(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_data_virtual_account_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_data_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_data_pay_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_data_cancel_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_data(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookTransactionData")
