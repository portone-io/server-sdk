from __future__ import annotations
from typing import Any, Literal, Optional

PlatformSettlementCycleDatePolicy = Literal["HOLIDAY_BEFORE", "HOLIDAY_AFTER", "CALENDAR_DAY"]
"""플랫폼 정산 기준일
"""


def _serialize_platform_settlement_cycle_date_policy(obj: PlatformSettlementCycleDatePolicy) -> Any:
    return obj


def _deserialize_platform_settlement_cycle_date_policy(obj: Any) -> PlatformSettlementCycleDatePolicy:
    if obj not in ["HOLIDAY_BEFORE", "HOLIDAY_AFTER", "CALENDAR_DAY"]:
        raise ValueError(f"{repr(obj)} is not PlatformSettlementCycleDatePolicy")
    return obj
