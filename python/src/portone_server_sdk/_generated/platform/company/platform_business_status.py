from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformBusinessStatus = Union[Literal["IN_BUSINESS", "CLOSED", "SUSPENDED"], str]
"""플랫폼 사업자 상태
"""


def _serialize_platform_business_status(obj: PlatformBusinessStatus) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_business_status(obj: Any) -> PlatformBusinessStatus:
    return obj
