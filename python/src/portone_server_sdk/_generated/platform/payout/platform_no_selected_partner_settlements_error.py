from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNoSelectedPartnerSettlementsError:
    """선택된 정산건이 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_no_selected_partner_settlements_error(obj: PlatformNoSelectedPartnerSettlementsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_no_selected_partner_settlements_error(obj: Any) -> PlatformNoSelectedPartnerSettlementsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformNoSelectedPartnerSettlementsError(message)
