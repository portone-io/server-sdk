from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.update_platform_partner_body import UpdatePlatformPartnerBody, _deserialize_update_platform_partner_body, _serialize_update_platform_partner_body

@dataclass
class ReschedulePlatformPartnerBody:
    """파트너 예약 업데이트 재설정을 위한 입력 정보
    """
    update: UpdatePlatformPartnerBody
    """반영할 업데이트 내용
    """
    applied_at: str
    """업데이트 적용 시점
    (RFC 3339 date-time)
    """


def _serialize_reschedule_platform_partner_body(obj: ReschedulePlatformPartnerBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["update"] = _serialize_update_platform_partner_body(obj.update)
    entity["appliedAt"] = obj.applied_at
    return entity


def _deserialize_reschedule_platform_partner_body(obj: Any) -> ReschedulePlatformPartnerBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "update" not in obj:
        raise KeyError("Missing required field 'update'")
    update = obj["update"]
    update = _deserialize_update_platform_partner_body(update)
    if "appliedAt" not in obj:
        raise KeyError("Missing required field 'appliedAt'")
    applied_at = obj["appliedAt"]
    if not isinstance(applied_at, str):
        raise ValueError("Expected str for applied_at")
    return ReschedulePlatformPartnerBody(update, applied_at)
