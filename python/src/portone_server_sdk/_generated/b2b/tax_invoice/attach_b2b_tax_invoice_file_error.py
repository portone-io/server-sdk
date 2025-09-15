from __future__ import annotations
from typing import Any, Optional, Union
from ...common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from ...b2b.tax_invoice.b2b_file_not_found_error import B2bFileNotFoundError, _deserialize_b2b_file_not_found_error, _serialize_b2b_file_not_found_error
from ...common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from ...b2b.tax_invoice.b2b_tax_invoice_not_drafted_status_error import B2bTaxInvoiceNotDraftedStatusError, _deserialize_b2b_tax_invoice_not_drafted_status_error, _serialize_b2b_tax_invoice_not_drafted_status_error
from ...b2b.tax_invoice.b2b_tax_invoice_not_found_error import B2bTaxInvoiceNotFoundError, _deserialize_b2b_tax_invoice_not_found_error, _serialize_b2b_tax_invoice_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

AttachB2bTaxInvoiceFileError = Union[B2bExternalServiceError, B2bFileNotFoundError, B2bNotEnabledError, B2bTaxInvoiceNotDraftedStatusError, B2bTaxInvoiceNotFoundError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_attach_b2b_tax_invoice_file_error(obj: AttachB2bTaxInvoiceFileError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, B2bExternalServiceError):
        return _serialize_b2b_external_service_error(obj)
    if isinstance(obj, B2bFileNotFoundError):
        return _serialize_b2b_file_not_found_error(obj)
    if isinstance(obj, B2bNotEnabledError):
        return _serialize_b2b_not_enabled_error(obj)
    if isinstance(obj, B2bTaxInvoiceNotDraftedStatusError):
        return _serialize_b2b_tax_invoice_not_drafted_status_error(obj)
    if isinstance(obj, B2bTaxInvoiceNotFoundError):
        return _serialize_b2b_tax_invoice_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_attach_b2b_tax_invoice_file_error(obj: Any) -> AttachB2bTaxInvoiceFileError:
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_file_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_not_drafted_status_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_tax_invoice_not_found_error(obj)
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
    raise ValueError(f"{repr(obj)} is not AttachB2bTaxInvoiceFileError")
