from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedPartnersCannotBeScheduledError:
    """보관된 파트너들을 예약 업데이트하려고 하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_archived_partners_cannot_be_scheduled_error(obj: PlatformArchivedPartnersCannotBeScheduledError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_partners_cannot_be_scheduled_error(obj: Any) -> PlatformArchivedPartnersCannotBeScheduledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformArchivedPartnersCannotBeScheduledError(message)
