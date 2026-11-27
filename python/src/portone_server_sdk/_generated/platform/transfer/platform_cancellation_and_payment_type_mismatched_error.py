from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformCancellationAndPaymentTypeMismatchedError:
    message: Optional[str] = field(default=None)


def _serialize_platform_cancellation_and_payment_type_mismatched_error(obj: PlatformCancellationAndPaymentTypeMismatchedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_platform_cancellation_and_payment_type_mismatched_error(obj: Any) -> PlatformCancellationAndPaymentTypeMismatchedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED":
        raise ValueError("Expected 'PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PlatformCancellationAndPaymentTypeMismatchedError(message)
