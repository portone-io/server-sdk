from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.promotion.promotion_amount_discount_scheme import PromotionAmountDiscountScheme, _deserialize_promotion_amount_discount_scheme, _serialize_promotion_amount_discount_scheme
from ...payment.promotion.promotion_percent_discount_scheme import PromotionPercentDiscountScheme, _deserialize_promotion_percent_discount_scheme, _serialize_promotion_percent_discount_scheme

PromotionDiscountScheme = Union[PromotionAmountDiscountScheme, PromotionPercentDiscountScheme, dict]


def _serialize_promotion_discount_scheme(obj: PromotionDiscountScheme) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PromotionAmountDiscountScheme):
        return _serialize_promotion_amount_discount_scheme(obj)
    if isinstance(obj, PromotionPercentDiscountScheme):
        return _serialize_promotion_percent_discount_scheme(obj)


def _deserialize_promotion_discount_scheme(obj: Any) -> PromotionDiscountScheme:
    try:
        return _deserialize_promotion_amount_discount_scheme(obj)
    except Exception:
        pass
    try:
        return _deserialize_promotion_percent_discount_scheme(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PromotionDiscountScheme")
