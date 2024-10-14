from __future__ import annotations
from typing import Any, Literal, Optional

PaymentScheduleSortBy = Literal["CREATED_AT", "TIME_TO_PAY", "COMPLETED_AT"]
"""결제 예약 건 정렬 기준
"""


def _serialize_payment_schedule_sort_by(obj: PaymentScheduleSortBy) -> Any:
    return obj


def _deserialize_payment_schedule_sort_by(obj: Any) -> PaymentScheduleSortBy:
    if obj not in ["CREATED_AT", "TIME_TO_PAY", "COMPLETED_AT"]:
        raise ValueError(f"{repr(obj)} is not PaymentScheduleSortBy")
    return obj
