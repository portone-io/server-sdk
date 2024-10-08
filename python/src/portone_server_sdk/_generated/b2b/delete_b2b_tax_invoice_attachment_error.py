from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.b2b.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_attachment_not_found_error import B2bTaxInvoiceAttachmentNotFoundError, _deserialize_b2b_tax_invoice_attachment_not_found_error, _serialize_b2b_tax_invoice_attachment_not_found_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.b2b_tax_invoice_not_registered_status_error import B2bTaxInvoiceNotRegisteredStatusError, _deserialize_b2b_tax_invoice_not_registered_status_error, _serialize_b2b_tax_invoice_not_registered_status_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeleteB2bTaxInvoiceAttachmentError = Union[B2bExternalServiceError, B2bNotEnabledError, B2bTaxInvoiceAttachmentNotFoundError, B2bTaxInvoiceNotFoundError, B2bTaxInvoiceNotRegisteredStatusError, InvalidRequestError, UnauthorizedError]


def _serialize_delete_b2b_tax_invoice_attachment_error(obj: DeleteB2bTaxInvoiceAttachmentError) -> Any:
    if obj.type == "B2B_EXTERNAL_SERVICE":
        return _serialize_b2b_external_service_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
        return _serialize_b2b_tax_invoice_attachment_not_found_error(obj)
    if obj.type == "B2B_TAX_INVOICE_NOT_FOUND":
        return _serialize_b2b_tax_invoice_not_found_error(obj)
    if obj.type == "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
        return _serialize_b2b_tax_invoice_not_registered_status_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_delete_b2b_tax_invoice_attachment_error(obj: Any) -> DeleteB2bTaxInvoiceAttachmentError:
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_attachment_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_not_registered_status_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not DeleteB2bTaxInvoiceAttachmentError")
