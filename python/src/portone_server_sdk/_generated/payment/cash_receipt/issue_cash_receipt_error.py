from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_already_issued_error import CashReceiptAlreadyIssuedError, _deserialize_cash_receipt_already_issued_error, _serialize_cash_receipt_already_issued_error
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError, _deserialize_channel_not_found_error, _serialize_channel_not_found_error
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError, _deserialize_pg_provider_error, _serialize_pg_provider_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

IssueCashReceiptError = Union[CashReceiptAlreadyIssuedError, ChannelNotFoundError, ForbiddenError, InvalidRequestError, PgProviderError, UnauthorizedError]


def _serialize_issue_cash_receipt_error(obj: IssueCashReceiptError) -> Any:
    if obj.type == "CASH_RECEIPT_ALREADY_ISSUED":
        return _serialize_cash_receipt_already_issued_error(obj)
    if obj.type == "CHANNEL_NOT_FOUND":
        return _serialize_channel_not_found_error(obj)
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PG_PROVIDER":
        return _serialize_pg_provider_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_issue_cash_receipt_error(obj: Any) -> IssueCashReceiptError:
    try:
        return _deserialize_cash_receipt_already_issued_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_channel_not_found_error(obj)
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
        return _deserialize_pg_provider_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not IssueCashReceiptError")
