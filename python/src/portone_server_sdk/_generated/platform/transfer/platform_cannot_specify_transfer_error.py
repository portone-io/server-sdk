from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCannotSpecifyTransferError:
    """정산 건 식별에 실패한 경우
    """
    type: Literal["PLATFORM_CANNOT_SPECIFY_TRANSFER"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_cannot_specify_transfer_error(obj: PlatformCannotSpecifyTransferError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANNOT_SPECIFY_TRANSFER"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cannot_specify_transfer_error(obj: Any) -> PlatformCannotSpecifyTransferError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANNOT_SPECIFY_TRANSFER":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANNOT_SPECIFY_TRANSFER'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCannotSpecifyTransferError(type, message)
