from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.platform.month_day import MonthDay, _deserialize_month_day, _serialize_month_day

@dataclass
class PlatformSettlementCycleMethodManualDates:
    """정해진 날짜(월, 일)에 정산
    """
    type: Literal["MANUAL_DATES"] = field(repr=False)
    dates: list[MonthDay]
    """월 및 일자 정보
    """


def _serialize_platform_settlement_cycle_method_manual_dates(obj: PlatformSettlementCycleMethodManualDates) -> Any:
    entity = {}
    entity["type"] = "MANUAL_DATES"
    entity["dates"] = list(map(_serialize_month_day, obj.dates))
    return entity


def _deserialize_platform_settlement_cycle_method_manual_dates(obj: Any) -> PlatformSettlementCycleMethodManualDates:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MANUAL_DATES":
        raise ValueError(f"{repr(type)} is not 'MANUAL_DATES'")
    if "dates" not in obj:
        raise KeyError(f"'dates' is not in {obj}")
    dates = obj["dates"]
    if not isinstance(dates, list):
        raise ValueError(f"{repr(dates)} is not list")
    for i, item in enumerate(dates):
        item = _deserialize_month_day(item)
        dates[i] = item
    return PlatformSettlementCycleMethodManualDates(type, dates)
