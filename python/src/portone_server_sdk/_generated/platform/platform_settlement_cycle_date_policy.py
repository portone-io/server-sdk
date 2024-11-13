from __future__ import annotations
from typing import Any, Literal, Optional, Union

PlatformSettlementCycleDatePolicy = Union[Literal["HOLIDAY_BEFORE", "HOLIDAY_AFTER", "CALENDAR_DAY"], str]
"""플랫폼 정산 기준일
"""


def _serialize_platform_settlement_cycle_date_policy(obj: PlatformSettlementCycleDatePolicy) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_platform_settlement_cycle_date_policy(obj: Any) -> PlatformSettlementCycleDatePolicy:
    return obj
