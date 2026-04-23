from __future__ import annotations
from typing import Any, Literal, Optional, Union

PaymentOriginPlatformType = Union[Literal["PC", "MOBILE", "API"], str]
"""플랫폼 타입
"""


def _serialize_payment_origin_platform_type(obj: PaymentOriginPlatformType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_payment_origin_platform_type(obj: Any) -> PaymentOriginPlatformType:
    return obj
