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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "INVALID_PAYMENT_TOKEN":
        raise ValueError("Expected 'INVALID_PAYMENT_TOKEN' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return InvalidPaymentTokenError(message)
