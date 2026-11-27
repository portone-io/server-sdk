from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotSpecifyTransferError:
    """정산 건 식별에 실패한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_cannot_specify_transfer_error(obj: PlatformCannotSpecifyTransferError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_SPECIFY_TRANSFER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_specify_transfer_error(obj: Any) -> PlatformCannotSpecifyTransferError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_SPECIFY_TRANSFER":
        raise ValueError("Expected 'PLATFORM_CANNOT_SPECIFY_TRANSFER' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformCannotSpecifyTransferError(message)
