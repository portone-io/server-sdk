from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class PlatformSettlementCycleMethodDaily:
    """매일 정산
    """
    pass


def _serialize_platform_settlement_cycle_method_daily(obj: PlatformSettlementCycleMethodDaily) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["type"] = "DAILY"
    return entity


def _deserialize_platform_settlement_cycle_method_daily(obj: Any) -> PlatformSettlementCycleMethodDaily:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "type" not in obj:
        raise KeyError("Missing required field 'type'")
    type = obj["type"]
    if type != "DAILY":
        raise ValueError("Expected 'DAILY' for type")
    return PlatformSettlementCycleMethodDaily()
