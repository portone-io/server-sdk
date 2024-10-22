from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.max_webhook_retry_count_reached_error import MaxWebhookRetryCountReachedError, _deserialize_max_webhook_retry_count_reached_error, _serialize_max_webhook_retry_count_reached_error
from portone_server_sdk._generated.payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error
from portone_server_sdk._generated.payment.webhook_not_found_error import WebhookNotFoundError, _deserialize_webhook_not_found_error, _serialize_webhook_not_found_error

ResendWebhookError = Union[ForbiddenError, InvalidRequestError, MaxWebhookRetryCountReachedError, PaymentNotFoundError, UnauthorizedError, WebhookNotFoundError]


def _serialize_resend_webhook_error(obj: ResendWebhookError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "MAX_WEBHOOK_RETRY_COUNT_REACHED":
        return _serialize_max_webhook_retry_count_reached_error(obj)
    if obj.type == "PAYMENT_NOT_FOUND":
        return _serialize_payment_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)
    if obj.type == "WEBHOOK_NOT_FOUND":
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
