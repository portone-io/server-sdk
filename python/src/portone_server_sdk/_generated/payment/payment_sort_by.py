from __future__ import annotations
from typing import Any, Literal, Optional

PaymentSortBy = Literal["REQUESTED_AT", "STATUS_CHANGED_AT"]
"""결제 건 정렬 기준
"""


def _serialize_payment_sort_by(obj: PaymentSortBy) -> Any:
    return obj


def _deserialize_payment_sort_by(obj: Any) -> PaymentSortBy:
    if obj not in ["REQUESTED_AT", "STATUS_CHANGED_AT"]:
        raise ValueError(f"{repr(obj)} is not PaymentSortBy")
    return obj
