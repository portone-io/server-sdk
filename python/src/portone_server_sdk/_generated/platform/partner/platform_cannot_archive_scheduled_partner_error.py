from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotArchiveScheduledPartnerError:
    """예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_cannot_archive_scheduled_partner_error(obj: PlatformCannotArchiveScheduledPartnerError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_archive_scheduled_partner_error(obj: Any) -> PlatformCannotArchiveScheduledPartnerError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
        raise ValueError("Expected 'PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformCannotArchiveScheduledPartnerError(message)
