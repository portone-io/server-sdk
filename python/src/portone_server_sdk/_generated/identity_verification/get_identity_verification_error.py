from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.identity_verification.identity_verification_not_found_error import IdentityVerificationNotFoundError, _deserialize_identity_verification_not_found_error, _serialize_identity_verification_not_found_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetIdentityVerificationError = Union[ForbiddenError, IdentityVerificationNotFoundError, InvalidRequestError, UnauthorizedError]


def _serialize_get_identity_verification_error(obj: GetIdentityVerificationError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "IDENTITY_VERIFICATION_NOT_FOUND":
        return _serialize_identity_verification_not_found_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_get_identity_verification_error(obj: Any) -> GetIdentityVerificationError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_identity_verification_not_found_error(obj)
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
    raise ValueError(f"{repr(obj)} is not GetIdentityVerificationError")
