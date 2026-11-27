from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentScheduleSummary:
    """결제 예약 건
    """
    id: str
    """결제 예약 건 아이디
    """


def _serialize_payment_schedule_summary(obj: PaymentScheduleSummary) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    return entity


def _deserialize_payment_schedule_summary(obj: Any) -> PaymentScheduleSummary:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    return PaymentScheduleSummary(id)
