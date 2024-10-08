from __future__ import annotations
from typing import Any, Literal, Optional

CardBrand = Literal["LOCAL", "MASTER", "UNIONPAY", "VISA", "JCB", "AMEX", "DINERS"]
"""카드 브랜드
"""


def _serialize_card_brand(obj: CardBrand) -> Any:
    return obj


def _deserialize_card_brand(obj: Any) -> CardBrand:
    if obj not in ["LOCAL", "MASTER", "UNIONPAY", "VISA", "JCB", "AMEX", "DINERS"]:
        raise ValueError(f"{repr(obj)} is not CardBrand")
    return obj
