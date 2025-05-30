from __future__ import annotations
from typing import Any, Literal, Optional, Union

ConvenienceStoreBrand = Union[Literal["LAWSON", "FAMILY_MART", "MINI_STOP", "SEVEN_ELEVEN", "SEICOMART"], str]
"""편의점 브랜드
"""


def _serialize_convenience_store_brand(obj: ConvenienceStoreBrand) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_convenience_store_brand(obj: Any) -> ConvenienceStoreBrand:
    return obj
