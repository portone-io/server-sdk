from __future__ import annotations
from typing import Any, Literal, Optional, Union

CardOwnerType = Union[Literal["PERSONAL", "CORPORATE"], str]
"""카드 소유주 유형
"""


def _serialize_card_owner_type(obj: CardOwnerType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_card_owner_type(obj: Any) -> CardOwnerType:
    return obj
