from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformNotSupportedBankError:
    """지원하지 않는 은행인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_not_supported_bank_error(obj: PlatformNotSupportedBankError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_NOT_SUPPORTED_BANK"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_not_supported_bank_error(obj: Any) -> PlatformNotSupportedBankError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_NOT_SUPPORTED_BANK":
        raise ValueError("Expected 'PLATFORM_NOT_SUPPORTED_BANK' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformNotSupportedBankError(message)
