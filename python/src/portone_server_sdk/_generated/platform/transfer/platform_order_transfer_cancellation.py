from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformOrderTransferCancellation:
    """주문 취소 정보
    """
    id: str
    """주문 취소 아이디
    """
    cancelled_at: str
    """취소 일시
    (RFC 3339 date-time)
    """


def _serialize_platform_order_transfer_cancellation(obj: PlatformOrderTransferCancellation) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["cancelledAt"] = obj.cancelled_at
    return entity


def _deserialize_platform_order_transfer_cancellation(obj: Any) -> PlatformOrderTransferCancellation:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "id" not in obj:
        raise KeyError("Missing required field 'id'")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError("Expected str for id")
    if "cancelledAt" not in obj:
        raise KeyError("Missing required field 'cancelledAt'")
    cancelled_at = obj["cancelledAt"]
    if not isinstance(cancelled_at, str):
        raise ValueError("Expected str for cancelled_at")
    return PlatformOrderTransferCancellation(id, cancelled_at)
