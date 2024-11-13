from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreatePlatformOrderCancelTransferBodyExternalCancellationDetail:
    """외부 결제 상세 정보
    """
    cancelled_at: Optional[str] = field(default=None)
    """취소 일시
    (RFC 3339 date-time)
    """


def _serialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(obj: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.cancelled_at is not None:
        entity["cancelledAt"] = obj.cancelled_at
    return entity


def _deserialize_create_platform_order_cancel_transfer_body_external_cancellation_detail(obj: Any) -> CreatePlatformOrderCancelTransferBodyExternalCancellationDetail:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "cancelledAt" in obj:
        cancelled_at = obj["cancelledAt"]
        if not isinstance(cancelled_at, str):
            raise ValueError(f"{repr(cancelled_at)} is not str")
    else:
        cancelled_at = None
    return CreatePlatformOrderCancelTransferBodyExternalCancellationDetail(cancelled_at)
