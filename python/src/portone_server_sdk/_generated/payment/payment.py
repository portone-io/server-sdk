from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.cancelled_payment import CancelledPayment, _deserialize_cancelled_payment, _serialize_cancelled_payment
from portone_server_sdk._generated.payment.failed_payment import FailedPayment, _deserialize_failed_payment, _serialize_failed_payment
from portone_server_sdk._generated.payment.paid_payment import PaidPayment, _deserialize_paid_payment, _serialize_paid_payment
from portone_server_sdk._generated.payment.partial_cancelled_payment import PartialCancelledPayment, _deserialize_partial_cancelled_payment, _serialize_partial_cancelled_payment
from portone_server_sdk._generated.payment.pay_pending_payment import PayPendingPayment, _deserialize_pay_pending_payment, _serialize_pay_pending_payment
from portone_server_sdk._generated.payment.ready_payment import ReadyPayment, _deserialize_ready_payment, _serialize_ready_payment
from portone_server_sdk._generated.payment.virtual_account_issued_payment import VirtualAccountIssuedPayment, _deserialize_virtual_account_issued_payment, _serialize_virtual_account_issued_payment

Payment = Union[CancelledPayment, FailedPayment, PaidPayment, PartialCancelledPayment, PayPendingPayment, ReadyPayment, VirtualAccountIssuedPayment]
"""결제 건
"""


def _serialize_payment(obj: Payment) -> Any:
    if obj.status == "CANCELLED":
        return _serialize_cancelled_payment(obj)
    if obj.status == "FAILED":
        return _serialize_failed_payment(obj)
    if obj.status == "PAID":
        return _serialize_paid_payment(obj)
    if obj.status == "PARTIAL_CANCELLED":
        return _serialize_partial_cancelled_payment(obj)
    if obj.status == "PAY_PENDING":
        return _serialize_pay_pending_payment(obj)
    if obj.status == "READY":
        return _serialize_ready_payment(obj)
    if obj.status == "VIRTUAL_ACCOUNT_ISSUED":
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
