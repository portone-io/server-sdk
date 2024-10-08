from __future__ import annotations
from typing import Any, Literal, Optional

PaymentCashReceiptStatus = Literal["ISSUED", "CANCELLED"]
"""결제건 내 현금영수증 상태
"""


def _serialize_payment_cash_receipt_status(obj: PaymentCashReceiptStatus) -> Any:
    return obj


def _deserialize_payment_cash_receipt_status(obj: Any) -> PaymentCashReceiptStatus:
    if obj not in ["ISSUED", "CANCELLED"]:
        raise ValueError(f"{repr(obj)} is not PaymentCashReceiptStatus")
    return obj
