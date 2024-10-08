from __future__ import annotations
from typing import Any, Literal, Optional

CardType = Literal["CREDIT", "DEBIT", "GIFT"]
"""카드 유형
"""


def _serialize_card_type(obj: CardType) -> Any:
    return obj


def _deserialize_card_type(obj: Any) -> CardType:
    if obj not in ["CREDIT", "DEBIT", "GIFT"]:
        raise ValueError(f"{repr(obj)} is not CardType")
    return obj
