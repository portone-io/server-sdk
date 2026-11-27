from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPartnerTaxationTypeIsSimpleError:
    """파트너의 과세 유형이 간이 과세 세금계산서 미발행 유형인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_partner_taxation_type_is_simple_error(obj: PlatformPartnerTaxationTypeIsSimpleError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_partner_taxation_type_is_simple_error(obj: Any) -> PlatformPartnerTaxationTypeIsSimpleError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE":
        raise ValueError("Expected 'PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformPartnerTaxationTypeIsSimpleError(message)
