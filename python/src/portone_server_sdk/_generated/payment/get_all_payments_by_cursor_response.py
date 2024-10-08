from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.payment.payment_with_cursor import PaymentWithCursor, _deserialize_payment_with_cursor, _serialize_payment_with_cursor

@dataclass
class GetAllPaymentsByCursorResponse:
    """결제 건 커서 기반 대용량 다건 조회 성공 응답 정보
    """
    items: list[PaymentWithCursor]
    """조회된 결제 건 및 커서 정보 리스트
    """


def _serialize_get_all_payments_by_cursor_response(obj: GetAllPaymentsByCursorResponse) -> Any:
    entity = {}
    entity["items"] = list(map(_serialize_payment_with_cursor, obj.items))
    return entity


def _deserialize_get_all_payments_by_cursor_response(obj: Any) -> GetAllPaymentsByCursorResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_payment_with_cursor(item)
        items[i] = item
    return GetAllPaymentsByCursorResponse(items)
