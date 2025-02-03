from __future__ import annotations
from typing import Any, Optional, Union
from ..payment.cancelled_payment_cash_receipt import CancelledPaymentCashReceipt, _deserialize_cancelled_payment_cash_receipt, _serialize_cancelled_payment_cash_receipt
from ..payment.issued_payment_cash_receipt import IssuedPaymentCashReceipt, _deserialize_issued_payment_cash_receipt, _serialize_issued_payment_cash_receipt

PaymentCashReceipt = Union[CancelledPaymentCashReceipt, IssuedPaymentCashReceipt, dict]
"""결제 건 내 현금영수증 정보
"""


def _serialize_payment_cash_receipt(obj: PaymentCashReceipt) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CancelledPaymentCashReceipt):
        return _serialize_cancelled_payment_cash_receipt(obj)
    if isinstance(obj, IssuedPaymentCashReceipt):
        return _serialize_issued_payment_cash_receipt(obj)


def _deserialize_payment_cash_receipt(obj: Any) -> PaymentCashReceipt:
    try:
        return _deserialize_cancelled_payment_cash_receipt(obj)
    except Exception:
        pass
    try:
        return _deserialize_issued_payment_cash_receipt(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PaymentCashReceipt")
