from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class B2bIdAlreadyExistsError:
    """ID가 이미 사용중인 경우
    """
    type: Literal["B2B_ID_ALREADY_EXISTS"] = field(repr=False)
    message: Optional[str]


def _serialize_b2b_id_already_exists_error(obj: B2bIdAlreadyExistsError) -> Any:
    entity = {}
    entity["type"] = "B2B_ID_ALREADY_EXISTS"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_b2b_id_already_exists_error(obj: Any) -> B2bIdAlreadyExistsError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "B2B_ID_ALREADY_EXISTS":
        raise ValueError(f"{repr(type)} is not 'B2B_ID_ALREADY_EXISTS'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return B2bIdAlreadyExistsError(type, message)
