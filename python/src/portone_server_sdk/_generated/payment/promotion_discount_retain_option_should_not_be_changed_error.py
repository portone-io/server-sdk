from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PromotionDiscountRetainOptionShouldNotBeChangedError:
    """프로모션 혜택 유지 옵션을 이전 부분 취소와 다른 것으로 입력한 경우
    """
    message: Optional[str] = field(default=None)


def _serialize_promotion_discount_retain_option_should_not_be_changed_error(obj: PromotionDiscountRetainOptionShouldNotBeChangedError) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED"
    if obj.message is not None:
        entity["message"] = obj.message
    return entity


def _deserialize_promotion_discount_retain_option_should_not_be_changed_error(obj: Any) -> PromotionDiscountRetainOptionShouldNotBeChangedError:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED":
        raise ValueError(f"{repr(type)} is not 'PROMOTION_DISCOUNT_RETAIN_OPTION_SHOULD_NOT_BE_CHANGED'")
    if "message" in obj:
        message = obj["message"]
        if not isinstance(message, str):
            raise ValueError(f"{repr(message)} is not str")
    else:
        message = None
    return PromotionDiscountRetainOptionShouldNotBeChangedError(message)
