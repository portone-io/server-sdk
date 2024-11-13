from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentCashReceiptStatus = Union[Literal["ISSUED", "CANCELLED"], str]
"""결제건 내 현금영수증 상태
"""


def _serialize_payment_cash_receipt_status(obj: PaymentCashReceiptStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_cash_receipt_status(obj: Any) -> PaymentCashReceiptStatus:
    return obj
