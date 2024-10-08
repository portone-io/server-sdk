from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.platform.platform_fixed_amount_fee import PlatformFixedAmountFee, _deserialize_platform_fixed_amount_fee, _serialize_platform_fixed_amount_fee
from portone_server_sdk._generated.platform.platform_fixed_rate_fee import PlatformFixedRateFee, _deserialize_platform_fixed_rate_fee, _serialize_platform_fixed_rate_fee

PlatformFee = Union[PlatformFixedAmountFee, PlatformFixedRateFee]
"""플랫폼 중개수수료 정보
"""


def _serialize_platform_fee(obj: PlatformFee) -> Any:
    if obj.type == "FIXED_AMOUNT":
        return _serialize_platform_fixed_amount_fee(obj)
    if obj.type == "FIXED_RATE":
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
