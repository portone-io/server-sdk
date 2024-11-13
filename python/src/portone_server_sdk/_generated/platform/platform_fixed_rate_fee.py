from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformFixedRateFee:
    """정률 수수료

    총 금액에 정해진 비율을 곱한 만큼의 수수료를 책정합니다.
    """
    rate: int
    """수수료율

    총 금액 대비 수수료 비율을 의미하며, 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수입니다. `총 금액 * rate * 10^5` (`rate * 10^3 %`) 만큼 수수료를 책정합니다.
    (int32)
    """


def _serialize_platform_fixed_rate_fee(obj: PlatformFixedRateFee) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "FIXED_RATE"
    entity["rate"] = obj.rate
    return entity


def _deserialize_platform_fixed_rate_fee(obj: Any) -> PlatformFixedRateFee:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "FIXED_RATE":
        raise ValueError(f"{repr(type)} is not 'FIXED_RATE'")
    if "rate" not in obj:
        raise KeyError(f"'rate' is not in {obj}")
    rate = obj["rate"]
    if not isinstance(rate, int):
        raise ValueError(f"{repr(rate)} is not int")
    return PlatformFixedRateFee(rate)
