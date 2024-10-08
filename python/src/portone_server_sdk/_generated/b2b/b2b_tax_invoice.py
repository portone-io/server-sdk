from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.b2b_tax_invoice_before_sending import B2bTaxInvoiceBeforeSending, _deserialize_b2b_tax_invoice_before_sending, _serialize_b2b_tax_invoice_before_sending
from portone_server_sdk._generated.b2b.b2b_tax_invoice_issuance_cancelled import B2bTaxInvoiceIssuanceCancelled, _deserialize_b2b_tax_invoice_issuance_cancelled, _serialize_b2b_tax_invoice_issuance_cancelled
from portone_server_sdk._generated.b2b.b2b_tax_invoice_issued import B2bTaxInvoiceIssued, _deserialize_b2b_tax_invoice_issued, _serialize_b2b_tax_invoice_issued
from portone_server_sdk._generated.b2b.b2b_tax_invoice_registered import B2bTaxInvoiceRegistered, _deserialize_b2b_tax_invoice_registered, _serialize_b2b_tax_invoice_registered
from portone_server_sdk._generated.b2b.b2b_tax_invoice_request_cancelled import B2bTaxInvoiceRequestCancelled, _deserialize_b2b_tax_invoice_request_cancelled, _serialize_b2b_tax_invoice_request_cancelled
from portone_server_sdk._generated.b2b.b2b_tax_invoice_request_refused import B2bTaxInvoiceRequestRefused, _deserialize_b2b_tax_invoice_request_refused, _serialize_b2b_tax_invoice_request_refused
from portone_server_sdk._generated.b2b.b2b_tax_invoice_requested import B2bTaxInvoiceRequested, _deserialize_b2b_tax_invoice_requested, _serialize_b2b_tax_invoice_requested
from portone_server_sdk._generated.b2b.b2b_tax_invoice_sending import B2bTaxInvoiceSending, _deserialize_b2b_tax_invoice_sending, _serialize_b2b_tax_invoice_sending
from portone_server_sdk._generated.b2b.b2b_tax_invoice_sending_completed import B2bTaxInvoiceSendingCompleted, _deserialize_b2b_tax_invoice_sending_completed, _serialize_b2b_tax_invoice_sending_completed
from portone_server_sdk._generated.b2b.b2b_tax_invoice_sending_failed import B2bTaxInvoiceSendingFailed, _deserialize_b2b_tax_invoice_sending_failed, _serialize_b2b_tax_invoice_sending_failed
from portone_server_sdk._generated.b2b.b2b_tax_invoice_waiting_sending import B2bTaxInvoiceWaitingSending, _deserialize_b2b_tax_invoice_waiting_sending, _serialize_b2b_tax_invoice_waiting_sending

B2bTaxInvoice = Union[B2bTaxInvoiceBeforeSending, B2bTaxInvoiceIssuanceCancelled, B2bTaxInvoiceRequestRefused, B2bTaxInvoiceIssued, B2bTaxInvoiceRegistered, B2bTaxInvoiceRequested, B2bTaxInvoiceRequestCancelled, B2bTaxInvoiceSending, B2bTaxInvoiceSendingCompleted, B2bTaxInvoiceSendingFailed, B2bTaxInvoiceWaitingSending]


def _serialize_b2b_tax_invoice(obj: B2bTaxInvoice) -> Any:
    if obj.status == "BEFORE_SENDING":
        return _serialize_b2b_tax_invoice_before_sending(obj)
    if obj.status == "ISSUANCE_CANCELLED":
        return _serialize_b2b_tax_invoice_issuance_cancelled(obj)
    if obj.status == "ISSUANCE_REFUSED":
        return _serialize_b2b_tax_invoice_request_refused(obj)
    if obj.status == "ISSUED":
        return _serialize_b2b_tax_invoice_issued(obj)
    if obj.status == "REGISTERED":
        return _serialize_b2b_tax_invoice_registered(obj)
    if obj.status == "REQUESTED":
        return _serialize_b2b_tax_invoice_requested(obj)
    if obj.status == "REQUEST_CANCELLED":
        return _serialize_b2b_tax_invoice_request_cancelled(obj)
    if obj.status == "SENDING":
        return _serialize_b2b_tax_invoice_sending(obj)
    if obj.status == "SENDING_COMPLETED":
        return _serialize_b2b_tax_invoice_sending_completed(obj)
    if obj.status == "SENDING_FAILED":
        return _serialize_b2b_tax_invoice_sending_failed(obj)
    if obj.status == "WAITING_SENDING":
        return _serialize_b2b_tax_invoice_waiting_sending(obj)


def _deserialize_b2b_tax_invoice(obj: Any) -> B2bTaxInvoice:
    try:
        return _deserialize_b2b_tax_invoice_before_sending(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_issuance_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_request_refused(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_issued(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_registered(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_requested(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_request_cancelled(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_sending(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_sending_completed(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_sending_failed(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_waiting_sending(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not B2bTaxInvoice")
