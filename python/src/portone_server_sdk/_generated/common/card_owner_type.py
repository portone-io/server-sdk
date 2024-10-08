from __future__ import annotations
from typing import Any, Literal, Optional

CardOwnerType = Literal["PERSONAL", "CORPORATE"]
"""카드 소유주 유형
"""


def _serialize_card_owner_type(obj: CardOwnerType) -> Any:
    return obj


def _deserialize_card_owner_type(obj: Any) -> CardOwnerType:
    if obj not in ["PERSONAL", "CORPORATE"]:
        raise ValueError(f"{repr(obj)} is not CardOwnerType")
    return obj
