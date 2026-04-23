from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyVerificationInvalidError:
    """검증 결과가 유효하지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_verification_invalid_error(obj: B2bCounterpartyVerificationInvalidError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_VERIFICATION_INVALID"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_verification_invalid_error(obj: Any) -> B2bCounterpartyVerificationInvalidError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_VERIFICATION_INVALID":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_VERIFICATION_INVALID'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyVerificationInvalidError(message)
