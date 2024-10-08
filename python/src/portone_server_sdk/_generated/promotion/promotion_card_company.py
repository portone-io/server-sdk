from __future__ import annotations
from typing import Any, Literal, Optional

PromotionCardCompany = Literal["WOORI_CARD", "BC_CARD", "SAMSUNG_CARD", "SHINHAN_CARD", "HYUNDAI_CARD", "LOTTE_CARD", "NH_CARD", "HANA_CARD", "KOOKMIN_CARD"]
"""프로모션 적용 가능한 카드사
"""


def _serialize_promotion_card_company(obj: PromotionCardCompany) -> Any:
    return obj


def _deserialize_promotion_card_company(obj: Any) -> PromotionCardCompany:
    if obj not in ["WOORI_CARD", "BC_CARD", "SAMSUNG_CARD", "SHINHAN_CARD", "HYUNDAI_CARD", "LOTTE_CARD", "NH_CARD", "HANA_CARD", "KOOKMIN_CARD"]:
        raise ValueError(f"{repr(obj)} is not PromotionCardCompany")
    return obj
