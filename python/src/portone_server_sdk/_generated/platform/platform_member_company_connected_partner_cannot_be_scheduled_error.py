from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformMemberCompanyConnectedPartnerCannotBeScheduledError:
    """연동 사업자로 연동된 파트너를 예약 수정하려고 시도한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_member_company_connected_partner_cannot_be_scheduled_error(obj: PlatformMemberCompanyConnectedPartnerCannotBeScheduledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_CANNOT_BE_SCHEDULED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_member_company_connected_partner_cannot_be_scheduled_error(obj: Any) -> PlatformMemberCompanyConnectedPartnerCannotBeScheduledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_CANNOT_BE_SCHEDULED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_CANNOT_BE_SCHEDULED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformMemberCompanyConnectedPartnerCannotBeScheduledError(message)
