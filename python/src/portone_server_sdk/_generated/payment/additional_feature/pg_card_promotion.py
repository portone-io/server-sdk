from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ...payment.additional_feature.pg_promotion_card_company import PgPromotionCardCompany, _deserialize_pg_promotion_card_company, _serialize_pg_promotion_card_company

@dataclass
class PgCardPromotion:
    """PG사 카드 프로모션

    PG사에서 제공하는 카드 프로모션 정보입니다.
    """
    promotion_id: str
    """프로모션 아이디

    PG사에서 부여한 프로모션 식별자입니다.
    """
    card_company: PgPromotionCardCompany
    """카드사

    프로모션이 적용되는 카드사입니다.
    """
    discount_amount: int
    """할인 금액

    프로모션 적용 시 할인되는 금액입니다.
    (int64)
    """
    minimum_payment_amount: int
    """최소 결제 금액

    프로모션이 적용되기 위한 최소 결제 금액입니다.
    (int64)
    """


def _serialize_pg_card_promotion(obj: PgCardPromotion) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["promotionId"] = obj.promotion_id
    entity["cardCompany"] = _serialize_pg_promotion_card_company(obj.card_company)
    entity["discountAmount"] = obj.discount_amount
    entity["minimumPaymentAmount"] = obj.minimum_payment_amount
    return entity


def _deserialize_pg_card_promotion(obj: Any) -> PgCardPromotion:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "promotionId" not in obj:
        raise KeyError("Missing required field 'promotionId'")
    promotion_id = obj["promotionId"]
    if not isinstance(promotion_id, str):
        raise ValueError("Expected str for promotion_id")
    if "cardCompany" not in obj:
        raise KeyError("Missing required field 'cardCompany'")
    card_company = obj["cardCompany"]
    card_company = _deserialize_pg_promotion_card_company(card_company)
    if "discountAmount" not in obj:
        raise KeyError("Missing required field 'discountAmount'")
    discount_amount = obj["discountAmount"]
    if not isinstance(discount_amount, int):
        raise ValueError("Expected int for discount_amount")
    if "minimumPaymentAmount" not in obj:
        raise KeyError("Missing required field 'minimumPaymentAmount'")
    minimum_payment_amount = obj["minimumPaymentAmount"]
    if not isinstance(minimum_payment_amount, int):
        raise ValueError("Expected int for minimum_payment_amount")
    return PgCardPromotion(promotion_id, card_company, discount_amount, minimum_payment_amount)
