from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_processed_error import PaymentScheduleAlreadyProcessedError, _deserialize_payment_schedule_already_processed_error, _serialize_payment_schedule_already_processed_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_revoked_error import PaymentScheduleAlreadyRevokedError, _deserialize_payment_schedule_already_revoked_error, _serialize_payment_schedule_already_revoked_error
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_not_found_error import PaymentScheduleNotFoundError, _deserialize_payment_schedule_not_found_error, _serialize_payment_schedule_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

RevokePaymentSchedulesError = Union[BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyProcessedError, PaymentScheduleAlreadyRevokedError, PaymentScheduleNotFoundError, UnauthorizedError]


def _serialize_revoke_payment_schedules_error(obj: RevokePaymentSchedulesError) -> Any:
    if obj.type == "BILLING_KEY_ALREADY_DELETED":
        return _serialize_billing_key_already_deleted_error(obj)
    if obj.type == "BILLING_KEY_NOT_FOUND":
        return _serialize_billing_key_not_found_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
        return _serialize_payment_schedule_already_processed_error(obj)
    if obj.type == "PAYMENT_SCHEDULE_ALREADY_REVOKED":
        return _serialize_payment_schedule_already_revoked_error(obj)
    if obj.type == "PAYMENT_SCHEDULE_NOT_FOUND":
        return _serialize_payment_schedule_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_revoke_payment_schedules_error(obj: Any) -> RevokePaymentSchedulesError:
    try:
        return _deserialize_billing_key_already_deleted_error(obj)
    except Exception:
        pass
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
        return _deserialize_payment_schedule_already_processed_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_schedule_already_revoked_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_payment_schedule_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not RevokePaymentSchedulesError")
