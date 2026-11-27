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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS":
        raise ValueError("Expected 'PLATFORM_NO_SELECTED_PARTNER_SETTLEMENTS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformNoSelectedPartnerSettlementsError(message)
