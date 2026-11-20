from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ClosePaymentSessionResponse:
    """결제 세션 종료 성공 응답
    """
    closed_at: str
    """결제 세션 종료 시각
    (RFC 3339 date-time)
    """


def _serialize_close_payment_session_response(obj: ClosePaymentSessionResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["closedAt"] = obj.closed_at
    return entity


def _deserialize_close_payment_session_response(obj: Any) -> ClosePaymentSessionResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "closedAt" not in obj:
        raise KeyError(f"'closedAt' is not in {obj}")
    closed_at = obj["closedAt"]
    if not isinstance(closed_at, str):
        raise ValueError(f"{repr(closed_at)} is not str")
    return ClosePaymentSessionResponse(closed_at)
