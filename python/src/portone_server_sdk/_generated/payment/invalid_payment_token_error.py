from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class InvalidPaymentTokenError:
    """유효하지 않은 결제 토큰인 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_invalid_payment_token_error(obj: InvalidPaymentTokenError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "INVALID_PAYMENT_TOKEN"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_invalid_payment_token_error(obj: Any) -> InvalidPaymentTokenError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "INVALID_PAYMENT_TOKEN":
        raise ValueError(f"{repr(type)} is not 'INVALID_PAYMENT_TOKEN'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return InvalidPaymentTokenError(message)
