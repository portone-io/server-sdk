from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementParameterValue:
    """플랫폼 정산 파라미터 값
    """
    decimal: int
    """크기가 조정되지 않은 숫자
    (int64)
    """
    decimal_scale: Optional[int] = field(default=None)
    """소수 자리수

    정산 시 필요한 `decimalScale`이 지정되지 않은 경우 기본값으로 0을 사용합니다.
    입력 가능한 법위는 0 ~ 5 입니다.
    (int32)
    """


def _serialize_platform_settlement_parameter_value(obj: PlatformSettlementParameterValue) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["decimal"] = obj.decimal
    if obj.decimal_scale is not None:
        entity["decimalScale"] = obj.decimal_scale
    return entity


def _deserialize_platform_settlement_parameter_value(obj: Any) -> PlatformSettlementParameterValue:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "decimal" not in obj:
        raise KeyError(f"'decimal' is not in {obj}")
    decimal = obj["decimal"]
    if not isinstance(decimal, int):
        raise ValueError(f"{repr(decimal)} is not int")
    if "decimalScale" in obj:
        decimal_scale = obj["decimalScale"]
        if not isinstance(decimal_scale, int):
            raise ValueError(f"{repr(decimal_scale)} is not int")
    else:
        decimal_scale = None
    return PlatformSettlementParameterValue(decimal, decimal_scale)
