from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformProductIdNotFoundError:
    id: str
    message: Optional[str] = field(default=None)


def _serialize_platform_product_id_not_found_error(obj: PlatformProductIdNotFoundError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_PRODUCT_ID_NOT_FOUND"
    entity["id"] = obj.id
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_product_id_not_found_error(obj: Any) -> PlatformProductIdNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_PRODUCT_ID_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_PRODUCT_ID_NOT_FOUND'")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformProductIdNotFoundError(id, message)
