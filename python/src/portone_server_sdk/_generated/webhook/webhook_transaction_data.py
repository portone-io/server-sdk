from __future__ import annotations
from typing import Any, Optional, Union
from dataclasses import dataclass, field
from .webhook_transaction_cancelled_data import WebhookTransactionCancelledData, _deserialize_webhook_transaction_cancelled_data
from .webhook_transaction_data_confirm import WebhookTransactionDataConfirm, _deserialize_webhook_transaction_data_confirm
from .webhook_transaction_data_failed import WebhookTransactionDataFailed, _deserialize_webhook_transaction_data_failed
from .webhook_transaction_data_paid import WebhookTransactionDataPaid, _deserialize_webhook_transaction_data_paid
from .webhook_transaction_data_pay_pending import WebhookTransactionDataPayPending, _deserialize_webhook_transaction_data_pay_pending
from .webhook_transaction_data_ready import WebhookTransactionDataReady, _deserialize_webhook_transaction_data_ready
from .webhook_transaction_data_virtual_account_issued import WebhookTransactionDataVirtualAccountIssued, _deserialize_webhook_transaction_data_virtual_account_issued

WebhookTransactionData = Union[WebhookTransactionDataReady, WebhookTransactionDataPaid, WebhookTransactionDataVirtualAccountIssued, WebhookTransactionDataFailed, WebhookTransactionDataPayPending, WebhookTransactionDataConfirm, WebhookTransactionCancelledData]


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
        return _deserialize_webhook_transaction_data_confirm(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_cancelled_data(obj)
    except Exception:
        pass
    raise ValueError(f"{obj} is not WebhookTransactionData")
