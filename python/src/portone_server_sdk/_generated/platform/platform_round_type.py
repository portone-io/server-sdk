from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformRoundType = Union[Literal["OFF", "DOWN", "UP"], str]
"""금액에 대한 소수점 처리 방식
"""


def _serialize_platform_round_type(obj: PlatformRoundType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_round_type(obj: Any) -> PlatformRoundType:
    return obj
