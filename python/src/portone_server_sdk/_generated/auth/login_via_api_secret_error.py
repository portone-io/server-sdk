from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

LoginViaApiSecretError = Union[InvalidRequestError, UnauthorizedError]


def _serialize_login_via_api_secret_error(obj: LoginViaApiSecretError) -> Any:
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_login_via_api_secret_error(obj: Any) -> LoginViaApiSecretError:
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not LoginViaApiSecretError")
