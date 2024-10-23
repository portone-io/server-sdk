from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2BCannotChangeTaxTypeError:
    """세금계산서 과세 유형을 수정할 수 없는 경우
    """
    type: Literal["B2B_CANNOT_CHANGE_TAX_TYPE"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_cannot_change_tax_type_error(obj: B2BCannotChangeTaxTypeError) -> Any:
    entity = {}
    entity["type"] = "B2B_CANNOT_CHANGE_TAX_TYPE"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_cannot_change_tax_type_error(obj: Any) -> B2BCannotChangeTaxTypeError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_CANNOT_CHANGE_TAX_TYPE":
        raise ValueError(f"{repr(type)} is not 'B2B_CANNOT_CHANGE_TAX_TYPE'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2BCannotChangeTaxTypeError(type, message)
