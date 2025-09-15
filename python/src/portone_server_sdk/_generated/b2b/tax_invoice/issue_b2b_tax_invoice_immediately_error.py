from __future__ import annotations
from typing import Any, Optional, Union
from ...b2b.tax_invoice.b2b_cannot_change_tax_type_error import B2BCannotChangeTaxTypeError, _deserialize_b2b_cannot_change_tax_type_error, _serialize_b2b_cannot_change_tax_type_error
from ...b2b.tax_invoice.b2b_tax_invoice_status_not_sending_completed_error import B2BTaxInvoiceStatusNotSendingCompletedError, _deserialize_b2b_tax_invoice_status_not_sending_completed_error, _serialize_b2b_tax_invoice_status_not_sending_completed_error
from ...common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from ...b2b.tax_invoice.b2b_id_already_exists_error import B2bIdAlreadyExistsError, _deserialize_b2b_id_already_exists_error, _serialize_b2b_id_already_exists_error
from ...b2b.tax_invoice.b2b_issuance_type_mismatch_error import B2bIssuanceTypeMismatchError, _deserialize_b2b_issuance_type_mismatch_error, _serialize_b2b_issuance_type_mismatch_error
from ...b2b.tax_invoice.b2b_modification_not_provided_error import B2bModificationNotProvidedError, _deserialize_b2b_modification_not_provided_error, _serialize_b2b_modification_not_provided_error
from ...common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from ...b2b.tax_invoice.b2b_original_tax_invoice_not_found_error import B2bOriginalTaxInvoiceNotFoundError, _deserialize_b2b_original_tax_invoice_not_found_error, _serialize_b2b_original_tax_invoice_not_found_error
from ...b2b.tax_invoice.b2b_recipient_not_found_error import B2bRecipientNotFoundError, _deserialize_b2b_recipient_not_found_error, _serialize_b2b_recipient_not_found_error
from ...b2b.tax_invoice.b2b_supplier_not_found_error import B2bSupplierNotFoundError, _deserialize_b2b_supplier_not_found_error, _serialize_b2b_supplier_not_found_error
from ...b2b.tax_invoice.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from ...b2b.tax_invoice.b2b_tax_invoice_recipient_document_key_already_used_error import B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_recipient_document_key_already_used_error, _serialize_b2b_tax_invoice_recipient_document_key_already_used_error
from ...b2b.tax_invoice.b2b_tax_invoice_supplier_document_key_already_used_error import B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError, _deserialize_b2b_tax_invoice_supplier_document_key_already_used_error, _serialize_b2b_tax_invoice_supplier_document_key_already_used_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

IssueB2bTaxInvoiceImmediatelyError = Union[B2BCannotChangeTaxTypeError, B2bExternalServiceError, B2bIdAlreadyExistsError, B2bIssuanceTypeMismatchError, B2bModificationNotProvidedError, B2bNotEnabledError, B2bOriginalTaxInvoiceNotFoundError, B2bRecipientNotFoundError, B2bSupplierNotFoundError, B2bTaxInvoiceNotFoundError, B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError, B2BTaxInvoiceStatusNotSendingCompletedError, B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_issue_b2b_tax_invoice_immediately_error(obj: IssueB2bTaxInvoiceImmediatelyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, B2BCannotChangeTaxTypeError):
        return _serialize_b2b_cannot_change_tax_type_error(obj)
    if isinstance(obj, B2bExternalServiceError):
        return _serialize_b2b_external_service_error(obj)
    if isinstance(obj, B2bIdAlreadyExistsError):
        return _serialize_b2b_id_already_exists_error(obj)
    if isinstance(obj, B2bIssuanceTypeMismatchError):
        return _serialize_b2b_issuance_type_mismatch_error(obj)
    if isinstance(obj, B2bModificationNotProvidedError):
        return _serialize_b2b_modification_not_provided_error(obj)
    if isinstance(obj, B2bNotEnabledError):
        return _serialize_b2b_not_enabled_error(obj)
    if isinstance(obj, B2bOriginalTaxInvoiceNotFoundError):
        return _serialize_b2b_original_tax_invoice_not_found_error(obj)
    if isinstance(obj, B2bRecipientNotFoundError):
        return _serialize_b2b_recipient_not_found_error(obj)
    if isinstance(obj, B2bSupplierNotFoundError):
        return _serialize_b2b_supplier_not_found_error(obj)
    if isinstance(obj, B2bTaxInvoiceNotFoundError):
        return _serialize_b2b_tax_invoice_not_found_error(obj)
    if isinstance(obj, B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError):
        return _serialize_b2b_tax_invoice_recipient_document_key_already_used_error(obj)
    if isinstance(obj, B2BTaxInvoiceStatusNotSendingCompletedError):
        return _serialize_b2b_tax_invoice_status_not_sending_completed_error(obj)
    if isinstance(obj, B2bTaxInvoiceSupplierDocumentKeyAlreadyUsedError):
        return _serialize_b2b_tax_invoice_supplier_document_key_already_used_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_issue_b2b_tax_invoice_immediately_error(obj: Any) -> IssueB2bTaxInvoiceImmediatelyError:
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
        return _deserialize_b2b_issuance_type_mismatch_error(obj)
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
    raise ValueError(f"{repr(obj)} is not IssueB2bTaxInvoiceImmediatelyError")
