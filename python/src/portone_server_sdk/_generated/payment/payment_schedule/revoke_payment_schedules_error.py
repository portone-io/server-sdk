from __future__ import annotations
from typing import Any, Optional, Union
from ...common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from ...common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...payment.payment_schedule.payment_schedule_already_processed_error import PaymentScheduleAlreadyProcessedError, _deserialize_payment_schedule_already_processed_error, _serialize_payment_schedule_already_processed_error
from ...payment.payment_schedule.payment_schedule_already_revoked_error import PaymentScheduleAlreadyRevokedError, _deserialize_payment_schedule_already_revoked_error, _serialize_payment_schedule_already_revoked_error
from ...payment.payment_schedule.payment_schedule_not_found_error import PaymentScheduleNotFoundError, _deserialize_payment_schedule_not_found_error, _serialize_payment_schedule_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

RevokePaymentSchedulesError = Union[BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyProcessedError, PaymentScheduleAlreadyRevokedError, PaymentScheduleNotFoundError, UnauthorizedError, dict]


def _serialize_revoke_payment_schedules_error(obj: RevokePaymentSchedulesError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyAlreadyDeletedError):
        return _serialize_billing_key_already_deleted_error(obj)
    if isinstance(obj, BillingKeyNotFoundError):
        return _serialize_billing_key_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PaymentScheduleAlreadyProcessedError):
        return _serialize_payment_schedule_already_processed_error(obj)
    if isinstance(obj, PaymentScheduleAlreadyRevokedError):
        return _serialize_payment_schedule_already_revoked_error(obj)
    if isinstance(obj, PaymentScheduleNotFoundError):
        return _serialize_payment_schedule_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
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
