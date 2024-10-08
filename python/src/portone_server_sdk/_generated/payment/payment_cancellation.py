from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.failed_payment_cancellation import FailedPaymentCancellation, _deserialize_failed_payment_cancellation, _serialize_failed_payment_cancellation
from portone_server_sdk._generated.payment.requested_payment_cancellation import RequestedPaymentCancellation, _deserialize_requested_payment_cancellation, _serialize_requested_payment_cancellation
from portone_server_sdk._generated.payment.succeeded_payment_cancellation import SucceededPaymentCancellation, _deserialize_succeeded_payment_cancellation, _serialize_succeeded_payment_cancellation

PaymentCancellation = Union[FailedPaymentCancellation, RequestedPaymentCancellation, SucceededPaymentCancellation]
"""결제 취소 내역
"""


def _serialize_payment_cancellation(obj: PaymentCancellation) -> Any:
    if obj.status == "FAILED":
        return _serialize_failed_payment_cancellation(obj)
    if obj.status == "REQUESTED":
        return _serialize_requested_payment_cancellation(obj)
    if obj.status == "SUCCEEDED":
        return _serialize_succeeded_payment_cancellation(obj)


def _deserialize_payment_cancellation(obj: Any) -> PaymentCancellation:
    try:
        return _deserialize_failed_payment_cancellation(obj)
    except Exception:
        pass
    try:
        return _deserialize_requested_payment_cancellation(obj)
    except Exception:
        pass
    try:
        return _deserialize_succeeded_payment_cancellation(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentCancellation")
