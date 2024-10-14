from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.payment.promotion.promotion_amount_discount import PromotionAmountDiscount, _deserialize_promotion_amount_discount, _serialize_promotion_amount_discount
from portone_server_sdk._generated.payment.promotion.promotion_percent_discount import PromotionPercentDiscount, _deserialize_promotion_percent_discount, _serialize_promotion_percent_discount

PromotionDiscount = Union[PromotionAmountDiscount, PromotionPercentDiscount]


def _serialize_promotion_discount(obj: PromotionDiscount) -> Any:
    if obj.type == "AMOUNT":
        return _serialize_promotion_amount_discount(obj)
    if obj.type == "PERCENT":
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
    raise ValueError(f"{repr(obj)} is not PromotionDiscount")
