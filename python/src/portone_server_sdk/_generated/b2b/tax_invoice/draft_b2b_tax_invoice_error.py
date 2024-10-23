from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.b2b.tax_invoice.b2b_cannot_change_tax_type_error import B2BCannotChangeTaxTypeError, _deserialize_b2b_cannot_change_tax_type_error, _serialize_b2b_cannot_change_tax_type_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_status_not_sending_completed_error import B2BTaxInvoiceStatusNotSendingCompletedError, _deserialize_b2b_tax_invoice_status_not_sending_completed_error, _serialize_b2b_tax_invoice_status_not_sending_completed_error
from portone_server_sdk._generated.common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from portone_server_sdk._generated.common.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_modification_not_provided_error import B2bModificationNotProvidedError, _deserialize_b2b_modification_not_provided_error, _serialize_b2b_modification_not_provided_error
from portone_server_sdk._generated.common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_original_tax_invoice_not_found_error import B2bOriginalTaxInvoiceNotFoundError, _deserialize_b2b_original_tax_invoice_not_found_error, _serialize_b2b_original_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_recipient_not_found_error import B2bRecipientNotFoundError, _deserialize_b2b_recipient_not_found_error, _serialize_b2b_recipient_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_supplier_not_found_error import B2bSupplierNotFoundError, _deserialize_b2b_supplier_not_found_error, _serialize_b2b_supplier_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_recipient_document_key_already_used_error import B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_recipient_document_key_already_used_error, _serialize_b2b_tax_invoice_recipient_document_key_already_used_error
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_supplier_document_key_already_used_error import B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_supplier_document_key_already_used_error, _serialize_b2b_tax_invoice_supplier_document_key_already_used_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DraftB2bTaxInvoiceError = Union[B2BCannotChangeTaxTypeError, B2bExternalServiceError, B2bIdAlreadyExistsError, B2bModificationNotProvidedError, B2bNotEnabledError, B2bOriginalTaxInvoiceNotFoundError, B2bRecipientNotFoundError, B2bSupplierNotFoundError, B2bTaxInvoiceNotFoundError, B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError, B2BTaxInvoiceStatusNotSendingCompletedError, B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError, ForbiddenError, InvalidRequestError, UnauthorizedError]


def _serialize_draft_b2b_tax_invoice_error(obj: DraftB2bTaxInvoiceError) -> Any:
    if obj.type == "B2B_CANNOT_CHANGE_TAX_TYPE":
        return _serialize_b2b_cannot_change_tax_type_error(obj)
    if obj.type == "B2B_EXTERNAL_SERVICE":
        return _serialize_b2b_external_service_error(obj)
    if obj.type == "B2B_ID_ALREADY_EXISTS":
        return _serialize_b2b_id_already_exists_error(obj)
    if obj.type == "B2B_MODIFICATION_NOT_PROVIDED":
        return _serialize_b2b_modification_not_provided_error(obj)
    if obj.type == "B2B_NOT_ENABLED":
        return _serialize_b2b_not_enabled_error(obj)
    if obj.type == "B2B_ORIGINAL_TAX_INVOICE_NOT_FOUND":
        return _serialize_b2b_original_tax_invoice_not_found_error(obj)
    if obj.type == "B2B_RECIPIENT_NOT_FOUND":
        return _serialize_b2b_recipient_not_found_error(obj)
    if obj.type == "B2B_SUPPLIER_NOT_FOUND":
        return _serialize_b2b_supplier_not_found_error(obj)
    if obj.type == "B2B_TAX_INVOICE_NOT_FOUND":
        return _serialize_b2b_tax_invoice_not_found_error(obj)
    if obj.type == "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED":
        return _serialize_b2b_tax_invoice_recipient_document_key_already_used_error(obj)
    if obj.type == "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED":
        return _serialize_b2b_tax_invoice_status_not_sending_completed_error(obj)
    if obj.type == "B2B_TAX_INVOICE_SUPPLIER_DOCUMENT_KEY_ALREADY_USED":
        return _serialize_b2b_tax_invoice_supplier_document_key_already_used_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_draft_b2b_tax_invoice_error(obj: Any) -> DraftB2bTaxInvoiceError:
    try:
        return _deserialize_b2b_cannot_change_tax_type_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_id_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_modification_not_provided_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_original_tax_invoice_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_recipient_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_supplier_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_recipient_document_key_already_used_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_status_not_sending_completed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_supplier_document_key_already_used_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_forbidden_error(obj)
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
    raise ValueError(f"{repr(obj)} is not DraftB2bTaxInvoiceError")
