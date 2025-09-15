from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.already_paid_error import AlreadyPaidError, _deserialize_already_paid_error, _serialize_already_paid_error
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.information_mismatch_error import InformationMismatchError, _deserialize_information_mismatch_error, _serialize_information_mismatch_error
from ..payment.invalid_payment_token_error import InvalidPaymentTokenError, _deserialize_invalid_payment_token_error, _serialize_invalid_payment_token_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from ..common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

ConfirmPaymentError = Union[AlreadyPaidError, ForbiddenError, InformationMismatchError, InvalidPaymentTokenError, InvalidRequestError, PaymentNotFoundError, PgProviderError, UnauthorizedError, dict]


def _serialize_confirm_payment_error(obj: ConfirmPaymentError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, AlreadyPaidError):
        return _serialize_already_paid_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InformationMismatchError):
        return _serialize_information_mismatch_error(obj)
    if isinstance(obj, InvalidPaymentTokenError):
        return _serialize_invalid_payment_token_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PaymentNotFoundError):
        return _serialize_payment_not_found_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_confirm_payment_error(obj: Any) -> ConfirmPaymentError:
    try:
        return _deserialize_already_paid_error(obj)
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
        return _deserialize_invalid_payment_token_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
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
    raise ValueError(f"{repr(obj)} is not ConfirmPaymentError")
