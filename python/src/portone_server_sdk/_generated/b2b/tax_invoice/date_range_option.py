from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class DateRangeOption:
    from_: Optional[str] = field(default=None)
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    until: Optional[str] = field(default=None)
    """날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """


def _serialize_date_range_option(obj: DateRangeOption) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.from_ is not None:
        entity["from"] = obj.from_
    if obj.until is not None:
        entity["until"] = obj.until
    return entity


def _deserialize_date_range_option(obj: Any) -> DateRangeOption:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "from" in obj:
        from_ = obj["from"]
        if not isinstance(from_, str):
            raise ValueError(f"{repr(from_)} is not str")
    else:
        from_ = None
    if "until" in obj:
        until = obj["until"]
        if not isinstance(until, str):
            raise ValueError(f"{repr(until)} is not str")
    else:
        until = None
    return DateRangeOption(from_, until)
