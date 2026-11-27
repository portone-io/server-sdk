from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedPartnerError:
    """보관된 파트너를 업데이트하려고 하는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_archived_partner_error(obj: PlatformArchivedPartnerError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_PARTNER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_partner_error(obj: Any) -> PlatformArchivedPartnerError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_PARTNER":
        raise ValueError("Expected 'PLATFORM_ARCHIVED_PARTNER' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformArchivedPartnerError(message)
