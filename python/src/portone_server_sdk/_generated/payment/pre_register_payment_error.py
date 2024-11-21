from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.already_paid_error import AlreadyPaidError, _deserialize_already_paid_error, _serialize_already_paid_error
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

PreRegisterPaymentError = Union[AlreadyPaidError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_pre_register_payment_error(obj: PreRegisterPaymentError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, AlreadyPaidError):
        return _serialize_already_paid_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_pre_register_payment_error(obj: Any) -> PreRegisterPaymentError:
    try:
        return _deserialize_already_paid_error(obj)
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
    return obj
