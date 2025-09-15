from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.payment_event_with_cursor import PaymentEventWithCursor, _deserialize_payment_event_with_cursor, _serialize_payment_event_with_cursor

@dataclass
class GetAllPaymentEventsByCursorResponse:
    """결제 이벤트 커서 기반 대용량 다건 조회 성공 응답 정보
    """
    items: list[PaymentEventWithCursor]
    """조회된 결제 이벤트 및 커서 정보 리스트
    """


def _serialize_get_all_payment_events_by_cursor_response(obj: GetAllPaymentEventsByCursorResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["items"] = list(map(_serialize_payment_event_with_cursor, obj.items))
    return entity


def _deserialize_get_all_payment_events_by_cursor_response(obj: Any) -> GetAllPaymentEventsByCursorResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_payment_event_with_cursor(item)
        items[i] = item
    return GetAllPaymentEventsByCursorResponse(items)
