from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformFeeInput:
    """수수료 계산 방식을 특정하기 위한 입력 정보

    정률 수수료를 설정하고 싶은 경우 `fixedRate` 필드에, 정액 수수료를 설정하고 싶은 경우 `fixedAmount` 필드에 값을 명시해 요청합니다.
    두 필드 모두 값이 들어있지 않은 경우 요청이 거절됩니다.
    """
    fixed_rate: Optional[int]
    """정률 수수료
    (int32)
    """
    fixed_amount: Optional[int]
    """정액 수수료
    (int64)
    """


def _serialize_platform_fee_input(obj: PlatformFeeInput) -> Any:
    entity = {}
    if obj.fixed_rate is not None:
        entity["fixedRate"] = obj.fixed_rate
    if obj.fixed_amount is not None:
        entity["fixedAmount"] = obj.fixed_amount
    return entity


def _deserialize_platform_fee_input(obj: Any) -> PlatformFeeInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "fixedRate" in obj:
        fixed_rate = obj["fixedRate"]
        if not isinstance(fixed_rate, int):
            raise ValueError(f"{repr(fixed_rate)} is not int")
    else:
        fixed_rate = None
    if "fixedAmount" in obj:
        fixed_amount = obj["fixedAmount"]
        if not isinstance(fixed_amount, int):
            raise ValueError(f"{repr(fixed_amount)} is not int")
    else:
        fixed_amount = None
    return PlatformFeeInput(fixed_rate, fixed_amount)
