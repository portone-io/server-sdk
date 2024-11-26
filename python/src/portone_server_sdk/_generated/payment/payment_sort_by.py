from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentSortBy = Union[Literal["REQUESTED_AT", "STATUS_CHANGED_AT"], str]
"""결제 건 정렬 기준
"""


def _serialize_payment_sort_by(obj: PaymentSortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_sort_by(obj: Any) -> PaymentSortBy:
    return obj
