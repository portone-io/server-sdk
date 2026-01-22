from __future__ import annotations
from typing import Any, Literal, Optional, Union

PgPromotionCardCompany = Union[Literal["KOREA_DEVELOPMENT_BANK", "KFCC", "SHINHYUP", "EPOST", "SAVINGS_BANK_KOREA", "KAKAO_BANK", "WOORI_CARD", "BC_CARD", "GWANGJU_CARD", "SAMSUNG_CARD", "SHINHAN_CARD", "HYUNDAI_CARD", "LOTTE_CARD", "SUHYUP_CARD", "CITI_CARD", "NH_CARD", "JEONBUK_CARD", "JEJU_CARD", "HANA_CARD", "KOOKMIN_CARD", "K_BANK", "TOSS_BANK", "MIRAE_ASSET_SECURITIES"], str]
"""PG 프로모션 카드사

PG사 프로모션 조회 시 필터링할 수 있는 카드사 목록입니다.
"""


def _serialize_pg_promotion_card_company(obj: PgPromotionCardCompany) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_pg_promotion_card_company(obj: Any) -> PgPromotionCardCompany:
    return obj
