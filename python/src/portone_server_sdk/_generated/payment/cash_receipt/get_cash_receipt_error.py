from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.cash_receipt.cash_receipt_not_found_error import CashReceiptNotFoundError, _deserialize_cash_receipt_not_found_error, _serialize_cash_receipt_not_found_error
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetCashReceiptError = Union[CashReceiptNotFoundError, ForbiddenError, InvalidRequestError, UnauthorizedError, dict]


def _serialize_get_cash_receipt_error(obj: GetCashReceiptError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CashReceiptNotFoundError):
        return _serialize_cash_receipt_not_found_error(obj)
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_cash_receipt_error(obj: Any) -> GetCashReceiptError:
    try:
        return _deserialize_cash_receipt_not_found_error(obj)
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
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetCashReceiptError")
