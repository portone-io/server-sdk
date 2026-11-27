from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DateRange:
    from_: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    until: str
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """


def _serialize_date_range(obj: DateRange) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    return entity


def _deserialize_date_range(obj: Any) -> DateRange:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "from" not in obj:
        raise KeyError("Missing required field 'from'")
    from_ = obj["from"]
    if not isinstance(from_, str):
        raise ValueError("Expected str for from_")
    if "until" not in obj:
        raise KeyError("Missing required field 'until'")
    until = obj["until"]
    if not isinstance(until, str):
        raise ValueError("Expected str for until")
    return DateRange(from_, until)
