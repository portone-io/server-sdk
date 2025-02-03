from __future__ import annotations
from typing import Any, Optional, Union
from ...common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError, _deserialize_billing_key_already_deleted_error, _serialize_billing_key_already_deleted_error
from ...common.billing_key_not_found_error import BillingKeyNotFoundError, _deserialize_billing_key_not_found_error, _serialize_billing_key_not_found_error
from ...payment.billing_key.billing_key_not_issued_error import BillingKeyNotIssuedError, _deserialize_billing_key_not_issued_error, _serialize_billing_key_not_issued_error
from ...payment.billing_key.channel_specific_error import ChannelSpecificError, _deserialize_channel_specific_error, _serialize_channel_specific_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError, _deserialize_payment_schedule_already_exists_error, _serialize_payment_schedule_already_exists_error
from ...common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

DeleteBillingKeyError = Union[BillingKeyAlreadyDeletedError, BillingKeyNotFoundError, BillingKeyNotIssuedError, ChannelSpecificError, ForbiddenError, InvalidRequestError, PaymentScheduleAlreadyExistsError, PgProviderError, UnauthorizedError, dict]


def _serialize_delete_billing_key_error(obj: DeleteBillingKeyError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BillingKeyAlreadyDeletedError):
        return _serialize_billing_key_already_deleted_error(obj)
    if isinstance(obj, BillingKeyNotFoundError):
        return _serialize_billing_key_not_found_error(obj)
    if isinstance(obj, BillingKeyNotIssuedError):
        return _serialize_billing_key_not_issued_error(obj)
    if isinstance(obj, ChannelSpecificError):
        return _serialize_channel_specific_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PaymentScheduleAlreadyExistsError):
        return _serialize_payment_schedule_already_exists_error(obj)
    if isinstance(obj, PgProviderError):
        return _serialize_pg_provider_error(obj)
    if isinstance(obj, UnauthorizedError):
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
