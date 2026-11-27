from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_event import PaymentEvent, _deserialize_payment_event, _serialize_payment_event

@dataclass
class PaymentEventWithCursor:
    """결제 이벤트 및 커서 정보
    """
    payment_event: PaymentEvent
    """결제 이벤트 정보
    """
    cursor: str
    """해당 결제 이벤트의 커서 정보
    """


def _serialize_payment_event_with_cursor(obj: PaymentEventWithCursor) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["paymentEvent"] = _serialize_payment_event(obj.payment_event)
    entity["cursor"] = obj.cursor
    return entity


def _deserialize_payment_event_with_cursor(obj: Any) -> PaymentEventWithCursor:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "paymentEvent" not in obj:
        raise KeyError("Missing required field 'paymentEvent'")
    payment_event = obj["paymentEvent"]
    payment_event = _deserialize_payment_event(payment_event)
    if "cursor" not in obj:
        raise KeyError("Missing required field 'cursor'")
    cursor = obj["cursor"]
    if not isinstance(cursor, str):
        raise ValueError("Expected str for cursor")
    return PaymentEventWithCursor(payment_event, cursor)
