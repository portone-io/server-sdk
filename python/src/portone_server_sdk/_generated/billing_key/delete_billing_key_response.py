from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DeleteBillingKeyResponse:
    """빌링키 삭제 성공 응답
    """
    deleted_at: str
    """빌링키 삭제 완료 시점
    (RFC 3339 date-time)
    """


def _serialize_delete_billing_key_response(obj: DeleteBillingKeyResponse) -> Any:
    entity = {}
    entity["deletedAt"] = obj.deleted_at
    return entity


def _deserialize_delete_billing_key_response(obj: Any) -> DeleteBillingKeyResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "deletedAt" not in obj:
        raise KeyError(f"'deletedAt' is not in {obj}")
    deleted_at = obj["deletedAt"]
    if not isinstance(deleted_at, str):
        raise ValueError(f"{repr(deleted_at)} is not str")
    return DeleteBillingKeyResponse(deleted_at)
