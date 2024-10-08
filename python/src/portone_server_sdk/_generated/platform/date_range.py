from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DateRange:
    from_: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    until: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """


def _serialize_date_range(obj: DateRange) -> Any:
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    return entity


def _deserialize_date_range(obj: Any) -> DateRange:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "from" not in obj:
        raise KeyError(f"'from' is not in {obj}")
    from_ = obj["from"]
    if not isinstance(from_, str):
        raise ValueError(f"{repr(from_)} is not str")
    if "until" not in obj:
        raise KeyError(f"'until' is not in {obj}")
    until = obj["until"]
    if not isinstance(until, str):
        raise ValueError(f"{repr(until)} is not str")
    return DateRange(from_, until)
