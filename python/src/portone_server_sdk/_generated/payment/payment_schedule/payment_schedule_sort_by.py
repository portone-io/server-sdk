from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentScheduleSortBy = Union[Literal["CREATED_AT", "TIME_TO_PAY", "COMPLETED_AT"], str]
"""결제 예약 건 정렬 기준
"""


def _serialize_payment_schedule_sort_by(obj: PaymentScheduleSortBy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_schedule_sort_by(obj: Any) -> PaymentScheduleSortBy:
    return obj
