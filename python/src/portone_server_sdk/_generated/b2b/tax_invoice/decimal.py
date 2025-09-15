from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class Decimal:
    """BigDecimal 타입
    """
    value: int
    """비정규화된 값

    소수점 숫자의 비정규화된(unscaled) 값을 정수로 저장합니다. 예를 들어, 123.45의 경우 12345가 저장됩니다.
    (int64)
    """
    scale: Optional[int] = field(default=None)
    """소수점 이하 자릿수

    소수점 숫자의 소수점 이하 자릿수를 저장합니다. 기본값은 0입니다. 예를 들어, 123.45의 경우 2가 저장됩니다.
    (int32)
    """


def _serialize_decimal(obj: Decimal) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["value"] = obj.value
    if obj.scale is not None:
        entity["scale"] = obj.scale
    return entity


def _deserialize_decimal(obj: Any) -> Decimal:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "value" not in obj:
        raise KeyError(f"'value' is not in {obj}")
    value = obj["value"]
    if not isinstance(value, int):
        raise ValueError(f"{repr(value)} is not int")
    if "scale" in obj:
        scale = obj["scale"]
        if not isinstance(scale, int):
            raise ValueError(f"{repr(scale)} is not int")
    else:
        scale = None
    return Decimal(value, scale)
