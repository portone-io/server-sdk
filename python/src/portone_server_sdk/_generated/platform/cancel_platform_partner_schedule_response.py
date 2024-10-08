from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CancelPlatformPartnerScheduleResponse:
    """파트너 예약 업데이트 취소 성공 응답
    """
    pass


def _serialize_cancel_platform_partner_schedule_response(obj: CancelPlatformPartnerScheduleResponse) -> Any:
    entity = {}
    return entity


def _deserialize_cancel_platform_partner_schedule_response(obj: Any) -> CancelPlatformPartnerScheduleResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return CancelPlatformPartnerScheduleResponse()
