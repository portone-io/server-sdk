from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentStatus = Union[Literal["READY", "PENDING", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED"], str]
"""결제 건 상태
"""


def _serialize_payment_status(obj: PaymentStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_status(obj: Any) -> PaymentStatus:
    return obj
