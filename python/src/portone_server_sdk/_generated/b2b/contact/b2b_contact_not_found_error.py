from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bContactNotFoundError:
    """담당자가 존재하지 않는 경우
    """
    type: Literal["B2B_CONTACT_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_contact_not_found_error(obj: B2bContactNotFoundError) -> Any:
    entity = {}
    entity["type"] = "B2B_CONTACT_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_contact_not_found_error(obj: Any) -> B2bContactNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_CONTACT_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'B2B_CONTACT_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bContactNotFoundError(type, message)
