from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotArchiveScheduledPartnerError:
    """예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
    """
    type: Literal["PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_cannot_archive_scheduled_partner_error(obj: PlatformCannotArchiveScheduledPartnerError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_archive_scheduled_partner_error(obj: Any) -> PlatformCannotArchiveScheduledPartnerError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCannotArchiveScheduledPartnerError(type, message)
