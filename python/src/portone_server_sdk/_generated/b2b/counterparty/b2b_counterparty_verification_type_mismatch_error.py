from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bCounterpartyVerificationTypeMismatchError:
    """검증 유형이 일치하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_counterparty_verification_type_mismatch_error(obj: B2bCounterpartyVerificationTypeMismatchError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_COUNTERPARTY_VERIFICATION_TYPE_MISMATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_counterparty_verification_type_mismatch_error(obj: Any) -> B2bCounterpartyVerificationTypeMismatchError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_COUNTERPARTY_VERIFICATION_TYPE_MISMATCH":
        raise ValueError(f"{repr(type)} is not 'B2B_COUNTERPARTY_VERIFICATION_TYPE_MISMATCH'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bCounterpartyVerificationTypeMismatchError(message)
