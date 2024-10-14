from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellationAndPaymentTypeMismatchedError:
    type: Literal["PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED"] = field(repr=False)
    message: Optional[str]


def _serialize_platform_cancellation_and_payment_type_mismatched_error(obj: PlatformCancellationAndPaymentTypeMismatchedError) -> Any:
    entity = {}
    entity["type"] = "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellation_and_payment_type_mismatched_error(obj: Any) -> PlatformCancellationAndPaymentTypeMismatchedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED":
        raise ValueError(f"{repr(type)} is not 'PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PlatformCancellationAndPaymentTypeMismatchedError(type, message)
