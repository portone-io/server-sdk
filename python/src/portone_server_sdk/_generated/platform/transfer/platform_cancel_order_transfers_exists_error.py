from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancelOrderTransfersExistsError:
    message: Optional[str] = field(default=None)


def _serialize_platform_cancel_order_transfers_exists_error(obj: PlatformCancelOrderTransfersExistsError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancel_order_transfers_exists_error(obj: Any) -> PlatformCancelOrderTransfersExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCancelOrderTransfersExistsError(message)
