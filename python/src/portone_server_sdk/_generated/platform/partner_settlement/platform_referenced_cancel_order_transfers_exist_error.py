from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformReferencedCancelOrderTransfersExistError:
    """취소 정산건이 참조 중인 정산건이 포함된 경우
    """
    ids: list[str]
    message: Optional[str] = field(default=None)


def _serialize_platform_referenced_cancel_order_transfers_exist_error(obj: PlatformReferencedCancelOrderTransfersExistError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_REFERENCED_CANCEL_ORDER_TRANSFERS_EXIST"
    entity["ids"] = obj.ids
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_referenced_cancel_order_transfers_exist_error(obj: Any) -> PlatformReferencedCancelOrderTransfersExistError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_REFERENCED_CANCEL_ORDER_TRANSFERS_EXIST":
        raise ValueError("Expected 'PLATFORM_REFERENCED_CANCEL_ORDER_TRANSFERS_EXIST' for type")
    if "ids" not in obj:
        raise KeyError("Missing required field 'ids'")
    ids = obj["ids"]
    if not isinstance(ids, list):
        raise ValueError("Expected list for ids")
    for i, item in enumerate(ids):
        if not isinstance(item, str):
            raise ValueError("Expected str for item")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformReferencedCancelOrderTransfersExistError(ids, message)
