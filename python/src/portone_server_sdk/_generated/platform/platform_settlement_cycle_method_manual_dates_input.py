from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from ..platform.month_day import MonthDay, _deserialize_month_day, _serialize_month_day

@dataclass
class PlatformSettlementCycleMethodManualDatesInput:
    dates: list[MonthDay]
    """월 및 일자 정보
    """


def _serialize_platform_settlement_cycle_method_manual_dates_input(obj: PlatformSettlementCycleMethodManualDatesInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["dates"] = list(map(_serialize_month_day, obj.dates))
    return entity


def _deserialize_platform_settlement_cycle_method_manual_dates_input(obj: Any) -> PlatformSettlementCycleMethodManualDatesInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "dates" not in obj:
        raise KeyError(f"'dates' is not in {obj}")
    dates = obj["dates"]
    if not isinstance(dates, list):
        raise ValueError(f"{repr(dates)} is not list")
    for i, item in enumerate(dates):
        item = _deserialize_month_day(item)
        dates[i] = item
    return PlatformSettlementCycleMethodManualDatesInput(dates)
