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
        raise ValueError("Expected dict for obj")
    if "daysOfMonth" not in obj:
        raise KeyError("Missing required field 'daysOfMonth'")
    days_of_month = obj["daysOfMonth"]
    if not isinstance(days_of_month, list):
        raise ValueError("Expected list for days_of_month")
    for i, item in enumerate(days_of_month):
        if not isinstance(item, int):
            raise ValueError("Expected int for item")
    return PlatformSettlementCycleMethodMonthlyInput(days_of_month)
