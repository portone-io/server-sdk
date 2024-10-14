from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformArchivedPartnerError:
    """보관된 파트너를 업데이트하려고 하는 경우
    """
    type: Literal["PLATFORM_ARCHIVED_PARTNER"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_archived_partner_error(obj: PlatformArchivedPartnerError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_ARCHIVED_PARTNER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_archived_partner_error(obj: Any) -> PlatformArchivedPartnerError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ARCHIVED_PARTNER":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ARCHIVED_PARTNER'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformArchivedPartnerError(type, message)
