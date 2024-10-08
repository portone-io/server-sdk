from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementCycleMethodDailyInput:
    pass


def _serialize_platform_settlement_cycle_method_daily_input(obj: PlatformSettlementCycleMethodDailyInput) -> Any:
    entity = {}
    return entity


def _deserialize_platform_settlement_cycle_method_daily_input(obj: Any) -> PlatformSettlementCycleMethodDailyInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    return PlatformSettlementCycleMethodDailyInput()
