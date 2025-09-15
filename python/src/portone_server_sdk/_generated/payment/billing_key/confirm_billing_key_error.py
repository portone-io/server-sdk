from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.billing_key.billing_key_already_issued_error import BillingKeyAlreadyIssuedError, _deserialize_billing_key_already_issued_error, _serialize_billing_key_already_issued_error
from ...common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.information_mismatch_error import InformationMismatchError, _deserialize_information_mismatch_error, _serialize_information_mismatch_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ConfirmBillingKeyError = Union[BillingKeyAlreadyIssuedError, BillingKeyNotFoundError, ForbiddenError, InformationMismatchError, InvalidRequestError, PgProviderError, UnauthorizedError, dict]


def _serialize_confirm_billing_key_error(obj: ConfirmBillingKeyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyAlreadyIssuedError):
        return _serialize_billing_key_already_issued_error(obj)
    if isinstance(obj, BillingKeyNotFoundError):
        return _serialize_billing_key_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InformationMismatchError):
        return _serialize_information_mismatch_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_confirm_billing_key_error(obj: Any) -> ConfirmBillingKeyError:
    try:
        return _deserialize_billing_key_already_issued_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_information_mismatch_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ConfirmBillingKeyError")
