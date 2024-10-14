from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCurrencyNotSupportedError:
    """지원 되지 않는 통화를 선택한 경우
    """
    type: Literal["PLATFORM_CURRENCY_NOT_SUPPORTED"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_currency_not_supported_error(obj: PlatformCurrencyNotSupportedError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CURRENCY_NOT_SUPPORTED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_currency_not_supported_error(obj: Any) -> PlatformCurrencyNotSupportedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CURRENCY_NOT_SUPPORTED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CURRENCY_NOT_SUPPORTED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCurrencyNotSupportedError(type, message)
