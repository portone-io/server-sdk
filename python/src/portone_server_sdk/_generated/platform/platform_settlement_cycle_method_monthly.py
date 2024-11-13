from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementCycleMethodMonthly:
    """매월 정해진 날(일)에 정산
    """
    days_of_month: list[int]


def _serialize_platform_settlement_cycle_method_monthly(obj: PlatformSettlementCycleMethodMonthly) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "MONTHLY"
    entity["daysOfMonth"] = obj.days_of_month
    return entity


def _deserialize_platform_settlement_cycle_method_monthly(obj: Any) -> PlatformSettlementCycleMethodMonthly:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "type" not in obj:
        raise KeyError(f"'type' is not in {obj}")
    type = obj["type"]
    if type != "MONTHLY":
        raise ValueError(f"{repr(type)} is not 'MONTHLY'")
    if "daysOfMonth" not in obj:
        raise KeyError(f"'daysOfMonth' is not in {obj}")
    days_of_month = obj["daysOfMonth"]
    if not isinstance(days_of_month, list):
        raise ValueError(f"{repr(days_of_month)} is not list")
    for i, item in enumerate(days_of_month):
        if not isinstance(item, int):
            raise ValueError(f"{repr(item)} is not int")
    return PlatformSettlementCycleMethodMonthly(days_of_month)
