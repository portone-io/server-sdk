from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformInsufficientDataToChangePartnerTypeError:
    """파트너 타입 수정에 필요한 데이터가 부족한 경우
    """
    type: Literal["PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_insufficient_data_to_change_partner_type_error(obj: PlatformInsufficientDataToChangePartnerTypeError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_insufficient_data_to_change_partner_type_error(obj: Any) -> PlatformInsufficientDataToChangePartnerTypeError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformInsufficientDataToChangePartnerTypeError(type, message)
