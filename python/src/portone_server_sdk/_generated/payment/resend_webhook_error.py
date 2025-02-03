from __future__ import annotations
from typing import Any, Optional, Union
from ..common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..payment.max_webhook_retry_count_reached_error import MaxWebhookRetryCountReachedError, _deserialize_max_webhook_retry_count_reached_error, _serialize_max_webhook_retry_count_reached_error
from ..payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from ..payment.webhook_not_found_error import WebhookNotFoundError, _deserialize_webhook_not_found_error, _serialize_webhook_not_found_error

ResendWebhookError = Union[ForbiddenError, InvalidRequestError, MaxWebhookRetryCountReachedError, PaymentNotFoundError, UnauthorizedError, WebhookNotFoundError, dict]


def _serialize_resend_webhook_error(obj: ResendWebhookError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, MaxWebhookRetryCountReachedError):
        return _serialize_max_webhook_retry_count_reached_error(obj)
    if isinstance(obj, PaymentNotFoundError):
        return _serialize_payment_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)
    if isinstance(obj, WebhookNotFoundError):
        return _serialize_webhook_not_found_error(obj)


def _deserialize_resend_webhook_error(obj: Any) -> ResendWebhookError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_max_webhook_retry_count_reached_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_webhook_not_found_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not ResendWebhookError")
