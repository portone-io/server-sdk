from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellableProductQuantityExceededError:
    type: Literal["PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED"] = field(repr=False)
    product_id: str
    cancellable_quantity: int
    """(int64)
    """
    message: Optional[str]


def _serialize_platform_cancellable_product_quantity_exceeded_error(obj: PlatformCancellableProductQuantityExceededError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED"
    entity["productId"] = obj.product_id
    entity["cancellableQuantity"] = obj.cancellable_quantity
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellable_product_quantity_exceeded_error(obj: Any) -> PlatformCancellableProductQuantityExceededError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED'")
    if "productId" not in obj:
        raise KeyError(f"'productId' is not in {obj}")
    product_id = obj["productId"]
    if not isinstance(product_id, str):
        raise ValueError(f"{repr(product_id)} is not str")
    if "cancellableQuantity" not in obj:
        raise KeyError(f"'cancellableQuantity' is not in {obj}")
    cancellable_quantity = obj["cancellableQuantity"]
    if not isinstance(cancellable_quantity, int):
        raise ValueError(f"{repr(cancellable_quantity)} is not int")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCancellableProductQuantityExceededError(type, product_id, cancellable_quantity, message)
