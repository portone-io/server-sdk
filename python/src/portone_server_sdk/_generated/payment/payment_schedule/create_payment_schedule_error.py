from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.payment_schedule.already_paid_or_waiting_error import AlreadyPaidOrWaitingError, _deserialize_already_paid_or_waiting_error, _serialize_already_paid_or_waiting_error
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from portone_server_sdk._generated.common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError, _deserialize_sum_of_parts_exceeds_total_amount_error, _serialize_sum_of_parts_exceeds_total_amount_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePaymentScheduleError = Union[AlreadyPaidOrWaitingError, BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, SumOfPartsExceedsTotalAmountError, UnauthorizedError]


def _serialize_create_payment_schedule_error(obj: CreatePaymentScheduleError) -> Any:
    if obj.type == "ALREADY_PAID_OR_WAITING":
        return _serialize_already_paid_or_waiting_error(obj)
    if obj.type == "BILLING_KEY_ALREADY_DELETED":
        return _serialize_billing_key_already_deleted_error(obj)
    if obj.type == "BILLING_KEY_NOT_FOUND":
        return _serialize_billing_key_not_found_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
        return _serialize_payment_schedule_already_exists_error(obj)
    if obj.type == "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
        return _serialize_sum_of_parts_exceeds_total_amount_error(obj)
    if obj.type == "UNAUTHORIZED":
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
