from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNotSupportedBankError:
    """지원하지 않는 은행인 경우
    """
    type: Literal["PLATFORM_NOT_SUPPORTED_BANK"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_not_supported_bank_error(obj: PlatformNotSupportedBankError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_NOT_SUPPORTED_BANK"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_not_supported_bank_error(obj: Any) -> PlatformNotSupportedBankError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_NOT_SUPPORTED_BANK":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_NOT_SUPPORTED_BANK'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformNotSupportedBankError(type, message)
