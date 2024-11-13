from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentScheduleStatus = Union[Literal["SCHEDULED", "STARTED", "SUCCEEDED", "FAILED", "REVOKED", "PENDING"], str]
"""결제 예약 건 상태
"""


def _serialize_payment_schedule_status(obj: PaymentScheduleStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_schedule_status(obj: Any) -> PaymentScheduleStatus:
    return obj
