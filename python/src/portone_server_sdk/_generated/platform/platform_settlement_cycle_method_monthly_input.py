from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementCycleMethodMonthlyInput:
    days_of_month: list[int]


def _serialize_platform_settlement_cycle_method_monthly_input(obj: PlatformSettlementCycleMethodMonthlyInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["daysOfMonth"] = obj.days_of_month
    return entity


def _deserialize_platform_settlement_cycle_method_monthly_input(obj: Any) -> PlatformSettlementCycleMethodMonthlyInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "daysOfMonth" not in obj:
        raise KeyError(f"'daysOfMonth' is not in {obj}")
    days_of_month = obj["daysOfMonth"]
    if not isinstance(days_of_month, list):
        raise ValueError(f"{repr(days_of_month)} is not list")
    for i, item in enumerate(days_of_month):
        if not isinstance(item, int):
            raise ValueError(f"{repr(item)} is not int")
    return PlatformSettlementCycleMethodMonthlyInput(days_of_month)
