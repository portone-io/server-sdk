from __future__ import annotations
from typing import Any, Literal, Optional, Union

CardBrand = Union[Literal["LOCAL", "MASTER", "UNIONPAY", "VISA", "JCB", "AMEX", "DINERS"], str]
"""카드 브랜드
"""


def _serialize_card_brand(obj: CardBrand) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_card_brand(obj: Any) -> CardBrand:
    return obj
