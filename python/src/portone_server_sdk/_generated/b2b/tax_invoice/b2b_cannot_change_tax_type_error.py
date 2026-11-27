from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2BCannotChangeTaxTypeError:
    """세금계산서 과세 유형을 수정할 수 없는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_b2b_cannot_change_tax_type_error(obj: B2BCannotChangeTaxTypeError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "B2B_CANNOT_CHANGE_TAX_TYPE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_cannot_change_tax_type_error(obj: Any) -> B2BCannotChangeTaxTypeError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "B2B_CANNOT_CHANGE_TAX_TYPE":
        raise ValueError("Expected 'B2B_CANNOT_CHANGE_TAX_TYPE' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return B2BCannotChangeTaxTypeError(message)
