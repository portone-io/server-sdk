from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class StopPaymentCancellationResponse:
    """결제 취소 요청 취소 성공 응답
    """
    stopped_at: str
    """결제 취소 요청 취소 완료 시각
    (RFC 3339 date-time)
    """


def _serialize_stop_payment_cancellation_response(obj: StopPaymentCancellationResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["stoppedAt"] = obj.stopped_at
    return entity


def _deserialize_stop_payment_cancellation_response(obj: Any) -> StopPaymentCancellationResponse:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "stoppedAt" not in obj:
        raise KeyError("Missing required field 'stoppedAt'")
    stopped_at = obj["stoppedAt"]
    if not isinstance(stopped_at, str):
        raise ValueError("Expected str for stopped_at")
    return StopPaymentCancellationResponse(stopped_at)
