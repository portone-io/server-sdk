from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellableProductQuantityExceededError:
    product_id: str
    cancellable_quantity: int
    """(int64)
    """
    message: Optional[str] = field(default=None)


def _serialize_platform_cancellable_product_quantity_exceeded_error(obj: PlatformCancellableProductQuantityExceededError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED"
    entity["productId"] = obj.product_id
    entity["cancellableQuantity"] = obj.cancellable_quantity
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellable_product_quantity_exceeded_error(obj: Any) -> PlatformCancellableProductQuantityExceededError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED":
        raise ValueError("Expected 'PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED' for type")
    if "productId" not in obj:
        raise KeyError("Missing required field 'productId'")
    product_id = obj["productId"]
    if not isinstance(product_id, str):
        raise ValueError("Expected str for product_id")
    if "cancellableQuantity" not in obj:
        raise KeyError("Missing required field 'cancellableQuantity'")
    cancellable_quantity = obj["cancellableQuantity"]
    if not isinstance(cancellable_quantity, int):
        raise ValueError("Expected int for cancellable_quantity")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformCancellableProductQuantityExceededError(product_id, cancellable_quantity, message)
