from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.additional_feature.pg_card_promotion import PgCardPromotion, _deserialize_pg_card_promotion, _serialize_pg_card_promotion

@dataclass
class GetPgCardPromotionsResponse:
    """PG사 카드 프로모션 조회 응답
    """
    promotions: Optional[list[PgCardPromotion]] = field(default=None)
    """카드 프로모션 목록
    """


def _serialize_get_pg_card_promotions_response(obj: GetPgCardPromotionsResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.promotions is not None:
        entity["promotions"] = list(map(_serialize_pg_card_promotion, obj.promotions))
    return entity


def _deserialize_get_pg_card_promotions_response(obj: Any) -> GetPgCardPromotionsResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "promotions" in obj:
        promotions = obj["promotions"]
        if not isinstance(promotions, list):
            raise ValueError(f"{repr(promotions)} is not list")
        for i, item in enumerate(promotions):
            item = _deserialize_pg_card_promotion(item)
            promotions[i] = item
    else:
        promotions = None
    return GetPgCardPromotionsResponse(promotions)
