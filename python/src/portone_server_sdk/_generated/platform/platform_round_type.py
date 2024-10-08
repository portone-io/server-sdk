from __future__ import annotations
from typing import Any, Literal, Optional

PlatformRoundType = Literal["OFF", "DOWN", "UP"]
"""금액에 대한 소수점 처리 방식
"""


def _serialize_platform_round_type(obj: PlatformRoundType) -> Any:
    return obj


def _deserialize_platform_round_type(obj: Any) -> PlatformRoundType:
    if obj not in ["OFF", "DOWN", "UP"]:
        raise ValueError(f"{repr(obj)} is not PlatformRoundType")
    return obj
