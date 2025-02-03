from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.before_registered_payment_escrow import BeforeRegisteredPaymentEscrow, _deserialize_before_registered_payment_escrow, _serialize_before_registered_payment_escrow
from ..payment.cancelled_payment_escrow import CancelledPaymentEscrow, _deserialize_cancelled_payment_escrow, _serialize_cancelled_payment_escrow
from ..payment.confirmed_payment_escrow import ConfirmedPaymentEscrow, _deserialize_confirmed_payment_escrow, _serialize_confirmed_payment_escrow
from ..payment.delivered_payment_escrow import DeliveredPaymentEscrow, _deserialize_delivered_payment_escrow, _serialize_delivered_payment_escrow
from ..payment.registered_payment_escrow import RegisteredPaymentEscrow, _deserialize_registered_payment_escrow, _serialize_registered_payment_escrow
from ..payment.reject_confirmed_payment_escrow import RejectConfirmedPaymentEscrow, _deserialize_reject_confirmed_payment_escrow, _serialize_reject_confirmed_payment_escrow
from ..payment.rejected_payment_escrow import RejectedPaymentEscrow, _deserialize_rejected_payment_escrow, _serialize_rejected_payment_escrow

PaymentEscrow = Union[BeforeRegisteredPaymentEscrow, CancelledPaymentEscrow, ConfirmedPaymentEscrow, DeliveredPaymentEscrow, RegisteredPaymentEscrow, RejectedPaymentEscrow, RejectConfirmedPaymentEscrow, dict]
"""에스크로 정보

V1 결제 건의 경우 타입이 REGISTERED 로 고정됩니다.
"""


def _serialize_payment_escrow(obj: PaymentEscrow) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BeforeRegisteredPaymentEscrow):
        return _serialize_before_registered_payment_escrow(obj)
    if isinstance(obj, CancelledPaymentEscrow):
        return _serialize_cancelled_payment_escrow(obj)
    if isinstance(obj, ConfirmedPaymentEscrow):
        return _serialize_confirmed_payment_escrow(obj)
    if isinstance(obj, DeliveredPaymentEscrow):
        return _serialize_delivered_payment_escrow(obj)
    if isinstance(obj, RegisteredPaymentEscrow):
        return _serialize_registered_payment_escrow(obj)
    if isinstance(obj, RejectedPaymentEscrow):
        return _serialize_rejected_payment_escrow(obj)
    if isinstance(obj, RejectConfirmedPaymentEscrow):
        return _serialize_reject_confirmed_payment_escrow(obj)


def _deserialize_payment_escrow(obj: Any) -> PaymentEscrow:
    try:
        return _deserialize_before_registered_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_cancelled_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_confirmed_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_delivered_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_registered_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_rejected_payment_escrow(obj)
    except Exception:
        pass
    try:
        return _deserialize_reject_confirmed_payment_escrow(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentEscrow")
