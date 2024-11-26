from __future__ import annotations
from typing import Any, Optional, Union
from ...payment.promotion.promotion_amount_discount import PromotionAmountDiscount, _deserialize_promotion_amount_discount, _serialize_promotion_amount_discount
from ...payment.promotion.promotion_percent_discount import PromotionPercentDiscount, _deserialize_promotion_percent_discount, _serialize_promotion_percent_discount

PromotionDiscount = Union[PromotionAmountDiscount, PromotionPercentDiscount, dict]


def _serialize_promotion_discount(obj: PromotionDiscount) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PromotionAmountDiscount):
        return _serialize_promotion_amount_discount(obj)
    if isinstance(obj, PromotionPercentDiscount):
        return _serialize_promotion_percent_discount(obj)


def _deserialize_promotion_discount(obj: Any) -> PromotionDiscount:
    try:
        return _deserialize_promotion_amount_discount(obj)
    except Exception:
        pass
    try:
        return _deserialize_promotion_percent_discount(obj)
    except Exception:
        pass
    return obj
