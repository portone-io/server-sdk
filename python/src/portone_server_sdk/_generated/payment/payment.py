from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.cancelled_payment import CancelledPayment, _deserialize_cancelled_payment, _serialize_cancelled_payment
from ..payment.failed_payment import FailedPayment, _deserialize_failed_payment, _serialize_failed_payment
from ..payment.paid_payment import PaidPayment, _deserialize_paid_payment, _serialize_paid_payment
from ..payment.partial_cancelled_payment import PartialCancelledPayment, _deserialize_partial_cancelled_payment, _serialize_partial_cancelled_payment
from ..payment.pay_pending_payment import PayPendingPayment, _deserialize_pay_pending_payment, _serialize_pay_pending_payment
from ..payment.ready_payment import ReadyPayment, _deserialize_ready_payment, _serialize_ready_payment
from ..payment.virtual_account_issued_payment import VirtualAccountIssuedPayment, _deserialize_virtual_account_issued_payment, _serialize_virtual_account_issued_payment

Payment = Union[CancelledPayment, FailedPayment, PaidPayment, PartialCancelledPayment, PayPendingPayment, ReadyPayment, VirtualAccountIssuedPayment, dict]
"""결제 건
"""


def _serialize_payment(obj: Payment) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CancelledPayment):
        return _serialize_cancelled_payment(obj)
    if isinstance(obj, FailedPayment):
        return _serialize_failed_payment(obj)
    if isinstance(obj, PaidPayment):
        return _serialize_paid_payment(obj)
    if isinstance(obj, PartialCancelledPayment):
        return _serialize_partial_cancelled_payment(obj)
    if isinstance(obj, PayPendingPayment):
        return _serialize_pay_pending_payment(obj)
    if isinstance(obj, ReadyPayment):
        return _serialize_ready_payment(obj)
    if isinstance(obj, VirtualAccountIssuedPayment):
        return _serialize_virtual_account_issued_payment(obj)


def _deserialize_payment(obj: Any) -> Payment:
    try:
        return _deserialize_cancelled_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_failed_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_paid_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_partial_cancelled_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_pay_pending_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_ready_payment(obj)
    except Exception:
        pass
    try:
        return _deserialize_virtual_account_issued_payment(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not Payment")
