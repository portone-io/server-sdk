from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.cancelled_payment_cash_receipt import CancelledPaymentCashReceipt, _deserialize_cancelled_payment_cash_receipt, _serialize_cancelled_payment_cash_receipt
from portone_server_sdk._generated.payment.issued_payment_cash_receipt import IssuedPaymentCashReceipt, _deserialize_issued_payment_cash_receipt, _serialize_issued_payment_cash_receipt

PaymentCashReceipt = Union[CancelledPaymentCashReceipt, IssuedPaymentCashReceipt]
"""결제 건 내 현금영수증 정보
"""


def _serialize_payment_cash_receipt(obj: PaymentCashReceipt) -> Any:
    if obj.status == "CANCELLED":
        return _serialize_cancelled_payment_cash_receipt(obj)
    if obj.status == "ISSUED":
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
