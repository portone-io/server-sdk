from __future__ import annotations
from typing import Any, Literal, Optional

PaymentStatus = Literal["READY", "PENDING", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED"]
"""결제 건 상태
"""


def _serialize_payment_status(obj: PaymentStatus) -> Any:
    return obj


def _deserialize_payment_status(obj: Any) -> PaymentStatus:
    if obj not in ["READY", "PENDING", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED"]:
        raise ValueError(f"{repr(obj)} is not PaymentStatus")
    return obj
