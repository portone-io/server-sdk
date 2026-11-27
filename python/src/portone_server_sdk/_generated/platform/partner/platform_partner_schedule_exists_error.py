from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerScheduleExistsError:
    """파트너 수정 예약 건이 존재하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_partner_schedule_exists_error(obj: PlatformPartnerScheduleExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_PARTNER_SCHEDULE_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_partner_schedule_exists_error(obj: Any) -> PlatformPartnerScheduleExistsError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_PARTNER_SCHEDULE_EXISTS":
        raise ValueError("Expected 'PLATFORM_PARTNER_SCHEDULE_EXISTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformPartnerScheduleExistsError(message)
