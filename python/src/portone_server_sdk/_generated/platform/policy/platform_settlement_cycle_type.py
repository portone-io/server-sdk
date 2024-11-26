from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformSettlementCycleType = Union[Literal["DAILY", "WEEKLY", "MONTHLY", "MANUAL_DATES"], str]
"""플랫폼 정산 주기 계산 방식
"""


def _serialize_platform_settlement_cycle_type(obj: PlatformSettlementCycleType) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_settlement_cycle_type(obj: Any) -> PlatformSettlementCycleType:
    return obj
