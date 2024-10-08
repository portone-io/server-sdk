from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CloseVirtualAccountResponse:
    """가상계좌 말소 성공 응답
    """
    closed_at: str
    """가상계좌 말소 시점
    (RFC 3339 date-time)
    """


def _serialize_close_virtual_account_response(obj: CloseVirtualAccountResponse) -> Any:
    entity = {}
    entity["closedAt"] = obj.closed_at
    return entity


def _deserialize_close_virtual_account_response(obj: Any) -> CloseVirtualAccountResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "closedAt" not in obj:
        raise KeyError(f"'closedAt' is not in {obj}")
    closed_at = obj["closedAt"]
    if not isinstance(closed_at, str):
        raise ValueError(f"{repr(closed_at)} is not str")
    return CloseVirtualAccountResponse(closed_at)
