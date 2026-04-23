from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyBrnInvalidError:
    """사업자등록번호가 유효하지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_brn_invalid_error(obj: B2bCounterpartyBrnInvalidError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_BRN_INVALID"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_brn_invalid_error(obj: Any) -> B2bCounterpartyBrnInvalidError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_BRN_INVALID":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_BRN_INVALID'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyBrnInvalidError(message)
