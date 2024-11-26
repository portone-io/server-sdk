from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class RevokePaymentSchedulesResponse:
    """결제 예약 건 취소 성공 응답
    """
    revoked_schedule_ids: list[str]
    """취소 완료된 결제 예약 건 아이디 목록
    """
    revoked_at: Optional[str] = field(default=None)
    """결제 예약 건 취소 완료 시점
    (RFC 3339 date-time)
    """


def _serialize_revoke_payment_schedules_response(obj: RevokePaymentSchedulesResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["revokedScheduleIds"] = obj.revoked_schedule_ids
    if obj.revoked_at is not None:
        entity["revokedAt"] = obj.revoked_at
    return entity


def _deserialize_revoke_payment_schedules_response(obj: Any) -> RevokePaymentSchedulesResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "revokedScheduleIds" not in obj:
        raise KeyError(f"'revokedScheduleIds' is not in {obj}")
    revoked_schedule_ids = obj["revokedScheduleIds"]
    if not isinstance(revoked_schedule_ids, list):
        raise ValueError(f"{repr(revoked_schedule_ids)} is not list")
    for i, item in enumerate(revoked_schedule_ids):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "revokedAt" in obj:
        revoked_at = obj["revokedAt"]
        if not isinstance(revoked_at, str):
            raise ValueError(f"{repr(revoked_at)} is not str")
    else:
        revoked_at = None
    return RevokePaymentSchedulesResponse(revoked_schedule_ids, revoked_at)
