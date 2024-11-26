from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PaymentNotPaidError:
    """결제가 완료되지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_payment_not_paid_error(obj: PaymentNotPaidError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PAYMENT_NOT_PAID"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_payment_not_paid_error(obj: Any) -> PaymentNotPaidError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PAYMENT_NOT_PAID":
        raise ValueError(f"{repr(type)} is not 'PAYMENT_NOT_PAID'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PaymentNotPaidError(message)
