from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyNotIssuedError:
    message: Optional[str] = field(default=None)


def _serialize_billing_key_not_issued_error(obj: BillingKeyNotIssuedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "BILLING_KEY_NOT_ISSUED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_billing_key_not_issued_error(obj: Any) -> BillingKeyNotIssuedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "BILLING_KEY_NOT_ISSUED":
        raise ValueError(f"{repr(type)} is not 'BILLING_KEY_NOT_ISSUED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return BillingKeyNotIssuedError(message)
