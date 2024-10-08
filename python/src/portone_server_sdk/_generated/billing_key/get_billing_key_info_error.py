from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetBillingKeyInfoError = Union[BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, UnauthorizedError]


def _serialize_get_billing_key_info_error(obj: GetBillingKeyInfoError) -> Any:
    if obj.type == "BILLING_KEY_NOT_FOUND":
        return _serialize_billing_key_not_found_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
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
