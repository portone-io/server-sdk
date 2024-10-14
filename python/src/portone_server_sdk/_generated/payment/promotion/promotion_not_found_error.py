from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionNotFoundError:
    """프로모션이 존재하지 않는 경우
    """
    type: Literal["PROMOTION_NOT_FOUND"] = field(repr=False)
    message: Optional[str]


def _serialize_promotion_not_found_error(obj: PromotionNotFoundError) -> Any:
    entity = {}
    entity["type"] = "PROMOTION_NOT_FOUND"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_promotion_not_found_error(obj: Any) -> PromotionNotFoundError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PROMOTION_NOT_FOUND":
        raise ValueError(f"{repr(type)} is not 'PROMOTION_NOT_FOUND'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PromotionNotFoundError(type, message)
