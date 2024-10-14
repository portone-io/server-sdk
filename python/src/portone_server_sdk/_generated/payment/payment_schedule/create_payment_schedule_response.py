from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_summary import PaymentScheduleSummary, _deserialize_payment_schedule_summary, _serialize_payment_schedule_summary

@dataclass
class CreatePaymentScheduleResponse:
    """결제 예약 성공 응답
    """
    schedule: PaymentScheduleSummary
    """결제 예약 건
    """


def _serialize_create_payment_schedule_response(obj: CreatePaymentScheduleResponse) -> Any:
    entity = {}
    entity["schedule"] = _serialize_payment_schedule_summary(obj.schedule)
    return entity


def _deserialize_create_payment_schedule_response(obj: Any) -> CreatePaymentScheduleResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "schedule" not in obj:
        raise KeyError(f"'schedule' is not in {obj}")
    schedule = obj["schedule"]
    schedule = _deserialize_payment_schedule_summary(schedule)
    return CreatePaymentScheduleResponse(schedule)
