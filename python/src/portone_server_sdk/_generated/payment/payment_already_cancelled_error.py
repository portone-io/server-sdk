from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentAlreadyCancelledError:
    """결제가 이미 취소된 경우
    """
    type: Literal["PAYMENT_ALREADY_CANCELLED"] = field(repr=False)
    message: Optional[str]


def _serialize_payment_already_cancelled_error(obj: PaymentAlreadyCancelledError) -> Any:
    entity = {}
    entity["type"] = "PAYMENT_ALREADY_CANCELLED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_already_cancelled_error(obj: Any) -> PaymentAlreadyCancelledError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_ALREADY_CANCELLED":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_ALREADY_CANCELLED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentAlreadyCancelledError(type, message)
