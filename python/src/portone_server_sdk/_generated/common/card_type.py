from __future__ import annotations
from typing import Any, Literal, Optional, Union

CardType = Union[Literal["CREDIT", "DEBIT", "GIFT"], str]
"""카드 유형
"""


def _serialize_card_type(obj: CardType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_card_type(obj: Any) -> CardType:
    return obj
