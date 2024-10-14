from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionPayMethodDoesNotMatchError:
    """결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
    """
    type: Literal["PROMOTION_PAY_METHOD_DOES_NOT_MATCH"] = field(repr=False)
    message: Optional[str]


def _serialize_promotion_pay_method_does_not_match_error(obj: PromotionPayMethodDoesNotMatchError) -> Any:
    entity = {}
    entity["type"] = "PROMOTION_PAY_METHOD_DOES_NOT_MATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_promotion_pay_method_does_not_match_error(obj: Any) -> PromotionPayMethodDoesNotMatchError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
        raise ValueError(f"{repr(type)} is not 'PROMOTION_PAY_METHOD_DOES_NOT_MATCH'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PromotionPayMethodDoesNotMatchError(type, message)
