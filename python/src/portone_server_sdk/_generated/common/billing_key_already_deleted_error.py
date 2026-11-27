from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyAlreadyDeletedError:
    """빌링키가 이미 삭제된 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_billing_key_already_deleted_error(obj: BillingKeyAlreadyDeletedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BILLING_KEY_ALREADY_DELETED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_billing_key_already_deleted_error(obj: Any) -> BillingKeyAlreadyDeletedError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "BILLING_KEY_ALREADY_DELETED":
        raise ValueError("Expected 'BILLING_KEY_ALREADY_DELETED' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return BillingKeyAlreadyDeletedError(message)
