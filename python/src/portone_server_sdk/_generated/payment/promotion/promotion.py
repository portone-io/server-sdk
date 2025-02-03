from __future__ import annotations
from typing import Any, Optional
from ...payment.promotion.card_promotion import CardPromotion, _deserialize_card_promotion, _serialize_card_promotion

Promotion = CardPromotion
"""프로모션
"""


def _serialize_promotion(obj: Promotion) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, CardPromotion):
        return _serialize_card_promotion(obj)


def _deserialize_promotion(obj: Any) -> Promotion:
    try:
        return _deserialize_card_promotion(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not Promotion")
