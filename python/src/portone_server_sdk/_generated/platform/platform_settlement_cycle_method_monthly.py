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
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "MONTHLY":
        raise ValueError("Expected 'MONTHLY' for type")
    if "daysOfMonth" not in obj:
        raise KeyError("Missing required field 'daysOfMonth'")
    days_of_month = obj["daysOfMonth"]
    if not isinstance(days_of_month, list):
        raise ValueError("Expected list for days_of_month")
    for i, item in enumerate(days_of_month):
        if not isinstance(item, int):
            raise ValueError("Expected int for item")
    return PlatformSettlementCycleMethodMonthly(days_of_month)
