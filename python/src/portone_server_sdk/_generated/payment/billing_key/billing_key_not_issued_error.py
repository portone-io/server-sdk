from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class BillingKeyNotIssuedError:
    type: Literal["BILLING_KEY_NOT_ISSUED"] = field(repr=False)
    message: Optional[str]


def _serialize_billing_key_not_issued_error(obj: BillingKeyNotIssuedError) -> Any:
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
    return BillingKeyNotIssuedError(type, message)
