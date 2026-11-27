from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bIssuanceTypeMismatchError:
    """세금계산서 발행 유형이 올바르지 않은 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_issuance_type_mismatch_error(obj: B2bIssuanceTypeMismatchError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_ISSUANCE_TYPE_MISMATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_issuance_type_mismatch_error(obj: Any) -> B2bIssuanceTypeMismatchError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_ISSUANCE_TYPE_MISMATCH":
        raise ValueError("Expected 'B2B_ISSUANCE_TYPE_MISMATCH' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2bIssuanceTypeMismatchError(message)
