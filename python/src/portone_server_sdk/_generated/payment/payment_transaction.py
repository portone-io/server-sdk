from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.cancelled_payment_transaction import CancelledPaymentTransaction, _deserialize_cancelled_payment_transaction, _serialize_cancelled_payment_transaction
from ..payment.failed_payment_transaction import FailedPaymentTransaction, _deserialize_failed_payment_transaction, _serialize_failed_payment_transaction
from ..payment.paid_payment_transaction import PaidPaymentTransaction, _deserialize_paid_payment_transaction, _serialize_paid_payment_transaction
from ..payment.partial_cancelled_payment_transaction import PartialCancelledPaymentTransaction, _deserialize_partial_cancelled_payment_transaction, _serialize_partial_cancelled_payment_transaction
from ..payment.pay_pending_payment_transaction import PayPendingPaymentTransaction, _deserialize_pay_pending_payment_transaction, _serialize_pay_pending_payment_transaction
from ..payment.ready_payment_transaction import ReadyPaymentTransaction, _deserialize_ready_payment_transaction, _serialize_ready_payment_transaction
from ..payment.virtual_account_issued_payment_transaction import VirtualAccountIssuedPaymentTransaction, _deserialize_virtual_account_issued_payment_transaction, _serialize_virtual_account_issued_payment_transaction

PaymentTransaction = Union[CancelledPaymentTransaction, FailedPaymentTransaction, PaidPaymentTransaction, PartialCancelledPaymentTransaction, PayPendingPaymentTransaction, ReadyPaymentTransaction, VirtualAccountIssuedPaymentTransaction, dict]
"""결제 시도
"""


def _serialize_payment_transaction(obj: PaymentTransaction) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CancelledPaymentTransaction):
        return _serialize_cancelled_payment_transaction(obj)
    if isinstance(obj, FailedPaymentTransaction):
        return _serialize_failed_payment_transaction(obj)
    if isinstance(obj, PaidPaymentTransaction):
        return _serialize_paid_payment_transaction(obj)
    if isinstance(obj, PartialCancelledPaymentTransaction):
        return _serialize_partial_cancelled_payment_transaction(obj)
    if isinstance(obj, PayPendingPaymentTransaction):
        return _serialize_pay_pending_payment_transaction(obj)
    if isinstance(obj, ReadyPaymentTransaction):
        return _serialize_ready_payment_transaction(obj)
    if isinstance(obj, VirtualAccountIssuedPaymentTransaction):
        return _serialize_virtual_account_issued_payment_transaction(obj)


def _deserialize_payment_transaction(obj: Any) -> PaymentTransaction:
    try:
        return _deserialize_cancelled_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_failed_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_paid_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_partial_cancelled_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_pay_pending_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_ready_payment_transaction(obj)
    except Exception:
        pass
    try:
        return _deserialize_virtual_account_issued_payment_transaction(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentTransaction")
