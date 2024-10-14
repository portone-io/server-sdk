from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class AlreadyPaidError:
    """결제가 이미 완료된 경우
    """
    type: Literal["ALREADY_PAID"] = field(repr=False)
    message: Optional[str]


def _serialize_already_paid_error(obj: AlreadyPaidError) -> Any:
    entity = {}
    entity["type"] = "ALREADY_PAID"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_already_paid_error(obj: Any) -> AlreadyPaidError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "ALREADY_PAID":
        raise ValueError(f"{repr(type)} is not 'ALREADY_PAID'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return AlreadyPaidError(type, message)
