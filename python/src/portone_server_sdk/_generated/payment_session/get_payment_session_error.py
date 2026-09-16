from __future__ import annotations
from typing import Any, Optional, Union
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..payment_session.session_expired_error import SessionExpiredError, _deserialize_session_expired_error, _serialize_session_expired_error
from ..payment_session.session_not_found_error import SessionNotFoundError, _deserialize_session_not_found_error, _serialize_session_not_found_error

GetPaymentSessionError = Union[InvalidRequestError, SessionExpiredError, SessionNotFoundError, dict]


def _serialize_get_payment_session_error(obj: GetPaymentSessionError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, SessionExpiredError):
        return _serialize_session_expired_error(obj)
    if isinstance(obj, SessionNotFoundError):
        return _serialize_session_not_found_error(obj)


def _deserialize_get_payment_session_error(obj: Any) -> GetPaymentSessionError:
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_session_expired_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_session_not_found_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetPaymentSessionError")
