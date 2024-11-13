from __future__ import annotations
from typing import Any, Literal, Optional, Union

PromotionDiscountRetainOption = Union[Literal["RETAIN", "RELEASE"], str]


def _serialize_promotion_discount_retain_option(obj: PromotionDiscountRetainOption) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_promotion_discount_retain_option(obj: Any) -> PromotionDiscountRetainOption:
    return obj
