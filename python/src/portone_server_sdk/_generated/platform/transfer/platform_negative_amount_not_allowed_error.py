from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNegativeAmountNotAllowedError:
    """정산 건별 옵션이 켜진 플랫폼에서 음수 금액 수기 정산 생성을 시도한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_negative_amount_not_allowed_error(obj: PlatformNegativeAmountNotAllowedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_NEGATIVE_AMOUNT_NOT_ALLOWED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_negative_amount_not_allowed_error(obj: Any) -> PlatformNegativeAmountNotAllowedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_NEGATIVE_AMOUNT_NOT_ALLOWED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_NEGATIVE_AMOUNT_NOT_ALLOWED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformNegativeAmountNotAllowedError(message)
