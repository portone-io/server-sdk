from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.webhook.webhook_billing_key_request_deleted import WebhookBillingKeyRequestDeleted, _deserialize_webhook_billing_key_request_deleted, _serialize_webhook_billing_key_request_deleted
from portone_server_sdk._generated.webhook.webhook_billing_key_request_failed import WebhookBillingKeyRequestFailed, _deserialize_webhook_billing_key_request_failed, _serialize_webhook_billing_key_request_failed
from portone_server_sdk._generated.webhook.webhook_billing_key_request_issued import WebhookBillingKeyRequestIssued, _deserialize_webhook_billing_key_request_issued, _serialize_webhook_billing_key_request_issued
from portone_server_sdk._generated.webhook.webhook_billing_key_request_ready import WebhookBillingKeyRequestReady, _deserialize_webhook_billing_key_request_ready, _serialize_webhook_billing_key_request_ready
from portone_server_sdk._generated.webhook.webhook_billing_key_request_updated import WebhookBillingKeyRequestUpdated, _deserialize_webhook_billing_key_request_updated, _serialize_webhook_billing_key_request_updated
from portone_server_sdk._generated.webhook.webhook_transaction_request_cancel_pending import WebhookTransactionRequestCancelPending, _deserialize_webhook_transaction_request_cancel_pending, _serialize_webhook_transaction_request_cancel_pending
from portone_server_sdk._generated.webhook.webhook_transaction_request_cancelled import WebhookTransactionRequestCancelled, _deserialize_webhook_transaction_request_cancelled, _serialize_webhook_transaction_request_cancelled
from portone_server_sdk._generated.webhook.webhook_transaction_request_failed import WebhookTransactionRequestFailed, _deserialize_webhook_transaction_request_failed, _serialize_webhook_transaction_request_failed
from portone_server_sdk._generated.webhook.webhook_transaction_request_paid import WebhookTransactionRequestPaid, _deserialize_webhook_transaction_request_paid, _serialize_webhook_transaction_request_paid
from portone_server_sdk._generated.webhook.webhook_transaction_request_partial_cancelled import WebhookTransactionRequestPartialCancelled, _deserialize_webhook_transaction_request_partial_cancelled, _serialize_webhook_transaction_request_partial_cancelled
from portone_server_sdk._generated.webhook.webhook_transaction_request_pay_pending import WebhookTransactionRequestPayPending, _deserialize_webhook_transaction_request_pay_pending, _serialize_webhook_transaction_request_pay_pending
from portone_server_sdk._generated.webhook.webhook_transaction_request_ready import WebhookTransactionRequestReady, _deserialize_webhook_transaction_request_ready, _serialize_webhook_transaction_request_ready
from portone_server_sdk._generated.webhook.webhook_transaction_request_virtual_account_issued import WebhookTransactionRequestVirtualAccountIssued, _deserialize_webhook_transaction_request_virtual_account_issued, _serialize_webhook_transaction_request_virtual_account_issued

WebhookRequest = Union[WebhookTransactionRequestReady, WebhookTransactionRequestPaid, WebhookTransactionRequestVirtualAccountIssued, WebhookTransactionRequestPartialCancelled, WebhookTransactionRequestCancelled, WebhookTransactionRequestFailed, WebhookTransactionRequestPayPending, WebhookTransactionRequestCancelPending, WebhookBillingKeyRequestReady, WebhookBillingKeyRequestIssued, WebhookBillingKeyRequestFailed, WebhookBillingKeyRequestDeleted, WebhookBillingKeyRequestUpdated]
"""웹훅 형식
"""


def _serialize_webhook_request(obj: WebhookRequest) -> Any:
    if obj.type == "Transaction.Ready":
        return _serialize_webhook_transaction_request_ready(obj)
    if obj.type == "Transaction.Paid":
        return _serialize_webhook_transaction_request_paid(obj)
    if obj.type == "Transaction.VirtualAccountIssued":
        return _serialize_webhook_transaction_request_virtual_account_issued(obj)
    if obj.type == "Transaction.PartialCancelled":
        return _serialize_webhook_transaction_request_partial_cancelled(obj)
    if obj.type == "Transaction.Cancelled":
        return _serialize_webhook_transaction_request_cancelled(obj)
    if obj.type == "Transaction.Failed":
        return _serialize_webhook_transaction_request_failed(obj)
    if obj.type == "Transaction.PayPending":
        return _serialize_webhook_transaction_request_pay_pending(obj)
    if obj.type == "Transaction.CancelPending":
        return _serialize_webhook_transaction_request_cancel_pending(obj)
    if obj.type == "BillingKey.Ready":
        return _serialize_webhook_billing_key_request_ready(obj)
    if obj.type == "BillingKey.Issued":
        return _serialize_webhook_billing_key_request_issued(obj)
    if obj.type == "BillingKey.Failed":
        return _serialize_webhook_billing_key_request_failed(obj)
    if obj.type == "BillingKey.Deleted":
        return _serialize_webhook_billing_key_request_deleted(obj)
    if obj.type == "BillingKey.Updated":
        return _serialize_webhook_billing_key_request_updated(obj)


def _deserialize_webhook_request(obj: Any) -> WebhookRequest:
    try:
        return _deserialize_webhook_transaction_request_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_paid(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_virtual_account_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_partial_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_pay_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_transaction_request_cancel_pending(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_request_ready(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_request_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_request_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_request_deleted(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_billing_key_request_updated(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not WebhookRequest")
