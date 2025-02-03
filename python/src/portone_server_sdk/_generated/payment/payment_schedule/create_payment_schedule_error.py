from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.payment_schedule.already_paid_or_waiting_error import AlreadyPaidOrWaitingError, _deserialize_already_paid_or_waiting_error, _serialize_already_paid_or_waiting_error
from ...common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from ...common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from ...common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePaymentScheduleError = Union[AlreadyPaidOrWaitingError, BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, SumOfPartsExceedsTotalAmountError, UnauthorizedError, dict]


def _serialize_create_payment_schedule_error(obj: CreatePaymentScheduleError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, AlreadyPaidOrWaitingError):
        return _serialize_already_paid_or_waiting_error(obj)
    if isinstance(obj, BillingKeyAlreadyDeletedError):
        return _serialize_billing_key_already_deleted_error(obj)
    if isinstance(obj, BillingKeyNotFoundError):
        return _serialize_billing_key_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PaymentScheduleAlreadyExistsError):
        return _serialize_payment_schedule_already_exists_error(obj)
    if isinstance(obj, SumOfPartsExceedsTotalAmountError):
        return _serialize_sum_of_parts_exceeds_total_amount_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_create_payment_schedule_error(obj: Any) -> CreatePaymentScheduleError:
    try:
        return _deserialize_already_paid_or_waiting_error(obj)
    except Exception:
        pass
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
        return _deserialize_payment_schedule_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_sum_of_parts_exceeds_total_amount_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CreatePaymentScheduleError")
