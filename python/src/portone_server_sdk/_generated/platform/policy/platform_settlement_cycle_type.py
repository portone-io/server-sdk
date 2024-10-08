from __future__ import annotations
from typing import Any, Literal, Optional

PlatformSettlementCycleType = Literal["DAILY", "WEEKLY", "MONTHLY", "MANUAL_DATES"]
"""플랫폼 정산 주기 계산 방식
"""


def _serialize_platform_settlement_cycle_type(obj: PlatformSettlementCycleType) -> Any:
    return obj


def _deserialize_platform_settlement_cycle_type(obj: Any) -> PlatformSettlementCycleType:
    if obj not in ["DAILY", "WEEKLY", "MONTHLY", "MANUAL_DATES"]:
        raise ValueError(f"{repr(obj)} is not PlatformSettlementCycleType")
    return obj
