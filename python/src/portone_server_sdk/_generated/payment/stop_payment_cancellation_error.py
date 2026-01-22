from __future__ import annotations
from typing import Any, Optional, Union
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..payment.payment_cancellation_not_found_error import PaymentCancellationNotFoundError, _deserialize_payment_cancellation_not_found_error, _serialize_payment_cancellation_not_found_error
from ..payment.payment_cancellation_not_pending_error import PaymentCancellationNotPendingError, _deserialize_payment_cancellation_not_pending_error, _serialize_payment_cancellation_not_pending_error
from ..payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from ..common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

StopPaymentCancellationError = Union[ForbiddenError, InvalidRequestError, PaymentCancellationNotFoundError, PaymentCancellationNotPendingError, PaymentNotFoundError, PgProviderError, UnauthorizedError, dict]


def _serialize_stop_payment_cancellation_error(obj: StopPaymentCancellationError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PaymentCancellationNotFoundError):
        return _serialize_payment_cancellation_not_found_error(obj)
    if isinstance(obj, PaymentCancellationNotPendingError):
        return _serialize_payment_cancellation_not_pending_error(obj)
    if isinstance(obj, PaymentNotFoundError):
        return _serialize_payment_not_found_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_stop_payment_cancellation_error(obj: Any) -> StopPaymentCancellationError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_cancellation_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_cancellation_not_pending_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_not_found_error(obj)
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
    raise ValueError(f"{repr(obj)} is not StopPaymentCancellationError")
