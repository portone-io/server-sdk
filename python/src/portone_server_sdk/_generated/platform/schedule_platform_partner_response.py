from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class SchedulePlatformPartnerResponse:
    """파트너 업데이트 예약 성공 응답
    """
    scheduled_partner: PlatformPartner
    """예약된 파트너 정보
    """


def _serialize_schedule_platform_partner_response(obj: SchedulePlatformPartnerResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["scheduledPartner"] = _serialize_platform_partner(obj.scheduled_partner)
    return entity


def _deserialize_schedule_platform_partner_response(obj: Any) -> SchedulePlatformPartnerResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledPartner" not in obj:
        raise KeyError(f"'scheduledPartner' is not in {obj}")
    scheduled_partner = obj["scheduledPartner"]
    scheduled_partner = _deserialize_platform_partner(scheduled_partner)
    return SchedulePlatformPartnerResponse(scheduled_partner)
