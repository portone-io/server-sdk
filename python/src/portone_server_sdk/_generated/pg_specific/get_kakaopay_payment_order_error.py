from __future__ import annotations
from typing import Any, Optional, Union
from ..common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ..common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

GetKakaopayPaymentOrderError = Union[InvalidRequestError, UnauthorizedError, dict]


def _serialize_get_kakaopay_payment_order_error(obj: GetKakaopayPaymentOrderError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, UnauthorizedError):
        return _serialize_unauthorized_error(obj)


def _deserialize_get_kakaopay_payment_order_error(obj: Any) -> GetKakaopayPaymentOrderError:
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not GetKakaopayPaymentOrderError")
