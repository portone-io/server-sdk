from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from portone_server_sdk._generated.payment.billing_key.billing_key_not_issued_error import BillingKeyNotIssuedError, _deserialize_billing_key_not_issued_error, _serialize_billing_key_not_issued_error
from portone_server_sdk._generated.payment.billing_key.channel_specific_error import ChannelSpecificError, _deserialize_channel_specific_error, _serialize_channel_specific_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeleteBillingKeyError = Union[BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, BillingKeyNotIssuedError, ChannelSpecificError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, PgProviderError, UnauthorizedError]


def _serialize_delete_billing_key_error(obj: DeleteBillingKeyError) -> Any:
    if obj.type == "BILLING_KEY_ALREADY_DELETED":
        return _serialize_billing_key_already_deleted_error(obj)
    if obj.type == "BILLING_KEY_NOT_FOUND":
        return _serialize_billing_key_not_found_error(obj)
    if obj.type == "BILLING_KEY_NOT_ISSUED":
        return _serialize_billing_key_not_issued_error(obj)
    if obj.type == "CHANNEL_SPECIFIC":
        return _serialize_channel_specific_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PAYMENT_SCHEDULE_ALREADY_EXISTS":
        return _serialize_payment_schedule_already_exists_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_delete_billing_key_error(obj: Any) -> DeleteBillingKeyError:
    try:
        return _deserialize_billing_key_already_deleted_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_billing_key_not_issued_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_channel_specific_error(obj)
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
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not DeleteBillingKeyError")
