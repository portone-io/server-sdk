from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.payment.payment_not_found_error import PaymentNotFoundError, _deserialize_payment_not_found_error, _serialize_payment_not_found_error
from portone_server_sdk._generated.payment.payment_not_paid_error import PaymentNotPaidError, _deserialize_payment_not_paid_error, _serialize_payment_not_paid_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

RegisterStoreReceiptError = Union[ForbiddenError, InvalidRequestError, PaymentNotFoundError, PaymentNotPaidError, PgProviderError, UnauthorizedError]


def _serialize_register_store_receipt_error(obj: RegisterStoreReceiptError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PAYMENT_NOT_FOUND":
        return _serialize_payment_not_found_error(obj)
    if obj.type == "PAYMENT_NOT_PAID":
        return _serialize_payment_not_paid_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_register_store_receipt_error(obj: Any) -> RegisterStoreReceiptError:
    try:
        return _deserialize_forbidden_error(obj)
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
        return _deserialize_payment_not_paid_error(obj)
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
    raise ValueError(f"{repr(obj)} is not RegisterStoreReceiptError")
