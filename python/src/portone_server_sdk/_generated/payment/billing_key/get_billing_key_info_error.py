from __future__ import annotations
from typing import Any, Optional, Union
from ...common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetBillingKeyInfoError = Union[BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_get_billing_key_info_error(obj: GetBillingKeyInfoError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyNotFoundError):
        return _serialize_billing_key_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_billing_key_info_error(obj: Any) -> GetBillingKeyInfoError:
    try:
        return _deserialize_billing_key_not_found_error(obj)
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
    raise ValueError(f"{repr(obj)} is not GetBillingKeyInfoError")
