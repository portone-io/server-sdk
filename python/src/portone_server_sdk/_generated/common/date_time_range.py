from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DateTimeRange:
    """시간 범위
    """
    from_: str
    """(RFC 3339 date-time)
    """
    until: str
    """(RFC 3339 date-time)
    """


def _serialize_date_time_range(obj: DateTimeRange) -> Any:
    entity = {}
    entity["from"] = obj.from_
    entity["until"] = obj.until
    return entity


def _deserialize_date_time_range(obj: Any) -> DateTimeRange:
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
    return DateTimeRange(from_, until)
