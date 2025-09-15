from __future__ import annotations
from typing import Any, Optional, Union
from ...b2b.tax_invoice.b2b_bulk_tax_invoice_not_found_error import B2bBulkTaxInvoiceNotFoundError, _deserialize_b2b_bulk_tax_invoice_not_found_error, _serialize_b2b_bulk_tax_invoice_not_found_error
from ...common.b2b_external_service_error import B2bExternalServiceError, _deserialize_b2b_external_service_error, _serialize_b2b_external_service_error
from ...common.b2b_not_enabled_error import B2bNotEnabledError, _deserialize_b2b_not_enabled_error, _serialize_b2b_not_enabled_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetB2bBulkTaxInvoiceError = Union[B2bBulkTaxInvoiceNotFoundError, B2bExternalServiceError, B2bNotEnabledError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_get_b2b_bulk_tax_invoice_error(obj: GetB2bBulkTaxInvoiceError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, B2bBulkTaxInvoiceNotFoundError):
        return _serialize_b2b_bulk_tax_invoice_not_found_error(obj)
    if isinstance(obj, B2bExternalServiceError):
        return _serialize_b2b_external_service_error(obj)
    if isinstance(obj, B2bNotEnabledError):
        return _serialize_b2b_not_enabled_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_b2b_bulk_tax_invoice_error(obj: Any) -> GetB2bBulkTaxInvoiceError:
    try:
        return _deserialize_b2b_bulk_tax_invoice_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_external_service_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_b2b_not_enabled_error(obj)
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
    raise ValueError(f"{repr(obj)} is not GetB2bBulkTaxInvoiceError")
