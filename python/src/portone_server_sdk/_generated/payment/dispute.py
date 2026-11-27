from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..payment.dispute_status import DisputeStatus, _deserialize_dispute_status, _serialize_dispute_status

@dataclass
class Dispute:
    """분쟁 내역
    """
    status: DisputeStatus
    """분쟁 상태
    """
    reason: str
    """분쟁 사유
    """
    created_at: str
    """분쟁 발생 시각
    (RFC 3339 date-time)
    """
    pg_dispute_id: Optional[str] = field(default=None)
    """PG사 분쟁 아이디
    """
    resolved_at: Optional[str] = field(default=None)
    """분쟁 해소 시각
    (RFC 3339 date-time)
    """


def _serialize_dispute(obj: Dispute) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["status"] = _serialize_dispute_status(obj.status)
    entity["reason"] = obj.reason
    entity["createdAt"] = obj.created_at
    if obj.pg_dispute_id is not None:
        entity["pgDisputeId"] = obj.pg_dispute_id
    if obj.resolved_at is not None:
        entity["resolvedAt"] = obj.resolved_at
    return entity


def _deserialize_dispute(obj: Any) -> Dispute:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "status" not in obj:
        raise KeyError("Missing required field 'status'")
    status = obj["status"]
    status = _deserialize_dispute_status(status)
    if "reason" not in obj:
        raise KeyError("Missing required field 'reason'")
    reason = obj["reason"]
    if not isinstance(reason, str):
        raise ValueError("Expected str for reason")
    if "createdAt" not in obj:
        raise KeyError("Missing required field 'createdAt'")
    created_at = obj["createdAt"]
    if not isinstance(created_at, str):
        raise ValueError("Expected str for created_at")
    if "pgDisputeId" in obj:
        pg_dispute_id = obj["pgDisputeId"]
        if not isinstance(pg_dispute_id, str):
            raise ValueError("Expected str for pg_dispute_id")
    else:
        pg_dispute_id = None
    if "resolvedAt" in obj:
        resolved_at = obj["resolvedAt"]
        if not isinstance(resolved_at, str):
            raise ValueError("Expected str for resolved_at")
    else:
        resolved_at = None
    return Dispute(status, reason, created_at, pg_dispute_id, resolved_at)
