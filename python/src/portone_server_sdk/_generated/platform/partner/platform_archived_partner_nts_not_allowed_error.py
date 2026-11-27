from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedPartnerNtsNotAllowedError:
    """보관된 파트너는 국세청 연동/연동해제를 할 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_archived_partner_nts_not_allowed_error(obj: PlatformArchivedPartnerNtsNotAllowedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_partner_nts_not_allowed_error(obj: Any) -> PlatformArchivedPartnerNtsNotAllowedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED":
        raise ValueError("Expected 'PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformArchivedPartnerNtsNotAllowedError(message)
