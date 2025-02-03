from __future__ import annotations
from typing import Any, Optional, Union
from ..platform.platform_fixed_amount_fee import PlatformFixedAmountFee, _deserialize_platform_fixed_amount_fee, _serialize_platform_fixed_amount_fee
from ..platform.platform_fixed_rate_fee import PlatformFixedRateFee, _deserialize_platform_fixed_rate_fee, _serialize_platform_fixed_rate_fee

PlatformFee = Union[PlatformFixedAmountFee, PlatformFixedRateFee, dict]
"""플랫폼 중개수수료 정보
"""


def _serialize_platform_fee(obj: PlatformFee) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, PlatformFixedAmountFee):
        return _serialize_platform_fixed_amount_fee(obj)
    if isinstance(obj, PlatformFixedRateFee):
        return _serialize_platform_fixed_rate_fee(obj)


def _deserialize_platform_fee(obj: Any) -> PlatformFee:
    try:
        return _deserialize_platform_fixed_amount_fee(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_fixed_rate_fee(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not PlatformFee")
