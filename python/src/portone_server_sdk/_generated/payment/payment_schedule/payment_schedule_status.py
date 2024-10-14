from __future__ import annotations
from typing import Any, Literal, Optional

PaymentScheduleStatus = Literal["SCHEDULED", "STARTED", "SUCCEEDED", "FAILED", "REVOKED", "PENDING"]
"""결제 예약 건 상태
"""


def _serialize_payment_schedule_status(obj: PaymentScheduleStatus) -> Any:
    return obj


def _deserialize_payment_schedule_status(obj: Any) -> PaymentScheduleStatus:
    if obj not in ["SCHEDULED", "STARTED", "SUCCEEDED", "FAILED", "REVOKED", "PENDING"]:
        raise ValueError(f"{repr(obj)} is not PaymentScheduleStatus")
    return obj
