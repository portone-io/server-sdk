from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.platform_partner import PlatformPartner, _deserialize_platform_partner, _serialize_platform_partner

@dataclass
class ReschedulePlatformPartnerResponse:
    """파트너 예약 업데이트 재설정 성공 응답
    """
    scheduled_partner: PlatformPartner
    """예약된 파트너 정보
    """


def _serialize_reschedule_platform_partner_response(obj: ReschedulePlatformPartnerResponse) -> Any:
    entity = {}
    entity["scheduledPartner"] = _serialize_platform_partner(obj.scheduled_partner)
    return entity


def _deserialize_reschedule_platform_partner_response(obj: Any) -> ReschedulePlatformPartnerResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "scheduledPartner" not in obj:
        raise KeyError(f"'scheduledPartner' is not in {obj}")
    scheduled_partner = obj["scheduledPartner"]
    scheduled_partner = _deserialize_platform_partner(scheduled_partner)
    return ReschedulePlatformPartnerResponse(scheduled_partner)
