from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformPaymentNotFoundError:
    type: Literal["PLATFORM_PAYMENT_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_payment_not_found_error(obj: PlatformPaymentNotFoundError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_PAYMENT_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_payment_not_found_error(obj: Any) -> PlatformPaymentNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_PAYMENT_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_PAYMENT_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformPaymentNotFoundError(type, message)
