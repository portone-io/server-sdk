from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionPayMethodDoesNotMatchError:
    """결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_promotion_pay_method_does_not_match_error(obj: PromotionPayMethodDoesNotMatchError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PROMOTION_PAY_METHOD_DOES_NOT_MATCH"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_promotion_pay_method_does_not_match_error(obj: Any) -> PromotionPayMethodDoesNotMatchError:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
        raise ValueError("Expected 'PROMOTION_PAY_METHOD_DOES_NOT_MATCH' for type")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError("Expected str for message")
    else:
        message = None
    return PromotionPayMethodDoesNotMatchError(message)
