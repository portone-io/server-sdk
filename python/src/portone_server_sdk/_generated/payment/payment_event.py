from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.cancelled_payment_event import CancelledPaymentEvent, _deserialize_cancelled_payment_event, _serialize_cancelled_payment_event
from ..payment.paid_payment_event import PaidPaymentEvent, _deserialize_paid_payment_event, _serialize_paid_payment_event
from ..payment.partial_cancelled_payment_event import PartialCancelledPaymentEvent, _deserialize_partial_cancelled_payment_event, _serialize_partial_cancelled_payment_event

PaymentEvent = Union[CancelledPaymentEvent, PaidPaymentEvent, PartialCancelledPaymentEvent, dict]
"""결제 이벤트
"""


def _serialize_payment_event(obj: PaymentEvent) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CancelledPaymentEvent):
        return _serialize_cancelled_payment_event(obj)
    if isinstance(obj, PaidPaymentEvent):
        return _serialize_paid_payment_event(obj)
    if isinstance(obj, PartialCancelledPaymentEvent):
        return _serialize_partial_cancelled_payment_event(obj)


def _deserialize_payment_event(obj: Any) -> PaymentEvent:
    try:
        return _deserialize_cancelled_payment_event(obj)
    except Exception:
        pass
    try:
        return _deserialize_paid_payment_event(obj)
    except Exception:
        pass
    try:
        return _deserialize_partial_cancelled_payment_event(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentEvent")
