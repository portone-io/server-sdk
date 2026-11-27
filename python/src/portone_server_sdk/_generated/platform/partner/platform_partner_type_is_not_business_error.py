from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerTypeIsNotBusinessError:
    """파트너 유형이 사업자가 아닌 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_partner_type_is_not_business_error(obj: PlatformPartnerTypeIsNotBusinessError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_partner_type_is_not_business_error(obj: Any) -> PlatformPartnerTypeIsNotBusinessError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS":
        raise ValueError("Expected 'PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformPartnerTypeIsNotBusinessError(message)
