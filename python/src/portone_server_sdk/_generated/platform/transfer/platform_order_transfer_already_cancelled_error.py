from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformOrderTransferAlreadyCancelledError:
    type: Literal["PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_order_transfer_already_cancelled_error(obj: PlatformOrderTransferAlreadyCancelledError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_order_transfer_already_cancelled_error(obj: Any) -> PlatformOrderTransferAlreadyCancelledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformOrderTransferAlreadyCancelledError(type, message)
