from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class ConfirmEscrowResponse:
    """에스크로 구매 확정 성공 응답
    """
    completed_at: str
    """에스크로 구매 확정 시점
    (RFC 3339 date-time)
    """


def _serialize_confirm_escrow_response(obj: ConfirmEscrowResponse) -> Any:
    entity = {}
    entity["completedAt"] = obj.completed_at
    return entity


def _deserialize_confirm_escrow_response(obj: Any) -> ConfirmEscrowResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "completedAt" not in obj:
        raise KeyError(f"'completedAt' is not in {obj}")
    completed_at = obj["completedAt"]
    if not isinstance(completed_at, str):
        raise ValueError(f"{repr(completed_at)} is not str")
    return ConfirmEscrowResponse(completed_at)
